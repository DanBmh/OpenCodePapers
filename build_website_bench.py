import argparse
import ast
import html
import json
import os
import re
from datetime import datetime

# ==================================================================================================

MD_JSON_BLOCK_RE = re.compile(
    r"```json:table\s*(\{.*?\})\s*```",
    re.DOTALL | re.IGNORECASE,
)

TITLE_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
TASK_HIER_RE = re.compile(r"Task\s*Hierarchy:\s*(\[.*?\])", re.IGNORECASE)
DATASET_LINK_RE = re.compile(r"\[Dataset Link\]\((.*?)\)")

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

# ==================================================================================================


def _preserve_whitelisted_entities(s: str) -> str:
    """Undo escaping for a few safe named entities often used in your data."""
    return (
        s.replace("&amp;check;", "&check;")
        .replace("&amp;nbsp;", "&nbsp;")
        .replace("&amp;times;", "&times;")
    )


# ==================================================================================================


def md_links_to_html(s: str) -> str:
    """Convert [text](url) to <a> while preserving whitelisted HTML entities in 'text'."""

    def _repl(m):
        text = html.escape(m.group(1), quote=True)
        text = _preserve_whitelisted_entities(text)  # allow &check; &nbsp; etc.
        url = html.escape(m.group(2), quote=True)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'

    return MD_LINK_RE.sub(_repl, s)


# ==================================================================================================


def parse_markdown(md_text: str):
    # Title
    m = TITLE_RE.search(md_text)
    title = m.group(1).strip() if m else "Benchmark"

    # Dataset link
    m = DATASET_LINK_RE.search(md_text)
    dataset_link = m.group(1).strip() if m else None

    # Task hierarchy
    m = TASK_HIER_RE.search(md_text)
    task_hierarchy = None
    if m:
        raw = m.group(1)
        try:
            task_hierarchy = json.loads(raw)
        except Exception:
            try:
                task_hierarchy = ast.literal_eval(raw)
            except Exception:
                task_hierarchy = None

    # JSON table block
    m = MD_JSON_BLOCK_RE.search(md_text)
    if not m:
        raise ValueError("Could not find ```json:table ...``` block in markdown.")
    table_spec = json.loads(m.group(1))

    return title, dataset_link, task_hierarchy, table_spec


# ==================================================================================================


def guess_field_type(field):
    """Return 'number', 'date', or 'string' for sorting/plotting."""
    key = field.get("key", "")
    label = field.get("label", "").lower()
    if key == "d" or "date" in label:
        return "date"
    if key.startswith("m"):  # common metric keys m1, m2, ...
        return "number"
    return "string"


# ==================================================================================================


def to_number(val):
    if val is None:
        return None
    s = str(val).strip().replace(",", "")
    if s.endswith("%"):
        s = s[:-1]
    try:
        return float(s)
    except ValueError:
        return None


# ==================================================================================================


def to_date_iso(val):
    """Return YYYY-MM-DD ISO string if parseable, else None."""
    if not val:
        return None
    try:
        v = str(val).strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
            dt = datetime.strptime(v, "%Y-%m-%d")
        elif re.fullmatch(r"\d{4}-\d{2}", v):
            dt = datetime.strptime(v + "-01", "%Y-%m-%d")
        elif re.fullmatch(r"\d{4}", v):
            dt = datetime.strptime(v + "-01-01", "%Y-%m-%d")
        else:
            # last resort; may still parse ISO-like strings
            dt = datetime.fromisoformat(v)
        return dt.date().isoformat()
    except Exception:
        return None


# ==================================================================================================


