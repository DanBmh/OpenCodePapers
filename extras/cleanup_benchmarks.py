import json
import os
import re
from datetime import datetime, timedelta

# ==================================================================================================

benchmark_dir = "../dataset/benchmarks/"
date_threshold = datetime.now() - timedelta(days=5 * 365.25)

# regex to extract the json block between ```json:table ... ```
json_block_pattern = re.compile(r"```json:table\s*(\{.*?\})\s*```", re.DOTALL)

# ==================================================================================================


def should_delete_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        match = json_block_pattern.search(text)
        if not match:
            # skip if no json block
            return False

        data = json.loads(match.group(1))
        items = data.get("items", [])

        # rule 1: less than 3 items
        if len(items) < 3:
            return True

        # rule 2: no item is newer than 5 years
        all_old = True
        for it in items:
            d = it.get("d")
            if not d:
                continue
            try:
                pub_date = datetime.strptime(d, "%Y-%m-%d")
                if pub_date >= date_threshold:
                    all_old = False
                    break
            except ValueError:
                pass
        return all_old

    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return False


# ==================================================================================================


def main():
    for f in os.listdir(benchmark_dir):
        if f.endswith(".md"):
            filepath = os.path.join(benchmark_dir, f)
            if should_delete_file(filepath):
                os.remove(filepath)


# ==================================================================================================

if __name__ == "__main__":
    main()
