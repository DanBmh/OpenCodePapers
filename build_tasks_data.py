import argparse
import ast
import os
import re
from typing import Dict, List, Optional, Tuple

# ==================================================================================================


HIERARCHY_PATTERN = re.compile(
    r"^\s*Task\s*Hierarchy\s*:\s*(\[[^\]]*\])", re.IGNORECASE | re.MULTILINE
)

# ==================================================================================================


class Node:
    __slots__ = ("children", "files")

    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.files: List[Tuple[str, str]] = []  # (display_text, link_path)


# ==================================================================================================


def add_path(root: Node, labels: List[str], file_entry: Tuple[str, str]):
    node = root
    for label in labels:
        node = node.children.setdefault(label, Node())
    node.files.append(file_entry)


# ==================================================================================================


def parse_hierarchy(md_text: str) -> Optional[List[str]]:
    m = HIERARCHY_PATTERN.search(md_text)
    if not m:
        return None
    try:
        parsed = ast.literal_eval(m.group(1))
        labels = [str(x).strip() for x in parsed if str(x).strip()]
        return labels if labels else None
    except Exception:
        return None


# ==================================================================================================


def scan_markdowns(input_dir: str) -> List[Tuple[Optional[List[str]], str, str]]:
    """
    Returns list of (labels or None, link_text, link_path) for each .md.
    If labels is None, hierarchy missing/empty -> top-level 'others'.
    """

    results: List[Tuple[Optional[List[str]], str, str]] = []
    for root_dir, _, files in os.walk(input_dir):
        for fn in files:
            if not fn.lower().endswith(".md"):
                continue
            full = os.path.join(root_dir, fn)
            try:
                with open(full, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception:
                print(f"[warn] Could not read: {full}")
                continue

            labels = parse_hierarchy(text)

            slug = os.path.splitext(os.path.basename(full))[0]
            rel_path = os.path.relpath(full, os.getcwd()).replace("\\", "/")
            if not rel_path.startswith(input_dir.rstrip("/")):
                rel_path = f"{input_dir.rstrip('/')}/{os.path.basename(full)}"

            results.append((labels, slug, rel_path))
    return results


# ==================================================================================================


def ensure_child(node: Node, label: str) -> Node:
    return node.children.setdefault(label, Node())


# ==================================================================================================


def process_small_leaves(node: Node, parent: Optional[Node] = None):
    """
    Bottom-up normalization:
    - Move small leaf buckets (<3 files) into 'others' at this node.
    - Flatten 'others' children to a single file list.
    - Bubble 'others' upward if still <3 (and not at root).
    - If THIS node already has files and also an 'others' child, MERGE
      'others' files into THIS node's files and remove the 'others' child.
    """

    # Recurse first
    for label, child in list(node.children.items()):
        process_small_leaves(child, node)

    # Move small leaf buckets into 'others'
    to_delete = []
    for label, child in list(node.children.items()):
        if child.files and not child.children:
            if 0 < len(child.files) < 3:
                others = ensure_child(node, "others")
                others.files.extend(child.files)
                to_delete.append(label)
    for label in to_delete:
        del node.children[label]

    # Flatten 'others'
    others = node.children.get("others")
    if others:
        if others.children:
            stack = [others]
            collected: List[Tuple[str, str]] = []
            while stack:
                cur = stack.pop()
                collected.extend(cur.files)
                for ch in cur.children.values():
                    stack.append(ch)
            others.children.clear()
            others.files = collected

        # If this node already has files, merge 'others' into the parent link list
        if node.files and others.files:
            node.files.extend(others.files)
            del node.children["others"]
            others = None  # dropped

    # Bubble 'others' upward if still present and <3 (and not root)
    others = node.children.get("others")
    if others and len(others.files) < 3 and parent is not None:
        p_others = ensure_child(parent, "others")
        p_others.files.extend(others.files)
        del node.children["others"]


# ==================================================================================================


def prune_empty(node: Node) -> bool:
    """
    Remove empty child groups recursively.
    Returns True if this node has any content (files or non-empty children).
    """

    empty_labels = []
    for label, child in node.children.items():
        if not prune_empty(child):
            empty_labels.append(label)
    for label in empty_labels:
        del node.children[label]
    return bool(node.files or node.children)


# ==================================================================================================


def escape_attr(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# ==================================================================================================


def render_html(node: Node) -> str:
    """
    Pure-HTML rendering:
      <details>
        <summary>Label</summary>
        <div>
          ... nested <details> for subgroups first ...
          <ul> ... files ... </ul>
        </div>
      </details>
    Only non-empty children are rendered (after pruning).
    """
    lines: List[str] = []

    def sort_key(lbl: str):
        return (lbl == "others", lbl.lower())

    for label in sorted(node.children.keys(), key=sort_key):
        child = node.children[label]
        # Skip empty children (safety; prune_empty should have removed them already)
        if not (child.files or child.children):
            continue

        lines.append("<details>")
        lines.append(f"  <summary>{escape_attr(label)}</summary>")
        lines.append("  <div>")

        # 1) Subgroups first
        if child.children:
            lines.append(render_html(child))

        # 2) Then files for this group
        if child.files:
            lines.append("    <ul>")
            for text, link in sorted(child.files, key=lambda x: x[0].lower()):
                lines.append(
                    f'      <li><a href="{escape_attr(link)}">{escape_attr(text)}</a></li>'
                )
            lines.append("    </ul>")

        lines.append("  </div>")
        lines.append("</details>")
    return "\n".join(lines)


# ==================================================================================================


def build_tasks_md(input_dir: str, output_path: str):
    entries = scan_markdowns(input_dir)
    if not entries:
        print("[info] No entries found. Nothing to write.")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("<h1>Tasks</h1>\n<p><em>No benchmarks found.</em></p>\n")
        return

    root = Node()
    for labels, slug, relpath in entries:
        if labels:
            add_path(root, labels, (slug, relpath))
        else:
            # No/empty hierarchy → top-level 'others'
            ensure_child(root, "others").files.append((slug, relpath))

    process_small_leaves(root, None)
    prune_empty(root)

    html = []
    html.append("<h1>Tasks</h1>")
    html.append(
        "<!-- Expandable, nested task hierarchy. Click to expand categories. -->"
    )
    html.append(render_html(root))
    html_text = "\n".join(html).rstrip() + "\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_text)


# ==================================================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Generate an expandable tasks.md from benchmark markdown files."
    )
    parser.add_argument("--input", "-i", default="dataset/benchmarks")
    parser.add_argument("--output", "-o", default="dataset/tasks.md")
    args = parser.parse_args()

    input_dir = args.input.rstrip("/").rstrip("\\")
    build_tasks_md(input_dir, args.output)


# ==================================================================================================

if __name__ == "__main__":
    main()
