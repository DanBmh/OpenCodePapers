import ast
import json
import re
import sys
from pathlib import Path

# ==================================================================================================


def check_title_equals_filename(text: str, path: Path):

    TITLE_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
    m = TITLE_RE.search(text)

    if not m:
        return [f"{path}: Missing H1 title line starting with '# '."]

    title = m.group(1).strip()
    expected = path.stem
    if title != expected:
        return [
            (
                f"{path}: Title must equal filename without extension.\n"
                f"  found title:    {title!r}\n"
                f"  expected title: {expected!r}"
            )
        ]

    return []


# ==================================================================================================


def check_dataset_link(text: str, path: Path):

    DATASET_LINK_RE = re.compile(
        r"^\s*\[Dataset\s+Link\]\((https?://[^)]+)\)\s*\\\s*$",
        re.MULTILINE,
    )
    m = DATASET_LINK_RE.search(text)

    if not m:
        return [f"{path}: Missing dataset link"]

    return []


# ==================================================================================================


def check_task_hierarchy(text: str, path: Path):

    TASK_RE = re.compile(r"(?im)^Task\s*Hierarchy:\s*(.+)$")
    m = TASK_RE.search(text)

    if not m:
        return [f"{path}: Missing 'Task Hierarchy: [...]' line."]

    list_text = m.group(1).strip()
    try:
        task_list = ast.literal_eval(list_text)
    except Exception as e:
        return [
            f"{path}: Task Hierarchy is not a valid list literal. Got {list_text!r}. Error: {e}"
        ]

    if not isinstance(task_list, list):
        return [
            f"{path}: Task Hierarchy must be a list, got {type(task_list).__name__}."
        ]

    # Enforce list elements be strings (empty list ok)
    if not all(isinstance(x, str) for x in task_list):
        return [f"{path}: All Task Hierarchy entries must be strings."]

    return []


# ==================================================================================================


def check_json_table_blocks(text: str, path: Path):

    JSON_TABLE_RE = re.compile(r"```json:table\s*([\s\S]*?)```", re.MULTILINE)
    matches = list(JSON_TABLE_RE.finditer(text))

    errors = []
    if not matches:
        errors.append(f"{path}: Missing fenced code block starting with ```json:table.")
        return errors

    for i, m in enumerate(matches, start=1):
        block = m.group(1)
        try:
            parsed = json.loads(block)
        except json.JSONDecodeError as e:
            base_line = text[: m.start(1)].count("\n") + 1
            abs_line = base_line + e.lineno - 1
            errors.append(
                f"{path}: Invalid JSON in ```json:table``` block #{i} "
                f"(line {abs_line}, col {e.colno}) — {e.msg}"
            )
            continue

        if not isinstance(parsed, dict):
            errors.append(
                f"{path}: ```json:table``` block #{i} must be a JSON object at the top level."
            )

    return errors


# ==================================================================================================


def main() -> int:

    MARKDOWN_DIR = "dataset/benchmarks/"

    root = Path(MARKDOWN_DIR).resolve()
    if not root.exists() or not root.is_dir():
        print(
            f"ERROR: MARKDOWN_DIR does not exist or is not a directory: {root}",
            file=sys.stderr,
        )
        return 2

    # check that all items in the directory are markdown files
    for item in root.iterdir():
        if item.is_file() and item.suffix != ".md":
            print(f"ERROR: Non-markdown file found in {root}: {item}", file=sys.stderr)
            return 1

    md_files = [p for p in root.rglob("*.md") if p.is_file()]
    if not md_files:
        print(f"No markdown files found under {root}")
        return 0

    all_errors = []
    for path in sorted(md_files):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            all_errors.append(f"{path}: Failed to read file as UTF-8: {e}")
            continue

        all_errors.extend(check_title_equals_filename(text, path))
        # all_errors.extend(check_dataset_link(text, path))
        all_errors.extend(check_task_hierarchy(text, path))
        all_errors.extend(check_json_table_blocks(text, path))

    if all_errors:
        print("Validation failed with the following issues:\n")
        for err in all_errors:
            print(f"- {err}")
        print(f"\nTotal files checked: {len(md_files)} | Errors: {len(all_errors)}")
        return 1

    print(f"All checks passed. Total markdown files checked: {len(md_files)}")
    return 0


# ==================================================================================================


if __name__ == "__main__":
    sys.exit(main())
