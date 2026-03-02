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
    tbody_cells = []
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
                    cell_html = (
                        f'<a href="{url}" target="_blank"'
                        + ' rel="noopener noreferrer">&check;&nbsp;Link</a>'
                    )
                else:
                    cell_html = html.escape(raw)
            elif isinstance(raw, dict):
                # Handle paper link dict {"name": "...", "link": "..."}
                if key == "p" and "name" in raw and "link" in raw:
                    name = html.escape(raw["name"])
                    link = html.escape(raw["link"], quote=True)
                    cell_html = (
                        f'<a href="{link}" target="_blank"'
                        + f' rel="noopener noreferrer">{name}</a>'
                    )
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
        tbody_cells.append(
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
        dataset_link_html = (
            f'<a class="dataset-link" href="{html.escape(dataset_link)}"'
            + ' target="_blank" rel="noopener noreferrer">Dataset Link</a>'
        )

    # Add caption to contribution page
    caption_html = ""
    cont = (
        "Check out how to <a href="
        + '"https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md"'
        + ' target="_blank" rel="noopener noreferrer">contribute</a>  new results.'
    )
    caption_html += cont

    # Add link to file source (JSON version)
    note = (
        " Then edit <a href="
        + '"https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/dataset/benchmarks/{}"'
        + ' target="_blank" rel="noopener noreferrer">this</a> file.'
    )
    note = note.format(os.path.basename(out_path).replace("html", "json"))
    caption_html += note

    # Build columns (headers)
    thead_cells = []
    for col in columns:
        if col["sortable"]:
            thead_cells.append(
                f'<th data-key="{html.escape(col["key"])}"'
                + f'data-type="{col["type"]}" data-sortable="true">'
                f'{html.escape(col["label"])}'
                f'<span class="sort-indicator" aria-hidden="true">↕</span>'
                f"</th>"
            )
        else:
            thead_cells.append(
                f'<th data-key="{html.escape(col["key"])}"'
                + f'data-type="{col["type"]}" data-sortable="false">'
                f'{html.escape(col["label"])}'
                f"</th>"
            )

    hpath = os.path.join(os.path.dirname(__file__), "benchmark.html")
    with open(hpath, "r", encoding="utf-8") as f:
        html_doc = f.read()

    html_doc = html_doc.replace("<!--[title]-->", title)
    html_doc = html_doc.replace("<!--[subtitle]-->", subtitle_html)
    html_doc = html_doc.replace("<!--[datasetlink]-->", dataset_link_html)
    html_doc = html_doc.replace("<!--[traces_code]-->", traces_js_code)
    html_doc = html_doc.replace("<!--[theadcells]-->", "".join(thead_cells))
    html_doc = html_doc.replace("<!--[tbodycells]-->", "".join(tbody_cells))
    html_doc = html_doc.replace("<!--[caption]-->", caption_html)

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
