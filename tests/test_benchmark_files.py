import json
import os
import re
import sys

# ==================================================================================================

benchmark_dir = "dataset/benchmarks/"

# ==================================================================================================


def check_benchmark_title(data: dict, path: str):

    title = data.get("title")
    if not title:
        return [f"{path}: Missing 'title' key in JSON."]

    expected = os.path.splitext(os.path.basename(path))[0]
    if title != expected:
        return [
            (
                f"{path}: Title must equal filename without extension.\n"
                f"  found title:    {title!r}\n"
                f"  expected title: {expected!r}"
            )
        ]

    # Check that title only contains allowed characters
    if not re.match(r"^[a-z0-9-]+$", title):
        return [
            (
                f"{path}: Title contains invalid characters. Only [a-z0-9-] are allowed.\n"
                f"  found title: {title!r}"
            )
        ]

    return []


# ==================================================================================================


def check_dataset_link(data: dict, path: str):

    dataset_info = data.get("dataset-info")
    if not dataset_info:
        return [f"{path}: Missing 'dataset-info' key in JSON."]

    if "link" not in dataset_info:
        return [f"{path}: Missing 'dataset-info.link' key in JSON."]
    if not isinstance(dataset_info["link"], str):
        return [
            f"{path}: 'Dataset Link must be a string, got {type(dataset_info['link']).__name__}."
        ]

    return []


# ==================================================================================================


def check_task_hierarchy(data: dict, path: str):

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


def check_benchmark_structure(data: dict, path: str):

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

    # Check that fields contain ["p", "c", "n", "d"] in some order and at least one metric
    if "fields" in benchmark and isinstance(benchmark["fields"], list):
        field_keys = [f.get("key") for f in benchmark["fields"] if isinstance(f, dict)]
        required_keys = {"p", "c", "n", "d"}
        if not required_keys.issubset(field_keys):
            errors.append(
                f"{path}: 'benchmark.fields' must contain entries with keys: {required_keys}."
            )
        if len(field_keys) <= 4:
            errors.append(
                f"{path}: 'benchmark.fields' must contain at least one field for metrics."
            )

    # Check that items contain ["p", "c", "n", "d"] in some order and at least one metric
    if "items" in benchmark and isinstance(benchmark["items"], list):
        for idx, item in enumerate(benchmark["items"]):
            if not isinstance(item, dict):
                errors.append(
                    f"{path}: 'benchmark.items[{idx}]' must be a JSON object."
                )
                continue

            item_keys = set(item.keys())
            required_keys = {"p", "c", "n", "d"}
            if not required_keys.issubset(item_keys):
                errors.append(
                    f"{path}: 'benchmark.items[{idx}]' must contain keys: {required_keys}."
                )
            metric_keys = [k for k in item_keys if k.startswith("m")]
            if not metric_keys:
                errors.append(
                    f"{path}: 'benchmark.items[{idx}]' must contain at least one metric field"
                )

    # Check that "p" field has "name" and "link" and both are not empty
    if "items" in benchmark and isinstance(benchmark["items"], list):
        for idx, item in enumerate(benchmark["items"]):
            if not isinstance(item, dict):
                continue
            if "p" in item and isinstance(item["p"], dict):
                p = item["p"]
                if "name" not in p or "link" not in p:
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].p' must contain 'name' and 'link' keys."
                    )
                else:
                    if not p["name"]:
                        errors.append(
                            f"{path}: 'benchmark.items[{idx}].p.name' must not be empty."
                        )
                    if not p["link"]:
                        errors.append(
                            f"{path}: 'benchmark.items[{idx}].p.link' must not be empty."
                        )

    # Check that paper and code links are valid URLs if they are not empty
    url_pattern = re.compile(
        r"^(https?://)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(/.*)?$"
    )
    if "items" in benchmark and isinstance(benchmark["items"], list):
        for idx, item in enumerate(benchmark["items"]):
            if not isinstance(item, dict):
                continue
            if "p" in item and isinstance(item["p"], dict):
                link = item["p"].get("link", "")
                if link and not url_pattern.match(link):
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].p.link' is not a valid URL: {link!r}"
                    )
            if "c" in item and isinstance(item["c"], str):
                code_link = item["c"]
                if code_link and not url_pattern.match(code_link):
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].c' is not a valid URL: {code_link!r}"
                    )

    # Check date fields are in YYYY-MM-DD format
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    if "items" in benchmark and isinstance(benchmark["items"], list):
        for idx, item in enumerate(benchmark["items"]):
            if not isinstance(item, dict):
                continue
            if "d" in item:
                date_value = item["d"]
                if date_value and not date_pattern.match(str(date_value)):
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].d' must be YYYY-MM-DD: {date_value!r}"
                    )

    return errors


# ==================================================================================================


def check_malicious_injections(data: dict, path: str):

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

    # Check that all items in the directory are json files
    files = sorted(os.listdir(benchmark_dir))
    if len(files) == 0:
        print(f"No files found in {benchmark_dir}.")
        return 0
    for item in files:
        if not item.endswith(".json"):
            print(
                f"ERROR: Non-JSON file found in {benchmark_dir}: {item}",
                file=sys.stderr,
            )
            return 1
    files = [os.path.join(benchmark_dir, f) for f in files]
    for item in files:
        if not os.path.isfile(item):
            print(
                f"ERROR: Non-file item found in {benchmark_dir}: {item}",
                file=sys.stderr,
            )
            return 1
    json_files = files

    # Check each JSON file
    all_errors = []
    for path in sorted(json_files):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            all_errors.append(f"{path}: Failed to parse JSON: {e}")
            continue
        except Exception as e:
            all_errors.append(f"{path}: Failed to read file as UTF-8: {e}")
            continue

        all_errors.extend(check_benchmark_title(data, path))
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
