import json
import re
import sys
from pathlib import Path

# ==================================================================================================


def check_title_equals_filename(data: dict, path: Path):

    title = data.get("title")
    if not title:
        return [f"{path}: Missing 'title' key in JSON."]

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


def check_dataset_link(data: dict, path: Path):

    dataset_info = data.get("dataset-info")
    if not dataset_info:
        return [f"{path}: Missing 'dataset-info' key in JSON."]

    if "link" not in dataset_info:
        return [f"{path}: Missing 'dataset-info.link' key in JSON."]
    if not isinstance(dataset_info["link"], str):
        return [
            f"{path}: 'dataset-info.link' must be a string, got {type(dataset_info['link']).__name__}."
        ]

    return []


# ==================================================================================================


def check_task_hierarchy(data: dict, path: Path):

    task_hierarchy = data.get("task-hierarchy")
    if not task_hierarchy:
        return [f"{path}: Missing 'task-hierarchy' key in JSON."]

    if not isinstance(task_hierarchy, list):
        return [
            f"{path}: Task Hierarchy must be a list, got {type(task_hierarchy).__name__}."
        ]

    # Enforce list elements be strings (empty list ok)
    if not all(isinstance(x, str) for x in task_hierarchy):
        return [f"{path}: All Task Hierarchy entries must be strings."]

    return []


# ==================================================================================================


def check_benchmark_structure(data: dict, path: Path):

    errors = []

    benchmark = data.get("benchmark")
    if not benchmark:
        errors.append(f"{path}: Missing 'benchmark' key in JSON.")
        return errors

    if not isinstance(benchmark, dict):
        errors.append(
            f"{path}: 'benchmark' must be a JSON object, got {type(benchmark).__name__}."
        )
        return errors

    # Check for required fields
    if "fields" not in benchmark:
        errors.append(f"{path}: Missing 'benchmark.fields' key.")
    elif not isinstance(benchmark["fields"], list):
        errors.append(f"{path}: 'benchmark.fields' must be a list.")

    if "items" not in benchmark:
        errors.append(f"{path}: Missing 'benchmark.items' key.")
    elif not isinstance(benchmark["items"], list):
        errors.append(f"{path}: 'benchmark.items' must be a list.")

    return errors


# ==================================================================================================


def check_malicious_injections(data: dict, path: Path):

    # Convert data dict to string for scanning
    text = json.dumps(data)

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

    JSON_DIR = "../dataset/benchmarks/"

    root = Path(JSON_DIR).resolve()
    if not root.exists() or not root.is_dir():
        print(
            f"ERROR: JSON_DIR does not exist or is not a directory: {root}",
            file=sys.stderr,
        )
        return 2

    # check that all items in the directory are json files
    for item in root.iterdir():
        if item.is_file() and item.suffix != ".json":
            print(f"ERROR: Non-JSON file found in {root}: {item}", file=sys.stderr)
            return 1

    json_files = [p for p in root.rglob("*.json") if p.is_file()]
    if not json_files:
        print(f"No JSON files found under {root}")
        return 0

    all_errors = []
    for path in sorted(json_files):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            all_errors.append(f"{path}: Failed to parse JSON: {e}")
            continue
        except Exception as e:
            all_errors.append(f"{path}: Failed to read file as UTF-8: {e}")
            continue

        all_errors.extend(check_title_equals_filename(data, path))
        all_errors.extend(check_dataset_link(data, path))
        all_errors.extend(check_task_hierarchy(data, path))
        all_errors.extend(check_benchmark_structure(data, path))
        all_errors.extend(check_malicious_injections(data, path))

    if all_errors:
        print("Validation failed with the following issues:\n")
        for err in all_errors:
            print(f"- {err}")
        print(f"\nTotal files checked: {len(json_files)} | Errors: {len(all_errors)}")
        return 1

    print(f"All checks passed. Total JSON files checked: {len(json_files)}")
    return 0


# ==================================================================================================


if __name__ == "__main__":
    sys.exit(main())
