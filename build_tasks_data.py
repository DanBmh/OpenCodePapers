import argparse
import json
import os
from typing import Dict, List

# ==================================================================================================


class Node:
    __slots__ = ("children", "benchmarks")

    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.benchmarks: List[str] = []


# ==================================================================================================


def add_path(root: Node, labels: List[str], title: str):
    node = root
    for label in labels:
        node = node.children.setdefault(label, Node())
    node.benchmarks.append(title)


# ==================================================================================================


def scan_json_files(input_dir: str) -> List[tuple]:
    """
    Returns list of (task_hierarchy, title) for each .json file.
    task_hierarchy is a list of strings, title is the benchmark name.
    """

    results: List[tuple] = []
    for root_dir, _, files in os.walk(input_dir):
        for fn in files:
            if not fn.lower().endswith(".json"):
                continue
            full = os.path.join(root_dir, fn)
            try:
                with open(full, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"[warn] Could not read {full}: {e}")
                continue

            task_hierarchy = data.get("task-hierarchy")
            title = data.get("title")

            if title:
                if task_hierarchy and isinstance(task_hierarchy, list):
                    results.append((task_hierarchy, title))
                else:
                    # No hierarchy or empty -> use None
                    results.append((None, title))
    return results


# ==================================================================================================


def ensure_child(node: Node, label: str) -> Node:
    return node.children.setdefault(label, Node())


# ==================================================================================================


def process_small_leaves(node: Node, parent: Node = None):
    """
    Bottom-up normalization:
    - Move small leaf buckets (<3 benchmarks) into 'others' at this node.
    - Flatten 'others' children to a single benchmark list.
    - Bubble 'others' upward if still <3 (and not at root).
    - If THIS node already has benchmarks and also an 'others' child, MERGE
      'others' benchmarks into THIS node's benchmarks and remove the 'others' child.
    """

    # Recurse first
    for label, child in list(node.children.items()):
        process_small_leaves(child, node)

    # Move small leaf buckets into 'others'
    to_delete = []
    for label, child in list(node.children.items()):
        if child.benchmarks and not child.children:
            if 0 < len(child.benchmarks) < 3:
                others = ensure_child(node, "others")
                others.benchmarks.extend(child.benchmarks)
                to_delete.append(label)
    for label in to_delete:
        del node.children[label]

    # Flatten 'others'
    others = node.children.get("others")
    if others:
        if others.children:
            stack = [others]
            collected: List[str] = []
            while stack:
                cur = stack.pop()
                collected.extend(cur.benchmarks)
                for ch in cur.children.values():
                    stack.append(ch)
            others.children.clear()
            others.benchmarks = collected

        # If this node already has benchmarks, merge 'others' into the node's list
        if node.benchmarks and others.benchmarks:
            node.benchmarks.extend(others.benchmarks)
            del node.children["others"]
            others = None

    # Bubble 'others' upward if still present and <3 (and not root)
    others = node.children.get("others")
    if others and len(others.benchmarks) < 3 and parent is not None:
        p_others = ensure_child(parent, "others")
        p_others.benchmarks.extend(others.benchmarks)
        del node.children["others"]


# ==================================================================================================


def prune_empty(node: Node) -> bool:
    """
    Remove empty child groups recursively.
    Returns True if this node has any content (benchmarks or non-empty children).
    """

    empty_labels = []
    for label, child in node.children.items():
        if not prune_empty(child):
            empty_labels.append(label)
    for label in empty_labels:
        del node.children[label]
    return bool(node.benchmarks or node.children)


# ==================================================================================================


def node_to_dict(node: Node) -> List:
    """
    Convert a Node tree to a mixed list structure.
    Returns [benchmark_string, benchmark_string, {subcategory_name: [...]}, ...]
    """

    result = []

    # Add subcategories as dicts
    if node.children:

        def sort_key(lbl: str):
            return (lbl == "others", lbl.lower())

        for label in sorted(node.children.keys(), key=sort_key):
            child = node.children[label]
            if child.benchmarks or child.children:  # Skip empty (safety)
                result.append({label: node_to_dict(child)})

    # Add benchmarks
    if node.benchmarks:
        result.extend(sorted(node.benchmarks))

    return result


# ==================================================================================================


def build_tasks_json(input_dir: str, output_path: str):
    entries = scan_json_files(input_dir)
    if not entries:
        print("[info] No JSON entries found. Writing empty structure.")
        output_data = {}
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        return

    root = Node()
    for hierarchy, title in entries:
        if hierarchy:
            add_path(root, hierarchy, title)
        else:
            # No/empty hierarchy -> top-level 'others'
            ensure_child(root, "others").benchmarks.append(title)

    process_small_leaves(root, None)
    prune_empty(root)

    # Convert tree to dictionary
    output_data = {}

    def sort_key(lbl: str):
        return (lbl == "others", lbl.lower())

    for label in sorted(root.children.keys(), key=sort_key):
        child = root.children[label]
        if child.benchmarks or child.children:
            output_data[label] = node_to_dict(child)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"[info] Written {len(entries)} benchmarks to {output_path}")


# ==================================================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Generate a tasks hierarchy JSON from benchmark JSON files."
    )
    parser.add_argument("--input", "-i", default="dataset/benchmarks")
    parser.add_argument("--output", "-o", default="dataset/tasks.json")
    args = parser.parse_args()

    input_dir = args.input.rstrip("/").rstrip("\\")
    build_tasks_json(input_dir, args.output)


# ==================================================================================================

if __name__ == "__main__":
    main()
