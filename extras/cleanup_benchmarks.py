import json
import math
import os
import re
from datetime import datetime

# ==================================================================================================

benchmark_dir = "../dataset/benchmarks/"

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

        # rule: drop if less than 3 items
        if len(items) < 3:
            return True

        # rule: drop if newest entry is older than the number of items
        # (-> drop outdated benchmarks, but keep those which were often used for longer time)
        threshold = len(items)
        all_old = True
        for it in items:
            d = it.get("d")
            if not d:
                continue
            try:
                pub_date = datetime.strptime(d, "%Y-%m-%d")
                age_years = (datetime.now() - pub_date).days / 365.25
                if math.floor(age_years) <= threshold:
                    all_old = False
                    break
            except ValueError:
                pass
        if all_old:
            return all_old

    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return False

    return False


# ==================================================================================================


def main():
    for f in sorted(os.listdir(benchmark_dir)):
        if f.endswith(".md"):
            filepath = os.path.join(benchmark_dir, f)
            if should_delete_file(filepath):
                os.remove(filepath)


# ==================================================================================================

if __name__ == "__main__":
    main()
