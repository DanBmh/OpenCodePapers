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


def check_template_layout(text: str, path: Path):
    errors = []

    # Normalize newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")

    # File must end with exactly one trailing blank line.
    if len(lines) < 2 or lines[-1] != "" or lines[-2] == "":
        errors.append(f"{path}: File must end with exactly one blank line.")
        return errors
    lines = lines[:-1]

    # Title lines
    if not lines[0].startswith("# "):
        errors.append(f"{path}: First line must be a title.")
        return errors
    if lines[1].strip() != "":
        errors.append(f"{path}: Second line must be blank.")
        return errors

    # Dataset and Hierarchy lines
    if not lines[2].startswith("[Dataset Link](") or not lines[2].endswith("\\"):
        errors.append(f"{path}: Dataset link line invalid.")
        return errors
    if not lines[3].startswith("Task Hierarchy:"):
        errors.append(f"{path}: Hierarchy line invalid.")
        return errors
    if lines[4].strip() != "":
        errors.append(f"{path}: Fifth line must be blank.")
        return errors

    # Any further text lines before the table block are allowed
    curr_idx = 5
    while curr_idx < len(lines):
        if lines[curr_idx].startswith("```json:table"):
            break
        curr_idx += 1

    # Check blanks before table block
    if lines[curr_idx - 3].strip() != "":
        errors.append(f"{path}: Line {curr_idx-3} must be blank.")
        return errors
    if lines[curr_idx - 2].strip() != "<br>":
        errors.append(f"{path}: Line {curr_idx-2} must be '<br>'.")
        return errors
    if lines[curr_idx - 1].strip() != "":
        errors.append(f"{path}: Line {curr_idx-1} must be blank.")
        return errors

    # Check table block start index
    if not lines[curr_idx].startswith("```json:table"):
        errors.append(f"{path}: Table block missing or misplaced.")
        return errors

    # Check table block finishes correctly
    curr_idx += 1
    while curr_idx < len(lines):
        if lines[curr_idx].startswith("```"):
            break
        curr_idx += 1
    if curr_idx == len(lines) or not lines[curr_idx].startswith("```"):
        errors.append(f"{path}: Table block missing closing fence.")
        return errors
    if curr_idx != len(lines) - 1:
        errors.append(f"{path}: No content allowed after table block.")
        return errors

    return errors


# ==================================================================================================


def check_malicious_injections(text: str, path: Path):

    MALICIOUS_PATTERNS = [
        (re.compile(r"(?is)<\s*script\b"), "HTML <script> tag"),
        (re.compile(r"(?is)<\s*/\s*script\s*>"), "HTML </script> tag"),
        (re.compile(r"(?is)<\s*iframe\b"), "HTML <iframe> tag"),
        (re.compile(r"(?is)<\s*object\b"), "HTML <object> tag"),
        (re.compile(r"(?is)<\s*embed\b"), "HTML <embed> tag"),
        (
            re.compile(r"(?is)<\s*link\b[^>]*\brel\s*=\s*['\"]?\s*import\b"),
            "HTML import via <link rel=import>",
        ),
        (
            re.compile(r"(?is)<\s*meta\b[^>]*\bhttp-equiv\s*=\s*['\"]?\s*refresh\b"),
            "Meta refresh redirect",
        ),
        (
            re.compile(r"(?is)\bon\w+\s*="),
            "Inline event handler attribute (e.g. onclick=)",
        ),
        (re.compile(r"(?is)\bjavascript\s*:"), "javascript: URL"),
        (re.compile(r"(?is)\bdata\s*:\s*text\s*/\s*html\b"), "data:text/html URL"),
        (re.compile(r"(?is)\bvbscript\s*:"), "vbscript: URL"),
    ]

    errors = []
    for rx, label in MALICIOUS_PATTERNS:
        for m in rx.finditer(text):
            idx = m.start()
            line = text.count("\n", 0, idx) + 1
            last_nl = text.rfind("\n", 0, idx)
            col = (idx - last_nl) if last_nl != -1 else (idx + 1)

            snippet = text[idx : min(len(text), idx + 80)].replace("\n", "\\n")
            errors.append(
                f"{path}: Potential malicious content detected: {label} "
                f"(line {line}, col {col}). Near: {snippet!r}"
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
        all_errors.extend(check_template_layout(text, path))
        all_errors.extend(check_malicious_injections(text, path))

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
