import html
import json
import os
import re

# ==================================================================================================

benchmark_dir = "dataset/benchmarks/"
badges_dir = "public/badges/"
template_path = "extras/badges/badge.svg.template"

# ==================================================================================================


def sanitize_filename(value: str) -> str:
    """Convert a string into a safe filename."""
    value = value.replace("/", "--")
    value = re.sub(r"[^A-Za-z0-9]", "-", value)
    value = value.lower().strip("-")
    return value


# ==================================================================================================


def render_badge(template: str, title: str, rank: int) -> str:
    template = template.replace("{{title}}", html.escape(title))
    template = template.replace("{{rank}}", html.escape(str(rank)))

    # Remove comments and extra whitespace
    template = re.sub(r"<!--.*?-->", "", template, flags=re.DOTALL)
    template = re.sub(r"\s+", " ", template)
    template = template.strip()

    return template


# ==================================================================================================


def generate_badges() -> None:
    if not os.path.exists(badges_dir):
        os.makedirs(badges_dir)

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    for benchmark_file in sorted(os.listdir(benchmark_dir)):
        if not benchmark_file.endswith(".json"):
            continue

        bpath = os.path.join(benchmark_dir, benchmark_file)
        with open(bpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        benchmark_title = str(data.get("title"))
        benchmark_output_dir = os.path.join(badges_dir, benchmark_title)
        os.makedirs(benchmark_output_dir, exist_ok=True)

        items = data.get("benchmark", {}).get("items", [])
        if not isinstance(items, list):
            continue

        rank = 0
        for i, item in enumerate(items, start=1):
            if not isinstance(item, dict):
                continue

            code_link = str(item.get("c", "")).strip()
            if not code_link:
                continue

            # Only count results with code links for ranking, ignore closed-source methods
            rank += 1

            code_link = code_link.replace("https://", "").replace("http://", "")
            code_link = code_link.rstrip("/").rstrip(".git")
            code_link = code_link[:50]

            method_name = str(item.get("n", "")).strip() or f"method-{i}"
            method_name = method_name[:50]

            filename = f"{code_link}---{method_name}"
            filename = sanitize_filename(filename)
            filename += ".svg"

            title = f"OpenCodePapers | {rank} | {benchmark_title}"
            badge_svg = render_badge(template=template, title=title, rank=rank)

            bpath = os.path.join(benchmark_output_dir, filename)
            with open(bpath, "w+", encoding="utf-8") as f:
                f.write(badge_svg)


# ==================================================================================================


if __name__ == "__main__":
    generate_badges()
