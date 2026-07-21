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

    if not isinstance(title, str):
        return f"Title must be a string, got '{type(title).__name__}'"

    # Check that title is the first entry in the JSON object
    first_key = next(iter(data.keys()))
    if first_key != "title":
        return [f"{path}: 'title' must be the first key in the JSON file"]

    # Check that title equals filename
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

    # Check that title is not too long
    if len(title) > 128:
        return [
            (
                f"{path}: Title is too long ({len(title)} characters). "
                f"Maximum allowed length is 128 characters.\n"
                f"  found title: {title!r}"
            )
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

    # Check that task hierarchy is second entry in the JSON object
    keys = list(data.keys())
    if len(keys) < 2 or keys[1] != "task-hierarchy":
        return [f"{path}: 'task-hierarchy' must be the second key in the JSON file"]

    # Enforce list elements be strings (empty list ok)
    if not all(isinstance(x, str) for x in task_hierarchy):
        return [f"{path}: All Task Hierarchy entries must be strings."]

    # Check that items are not too long
    for idx, item in enumerate(task_hierarchy):
        if len(item) > 96:
            return [
                f"{path}: Task Hierarchy item at index {idx} is longer than 96 characters"
            ]

    return []


# ==================================================================================================


def helper_link_validity(link: str) -> str:

    if not isinstance(link, str):
        return f"Link must be a string, got '{type(link).__name__}'"

    if link == "":
        return ""

    if len(link) > 255:
        return "Link is longer than 255 characters"

    url_pattern = re.compile(
        r"^(https?://)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(/.*)?$"
    )
    if not url_pattern.match(link):
        return "Link is not a valid URL"

    return ""


# ==================================================================================================


def check_dataset_info(data: dict, path: str):

    dataset_info = data.get("dataset-info")
    if not dataset_info:
        return [f"{path}: Missing 'dataset-info' key in JSON."]

    if "link" not in dataset_info:
        return [f"{path}: Missing 'dataset-info.link' key in JSON."]

    # Check that dataset-info is third entry in the JSON object
    keys = list(data.keys())
    if len(keys) < 3 or keys[2] != "dataset-info":
        return [f"{path}: 'dataset-info' must be the third key in the JSON file"]

    # Check link validity (can be empty)
    link_error = helper_link_validity(dataset_info["link"])
    if link_error:
        return [f"{path}: 'dataset-info.link' error: {link_error}"]

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

    # Check that benchmark is fourth and last entry in the JSON object
    keys = list(data.keys())
    if len(keys) < 4 or keys[3] != "benchmark" or len(keys) > 4:
        errors.append(
            f"{path}: 'benchmark' must be the fourth and last key in the JSON file"
        )

    # Check for required keys
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


def check_benchmark_fields(data: dict, path: str):

    errors = []
    benchmark = data.get("benchmark")

    p = {"key": "p", "label": "Paper"}
    c = {"key": "c", "label": "Code"}
    n = {"key": "n", "label": "ModelName"}
    d = {"key": "d", "label": "ReleaseDate", "sortable": "true"}
    req = [p, c, n, d]

    # Check that fields contains [p, c, n, d] as defined above
    fields = benchmark.get("fields")
    for f in fields:
        for r in list(req):
            if f == r:
                req.remove(r)
                continue
    if req:
        missing = ", ".join(r["key"] for r in req)
        errors.append(
            f"{path}: 'benchmark.fields' is missing required fields: {missing}."
        )

    # Check that rest of the fields (if any) start with "m" and have a non-empty label
    for f in fields:
        if f in [p, c, n, d]:
            continue
        if not isinstance(f, dict):
            errors.append(
                f"{path}: 'benchmark.fields' entry {f!r} must be a JSON object."
            )
            continue
        key = f.get("key")
        label = f.get("label")
        if not isinstance(key, str) or not key.startswith("m"):
            errors.append(
                f"{path}: 'benchmark.fields' entry {f!r} has invalid 'key'. "
                f"Metric fields must have 'key' starting with 'm'."
            )
        if not isinstance(label, str) or not label.strip():
            errors.append(
                f"{path}: 'benchmark.fields' entry {f!r} has invalid 'label'. "
                f"Metric fields must have a non-empty 'label'."
            )
        if len(label) > 64:
            errors.append(
                f"{path}: 'benchmark.fields' entry {f!r} has 'label' longer than 64 characters."
            )

    return errors


# ==================================================================================================


def check_benchmark_items(data: dict, path: str):

    errors = []
    benchmark = data.get("benchmark")

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
            if "p" in item and not isinstance(item["p"], dict):
                if item["p"] != "":
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].p' must be a JSON object or empty string."
                    )
            if "p" in item and isinstance(item["p"], dict):
                p = item["p"]
                if "name" not in p or "link" not in p:
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].p' must contain 'name', 'link'"
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
    if "items" in benchmark and isinstance(benchmark["items"], list):
        for idx, item in enumerate(benchmark["items"]):
            if not isinstance(item, dict):
                continue
            if "p" in item and isinstance(item["p"], dict):
                link = item["p"].get("link", "")
                link_error = helper_link_validity(link)
                if link_error:
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].p.link' error: {link_error}"
                    )

            if "c" in item and isinstance(item["c"], str):
                link = item["c"]
                link_error = helper_link_validity(link)
                if link_error:
                    errors.append(
                        f"{path}: 'benchmark.items[{idx}].c' error: {link_error}"
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


def check_benchmark_order(data: dict, path: str):

    benchmark = data.get("benchmark")
    if not isinstance(benchmark, dict):
        return []

    fields = benchmark.get("fields")
    items = benchmark.get("items")
    if not isinstance(fields, list) or not isinstance(items, list):
        return []

    first_metric_key = None
    for field in fields:
        if isinstance(field, dict):
            key = field.get("key")
            if isinstance(key, str) and key.startswith("m"):
                first_metric_key = key
                break

    if not first_metric_key:
        return []

    values = []
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        value = None
        raw = item.get(first_metric_key)
        if isinstance(raw, (int, float)):
            value = float(raw)
        if isinstance(raw, str):
            cleaned = raw.strip()

            if "," in cleaned and "." not in cleaned:
                if re.match(r"^\s*[-+]?\d+,\d+(?:[eE][-+]?\d+)?\s*$", cleaned):
                    normalized = cleaned.replace(",", ".")
                else:
                    normalized = cleaned.replace(",", "")
            else:
                normalized = cleaned.replace(",", "")

            match = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", normalized)
            if match:
                try:
                    value = float(match.group(0))
                except ValueError:
                    value = None
        if value is not None:
            values.append((idx, value))

    if len(values) < 3:
        return []

    diffs = [values[i + 1][1] - values[i][1] for i in range(len(values) - 1)]
    nonzero_diffs = [d for d in diffs if d != 0]
    if not nonzero_diffs:
        return []

    sorted_diffs = sorted(nonzero_diffs)
    median_diff = sorted_diffs[len(sorted_diffs) // 2]
    ascending = median_diff >= 0
    direction = "ascending" if ascending else "descending"

    violations = []
    for i in range(len(values) - 1):
        left_idx, left_val = values[i]
        right_idx, right_val = values[i + 1]

        if ascending and right_val < left_val:
            violations.append((left_idx, left_val, right_idx, right_val))
        elif not ascending and right_val > left_val:
            violations.append((left_idx, left_val, right_idx, right_val))

    errors = []

    if violations:
        preview = "; ".join(
            (
                f"items[{l_idx}]={l_val} -> items[{r_idx}]={r_val}"
                for l_idx, l_val, r_idx, r_val in violations
            )
        )
        errors.append(
            (
                f"{path}: Benchmark items are not ordered by first metric {first_metric_key!r} "
                f"in inferred {direction} order. Violations: {len(violations)}. {preview}"
            )
        )

    # For equal metric values, older papers should come first (ascending by date).
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    metric_date_violations = []
    for i in range(len(values) - 1):
        left_idx, left_val = values[i]
        right_idx, right_val = values[i + 1]

        if left_val != right_val:
            continue

        left_item = items[left_idx]
        right_item = items[right_idx]
        if not isinstance(left_item, dict) or not isinstance(right_item, dict):
            continue

        left_date = str(left_item.get("d", "")).strip()
        right_date = str(right_item.get("d", "")).strip()
        if not date_pattern.match(left_date) or not date_pattern.match(right_date):
            continue

        if right_date < left_date:
            metric_date_violations.append(
                (left_idx, left_val, left_date, right_idx, right_val, right_date)
            )

    if metric_date_violations:
        preview = "; ".join(
            (
                f"items[{l_idx}] metric={l_val}, date={l_date} -> "
                f"items[{r_idx}] metric={r_val}, date={r_date}"
                for l_idx, l_val, l_date, r_idx, r_val, r_date in metric_date_violations
            )
        )
        errors.append(
            (
                f"{path}: Benchmark items with equal first metric {first_metric_key!r} "
                f"must be ordered by date ascending (older first). "
                f"Violations: {len(metric_date_violations)}. {preview}"
            )
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
                text = f.read()
                data = json.loads(text)
        except json.JSONDecodeError as e:
            all_errors.append(f"{path}: Failed to parse JSON: {e}")
            continue
        except Exception as e:
            all_errors.append(f"{path}: Failed to read file as UTF-8: {e}")
            continue
        if not isinstance(data, dict):
            all_errors.append(
                f"{path}: Top-level JSON structure must be an object/dict."
            )
            continue
        if json.dumps(data, ensure_ascii=False, indent=2) != text:
            all_errors.append(
                f"{path}: JSON file contains formatting issues (whitespaces, unicode-escapes, ...)"
            )
            continue

        all_errors.extend(check_benchmark_title(data, path))
        all_errors.extend(check_dataset_info(data, path))
        all_errors.extend(check_task_hierarchy(data, path))
        all_errors.extend(check_benchmark_structure(data, path))
        all_errors.extend(check_benchmark_fields(data, path))
        all_errors.extend(check_benchmark_items(data, path))
        all_errors.extend(check_benchmark_order(data, path))
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
