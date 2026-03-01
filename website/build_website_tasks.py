import argparse
import html
import json
import os
import shutil

# ==================================================================================================


def json_to_html(data):
    """
    Convert the JSON hierarchy structure to nested HTML details/summary elements.
    data can be a dict with categories as keys, or a list of mixed strings and dicts.
    """
    if isinstance(data, dict):
        lines = []
        for category, content in data.items():
            lines.append(render_category(category, content))
        return "\n".join(lines)
    return ""


def render_category(category: str, content) -> str:
    """Render a single category with its nested content."""
    lines = []
    lines.append("<details>")
    lines.append(f"  <summary>{html.escape(category)}</summary>")
    lines.append("  <div>")

    if isinstance(content, list):
        # Separate strings (benchmarks) from dicts (nested categories)
        benchmarks = [item for item in content if isinstance(item, str)]
        subcategories = [item for item in content if isinstance(item, dict)]

        # Render nested categories first
        for item_dict in subcategories:
            for subcat, subcontent in item_dict.items():
                lines.append(render_category(subcat, subcontent))

        # Then render benchmarks as a list
        if benchmarks:
            lines.append("    <ul>")
            for benchmark in benchmarks:
                lines.append(
                    f'      <li><a href="benchmarks/{html.escape(benchmark)}.html"'
                    + ' target="_blank" rel="noopener noreferrer">'
                    + f"{html.escape(benchmark)}</a></li>"
                )
            lines.append("    </ul>")

    lines.append("  </div>")
    lines.append("</details>")
    return "\n".join(lines)


# ==================================================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Build a light-themed tasks landing page from tasks.json"
    )
    parser.add_argument("--input", "-i", default="dataset/tasks.json")
    parser.add_argument("--output", "-o", default="public/index.html")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        raise SystemExit(f"Not found: {args.input}")

    out_dir = os.path.dirname(os.path.abspath(args.output))
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(args.input, "r", encoding="utf-8") as f:
        tasks_data = json.load(f)

    # Convert JSON data to HTML
    html_tree = json_to_html(tasks_data)

    # Load template
    template_path = os.path.join(os.path.dirname(__file__), "tasks.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html_scaffold = f.read()

    html_full = html_scaffold.replace("<!--TREE-->", html_tree)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html_full)

    # Copy favicon to public/
    src_fav = os.path.join(os.path.abspath(os.path.dirname(__file__)), "favicon.svg")
    shutil.copy2(src_fav, os.path.join(out_dir, "favicon.svg"))

    print(f"[info] Generated {args.output}")


# ==================================================================================================

if __name__ == "__main__":
    main()
