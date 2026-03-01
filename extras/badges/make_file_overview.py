import os
from typing import List

# ==================================================================================================

badges_dir = "public/badges/"
template_path = "extras/badges/template.html"
out_file = os.path.join(badges_dir, "index.html")

# ==================================================================================================


def list_badges(base: str) -> List[tuple]:
    """Return a list of (folder, [files]) under base."""
    entries = []
    if not os.path.isdir(base):
        return entries

    for name in sorted(os.listdir(base)):
        path = os.path.join(base, name)
        if os.path.isdir(path):
            files = [f for f in sorted(os.listdir(path)) if f.lower().endswith(".svg")]
            entries.append((name, files))
    return entries


# ==================================================================================================


def render_overview(entries: List[tuple]) -> str:

    body = []
    if not entries:
        body.append("<p class='muted'>No badges found in public/badges.</p>")
    else:
        for folder, files in entries:
            body.append(f"<div class=folder>{folder}</div>")
            body.append("<ul>")
            for fn in files:
                fn = fn.replace(".svg", "")
                body.append(f"<li>{fn}</li>")
            body.append("</ul>")

    return "\n".join(body)


# ==================================================================================================


def main():
    os.makedirs(badges_dir, exist_ok=True)
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    entries = list_badges(badges_dir)
    content = render_overview(entries)
    html_doc = template.replace("{{content}}", content)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"Wrote {out_file} (folders: {len(entries)})")


# ==================================================================================================

if __name__ == "__main__":
    main()