def render_html(title, dataset_link, task_hierarchy, table_spec, out_path):
    fields = table_spec.get("fields", [])
    items = table_spec.get("items", [])
    caption = table_spec.get("caption", "")

    # Field metadata
    columns = []
    for f in fields:
        ftype = guess_field_type(f)
        columns.append(
            {
                "key": f.get("key"),
                "label": f.get("label", f.get("key", "")).strip(),
                "sortable": str(f.get("sortable", "")).lower() == "true",
                "type": ftype,
            }
        )

    metric_keys = [c["key"] for c in columns if c["type"] == "number"]

    date_key = None
    for c in columns:
        if c["type"] == "date":
            date_key = c["key"]
            break

    # Build rows + chart series
    rows_html = []
    series_code = {mk: [] for mk in metric_keys}  # mk -> list of dicts with x,y,model

    for row in items:
        tds = []
        model_name = str(row.get("n", "")).strip()
        for col in columns:
            key = col["key"]
            raw = row.get(key, "")
            # Display
            if isinstance(raw, str):
                cell_html = md_links_to_html(raw)
                if cell_html == raw:  # no link converted
                    cell_html = html.escape(raw)
                cell_html = _preserve_whitelisted_entities(cell_html)
            elif raw is None:
                cell_html = ""
            else:
                cell_html = html.escape(str(raw))

            # Sorting data-value
            data_value = ""
            if col["type"] == "number":
                num = to_number(raw)
                data_value = "" if num is None else str(num)
            elif col["type"] == "date":
                iso = to_date_iso(raw)
                if iso:
                    try:
                        ts = int(datetime.strptime(iso, "%Y-%m-%d").timestamp() * 1000)
                        data_value = str(ts)
                    except Exception:
                        data_value = ""
                else:
                    data_value = ""

            attr = f' data-value="{data_value}"' if data_value else ""
            tds.append(f"<td{attr}>{cell_html}</td>")

        raw_code = row.get("c", "")
        has_code = bool(isinstance(raw_code, str) and "](" in raw_code)

        # Chart series
        if date_key:
            date_iso = to_date_iso(row.get(date_key))
            if date_iso:
                for mk in metric_keys:
                    y = to_number(row.get(mk))
                    if y is not None:
                        pt = {"x": date_iso, "y": y, "model": model_name or ""}
                        if has_code:
                            series_code[mk].append(pt)

        row_cls = "" if has_code else ' class="nocode"'
        rows_html.append(
            f"<tr data-hascode={'1' if has_code else '0'}{row_cls}>"
            + "".join(tds)
            + "</tr>"
        )

    # Sort each series by date
    for mk in metric_keys:
        series_code[mk].sort(key=lambda d: d["x"])

    # Map metric key -> label
    metric_labels = {c["key"]: c["label"] for c in columns}

    # Build Plotly traces (as JS)
    def build_traces(series_dict):
        out = []
        for mk in metric_keys:
            pts = series_dict[mk]
            if not pts:
                continue
            x_js = json.dumps([p["x"] for p in pts])
            y_js = json.dumps([p["y"] for p in pts])
            text_js = json.dumps([(p["model"] or "") for p in pts])
            name = metric_labels.get(mk, mk).replace('"', '\\"')
            out.append(
                f"""{{
                    name: "{name}",
                    x: {x_js},
                    y: {y_js},
                    text: {text_js},
                    mode: 'lines+markers',
                    type: 'scatter',
                    hovertemplate: '%{{y}}<extra>%{{text}}</extra>'
                }}"""
            )
        return ",\n".join(out)
    traces_js_code = build_traces(series_code)

    # Subtitle
    subtitle_html = ""
    if task_hierarchy:
        chips = "".join(
            f'<span class="chip">{html.escape(x)}</span>' for x in task_hierarchy
        )
        subtitle_html = f'<div class="chips">{chips}</div>'

    dataset_link_html = ""
    if dataset_link:
        dataset_link_html = f'<a class="dataset-link" href="{html.escape(dataset_link)}" target="_blank" rel="noopener noreferrer">Dataset Link</a>'

    caption_html = ""
    if caption:
        caption_html = md_links_to_html(caption)

    # Build columns (headers)
    thead_cells = []
    for col in columns:
        if col["sortable"]:
            thead_cells.append(
                f'<th data-key="{html.escape(col["key"])}" data-type="{col["type"]}" data-sortable="true">'
                f'{html.escape(col["label"])}'
                f'<span class="sort-indicator" aria-hidden="true">↕</span>'
                f"</th>"
            )
        else:
            thead_cells.append(
                f'<th data-key="{html.escape(col["key"])}" data-type="{col["type"]}" data-sortable="false">'
                f'{html.escape(col["label"])}'
                f"</th>"
            )

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>OpenCodePapers</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root {{
    --bg: #ffffff;
    --card: #ffffff;
    --text: #111827;
    --muted: #4b5563;
    --border: #e5e7eb;
    --accent: #2563eb;
    --grid: #f3f4f6;
  }}
  html,body {{
    background: var(--bg);
    color: var(--text);
    margin: 0;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
  }}
  .wrap {{ max-width: 1100px; margin: 32px auto; padding: 0 16px; }}
  h1 {{ font-size: 28px; margin: 0 0 8px; }}
  .header-row {{ display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between; }}
  .subtle {{ color: var(--muted); font-size: 14px; }}
  .dataset-link {{ color: var(--accent); text-decoration: none; font-weight: 600; }}
  .dataset-link:hover {{ text-decoration: underline; }}
  .chips {{ display:flex; flex-wrap:wrap; gap:6px; margin-top:4px; }}
  .chip {{ background:#f3f4f6; border:1px solid var(--border); color:#374151; padding:2px 8px; border-radius:999px; font-size:12px; }}
  .nocode {{ display: none; }}
  .btn {{ border:1px solid var(--border); background:white; color:var(--text); padding:6px 10px; border-radius:8px; font-size:13px; cursor:pointer; }}
  .btn:hover {{ background:#f9fafb; }}
  .card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 2px 10px rgba(17,24,39,0.04);
  }}
  .hero {{
    background: linear-gradient(135deg, #2563eb, #9333ea);
    color: white;
    text-align: center;
  }}
  .hero-inner {{
    max-width: 800px;
    margin: 0 auto;
  }}
  .hero-title {{
    font-size: 28px;
    margin: 0 0 6px;
    font-weight: 700;
  }}
  .hero-title a {{
    color: white;
    text-decoration: none;
  }}
  .hero-title a:hover {{
    text-decoration: underline;
  }}
  .hero-sub {{
    font-size: 15px;
    color: #e0e7ff;
    margin: 0;
  }}
  /* Smaller variant for benchmark pages */
  .hero-small {{
    padding: 20px 16px;   /* less height than index */
    margin-bottom: 20px;
  }}
  .section-title {{ margin: 4px 0 12px; font-size: 18px; color: #1f2937; }}
  table {{ width: 100%; border-collapse: collapse; }}
  thead th {{
    position: sticky;
    top: 0;
    background: #f9fafb;
    text-align: left;
    font-weight: 600;
    padding: 10px;
    border-bottom: 1px solid var(--border);
    cursor: default;
  }}
  thead th[data-sortable="true"] {{ cursor: pointer; }}
  th[data-key="c"], td:nth-child(2) {{
    min-width: 100px;
    white-space: nowrap;
    text-align: center;
  }}
  tbody td {{ padding: 10px; border-bottom: 1px solid var(--border); vertical-align: top; }}
  tbody tr:hover {{ background: #fbfdff; }}
  .sort-indicator {{ opacity: 0.45; margin-left: 6px; font-size: 12px; color: var(--muted); }}
  .legend-note {{ color: var(--muted); font-size: 12px; margin-top: 6px; }}
  a {{ color: #1d4ed8; }}
  .footer-note {{ color: var(--muted); margin-top: 12px; font-size: 13px; }}
  .stack {{ display: grid; gap: 14px; }}
  /* Plot container height */
  #metricPlot {{ width: 100%; height: 360px; }}
</style>
</head>
<body>
<section class="hero hero-small">
  <div class="hero-inner">
    <h1 class="hero-title">
      <a href="../index.html">OpenCodePapers</a>
    </h1>
  </div>
</section>
  <div class="wrap stack">
    <div class="header-row">
      <div>
        <h1>{html.escape(title)}</h1>
        {subtitle_html}
      </div>
      <div>{dataset_link_html}</div>
    </div>

    <div class="card">
      <span>Results over time</span>
      <div id="metricPlot"></div>
      <div class="legend-note">Click legend items to toggle metrics. Hover points for model names.</div>
    </div>

    <div class="card">
      <div class="section-title" style="display:flex;align-items:center;justify-content:space-between;gap:12px;">
        <span>Leaderboard</span>
        <button class="btn toggle-nocode">Show papers without code</button>
      </div>
      <div class="footer-note">Click a sortable column header to sort.</div>
      <div style="overflow-x:auto;">
        <table id="resultsTable">
          <thead>
            <tr>
              {''.join(thead_cells)}
            </tr>
          </thead>
          <tbody>
            {''.join(rows_html)}
          </tbody>
        </table>
      </div>
      {"<div class='footer-note' style='margin-top:10px;'>" + caption_html + "</div>" if caption_html else ""}
    </div>
  </div>

  <!-- Plotly (charting) -->
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
  <script>
    (function() {{
      // ===== Plot (Plotly) =====
      const tracesCode = [ {traces_js_code} ];
      const layout = {{
        paper_bgcolor: 'white',
        plot_bgcolor: 'white',
        font: {{ color: '#111827' }},
        margin: {{ l: 50, r: 20, t: 10, b: 40 }},
        xaxis: {{ type: 'date', gridcolor: '#e5e7eb', title: 'Date' }},
        yaxis: {{ gridcolor: '#e5e7eb', title: 'Metric value', automargin: true }},
        legend: {{ orientation: 'h', x: 0, y: 1.15 }}
      }};
      const cfg = {{ displayModeBar:false, responsive:true }};

      let showNoCode = false; // start hidden
      Plotly.newPlot('metricPlot', tracesCode, layout, cfg);

      const btns = document.querySelectorAll('.toggle-nocode');
      function applyNoCodeVisibility() {{
        // Table rows: force correct display for <tr>
        document.querySelectorAll('tr.nocode').forEach(tr => {{
          tr.style.display = showNoCode ? 'table-row' : 'none';
        }});

        // Plot
        Plotly.react('metricPlot', tracesCode, layout, cfg);

        // Sync all buttons' labels
        btns.forEach(b => {{
          b.textContent = showNoCode ? 'Hide papers without code' : 'Show papers without code';
        }});
      }}

      btns.forEach(b => {{
        b.addEventListener('click', () => {{
          showNoCode = !showNoCode;
          applyNoCodeVisibility();
        }});
      }});

      // Ensure initial state matches default (hidden)
      applyNoCodeVisibility();
    }})();
  </script>

  <script>
    // ===== Table sorting (lightweight) =====
    (function() {{
      const table = document.getElementById('resultsTable');
      const getCellValue = (tr, idx, type) => {{
        const td = tr.children[idx];
        if (!td) return '';
        if (type === 'number' || type === 'date') {{
          const v = td.getAttribute('data-value');
          if (v === null || v === '') return NaN;
          return Number(v);
        }}
        return (td.textContent || '').trim().toLowerCase();
      }};

      const compare = (a, b, type, asc) => {{
        let va = getCellValue(a, sortIdx, type);
        let vb = getCellValue(b, sortIdx, type);
        if (type === 'string') {{
          return (va > vb ? 1 : va < vb ? -1 : 0) * (asc ? 1 : -1);
        }} else {{
          if (isNaN(va) && isNaN(vb)) return 0;
          if (isNaN(va)) return 1;
          if (isNaN(vb)) return -1;
          return ((va - vb) * (asc ? 1 : -1));
        }}
      }};

      let sortIdx = -1;
      let sortAsc = true;

      table.querySelectorAll('thead th').forEach((th, idx) => {{
        if (th.getAttribute('data-sortable') !== 'true') return;
        th.addEventListener('click', () => {{
          const type = th.getAttribute('data-type') || 'string';
          if (sortIdx === idx) {{
            sortAsc = !sortAsc;
          }} else {{
            sortIdx = idx;
            sortAsc = (type === 'string'); // strings asc first, numbers/dates desc first
          }}
          const tbody = table.tBodies[0];
          Array.from(tbody.querySelectorAll('tr'))
            .sort((a, b) => compare(a, b, type, sortAsc))
            .forEach(tr => tbody.appendChild(tr));
        }});
      }});
    }})();
  </script>
</body>
</html>
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_doc)


# ==================================================================================================


def process_markdown_file(md_path: str, out_dir: str):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    title, dataset_link, task_hierarchy, table_spec = parse_markdown(md_text)

    base = os.path.splitext(os.path.basename(md_path))[0]
    out_path = os.path.join(out_dir, base + ".html")
    render_html(title, dataset_link, task_hierarchy, table_spec, out_path)
    return out_path


# ==================================================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Build HTML pages from benchmark Markdown files."
    )
    parser.add_argument("--input", "-i", default="dataset/benchmarks")
    parser.add_argument("--output", "-o", default="public/benchmarks")
    args = parser.parse_args()

    in_dir = os.path.abspath(args.input)
    out_dir = os.path.abspath(args.output) if args.output else in_dir

    if not os.path.isdir(in_dir):
        raise SystemExit(f"Input folder not found: {in_dir}")
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    made = []
    for name in os.listdir(in_dir):
        if not name.lower().endswith(".md"):
            continue
        md_path = os.path.join(in_dir, name)
        try:
            out_path = process_markdown_file(md_path, out_dir)
            made.append(out_path)
        except Exception as e:
            print(f" Skipped {md_path}: {e}")

    if not made:
        print("No HTML generated. ")


# ==================================================================================================

if __name__ == "__main__":
    main()
