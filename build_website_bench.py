import argparse
import html
import json
import os
import re
from datetime import datetime

# ==================================================================================================


def parse_json(json_path: str):
    """Load benchmark data from JSON file."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    title = data.get("title", "Benchmark")
    task_hierarchy = data.get("task-hierarchy", [])
    dataset_info = data.get("dataset-info", {})
    dataset_link = dataset_info.get("link")
    benchmark = data.get("benchmark", {})
    table_spec = {
        "fields": benchmark.get("fields", []),
        "items": benchmark.get("items", []),
    }

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
                # Special handling for code links ("c" field)
                if key == "c" and raw.strip():
                    url = html.escape(raw, quote=True)
                    cell_html = f'<a href="{url}" target="_blank" rel="noopener noreferrer">&check;&nbsp;Link</a>'
                else:
                    cell_html = html.escape(raw)
            elif isinstance(raw, dict):
                # Handle paper link dict {"name": "...", "link": "..."}
                if key == "p" and "name" in raw and "link" in raw:
                    name = html.escape(raw["name"])
                    link = html.escape(raw["link"], quote=True)
                    cell_html = f'<a href="{link}" target="_blank" rel="noopener noreferrer">{name}</a>'
                else:
                    cell_html = html.escape(str(raw))
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
        has_code = bool(isinstance(raw_code, str) and raw_code.strip())

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
        for i in range(len(series_code[mk])):
            series_code[mk][i]["idx"] = i
        series_code[mk].sort(key=lambda d: d["x"])

    # Map metric key -> label
    metric_labels = {c["key"]: c["label"] for c in columns}

    # Build Plotly traces (as JS)
    def build_traces(series_dict):
        out = []
        for metric_index, mk in enumerate(metric_keys):
            pts = series_dict[mk]
            if not pts:
                continue

            xs = [p["x"] for p in pts]
            ys = [p["y"] for p in pts]
            texts = [(p["model"] or "") for p in pts]
            name = metric_labels.get(mk, mk).replace('"', '\\"')
            marker_sizes = [6] * len(pts)
            marker_symbols = ["circle"] * len(pts)

            # Highlight best point of the first metric
            best_idx = None
            if metric_index == 0:
                best_idx = min(enumerate(pts), key=lambda x: x[1]["idx"])[0]
            if best_idx is not None:
                marker_sizes[best_idx] = 18
                marker_symbols[best_idx] = "star"

            x_js = json.dumps(xs)
            y_js = json.dumps(ys)
            text_js = json.dumps(texts)
            size_js = json.dumps(marker_sizes)
            symbol_js = json.dumps(marker_symbols)

            out.append(f"""{{
                    name: "{name}",
                    x: {x_js},
                    y: {y_js},
                    text: {text_js},
                    mode: 'lines+markers',
                    type: 'scatter',
                    marker: {{
                        size: {size_js},
                        symbol: {symbol_js}
                    }},
                    hovertemplate: '%{{y}}<extra>%{{text}}</extra>'
                }}""")
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

    # Add caption to contribution page
    caption_html = ""
    cont = 'Check out how to <a href="https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener noreferrer">contribute</a>  new results.'
    caption_html += cont

    # Add link to file source (JSON version)
    note = ' Then edit <a href="https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/dataset/benchmarks/{}?plain=0" target="_blank" rel="noopener noreferrer">this</a> file.'
    note = note.format(os.path.basename(out_path).replace("html", "json"))
    caption_html += note

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
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
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

  <!-- Plotly chart -->
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
  <script>
    (function() {{
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

      // Hide all but the first metric initially
      tracesCode.forEach((trace, idx) => {{
        if (idx > 0) {{
          trace.visible = 'legendonly';
        }}
      }});

      // Create the plot
      Plotly.newPlot('metricPlot', tracesCode, layout, cfg);
    }})();
  </script>

  <!-- No code visibility toggle -->
  <script>
    let showNoCode = false; // start hidden
    const btns = document.querySelectorAll('.toggle-nocode');

    function applyNoCodeVisibility() {{
      // Table rows: force correct display for <tr>
      document.querySelectorAll('tr.nocode').forEach(tr => {{
        tr.style.display = showNoCode ? 'table-row' : 'none';
      }});

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
  </script>

  <!-- Table sorting -->
  <script>
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


def process_json_file(json_path: str, out_dir: str):
    title, dataset_link, task_hierarchy, table_spec = parse_json(json_path)

    base = os.path.splitext(os.path.basename(json_path))[0]
    out_path = os.path.join(out_dir, base + ".html")
    render_html(title, dataset_link, task_hierarchy, table_spec, out_path)
    return out_path


# ==================================================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Build HTML pages from benchmark JSON files."
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
        if not name.lower().endswith(".json"):
            continue
        json_path = os.path.join(in_dir, name)
        try:
            out_path = process_json_file(json_path, out_dir)
            made.append(out_path)
        except Exception as e:
            print(f" Skipped {json_path}: {e}")

    if not made:
        print("No HTML generated. ")


# ==================================================================================================

if __name__ == "__main__":
    main()
