import json
import math
import os
from datetime import datetime

# ==================================================================================================

benchmark_dir = "../dataset/benchmarks/"

# ==================================================================================================


def should_delete_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Access items from the nested benchmark structure
        items = data.get("benchmark", {}).get("items", [])

        # rule: drop if less than 3 items
        if len(items) < 3:
            return True

        # rule: drop if newest entry is older than the number of items
        # (-> drop outdated benchmarks, but keep those which were often used for longer time)
        threshold = max(5, len(set((str(it["p"]) for it in items if it["p"]))))
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

        # rule: drop if benchmark has no papers with code
        no_code = True
        for it in items:
            c = it.get("c")
            if not c:
                continue
            else:
                no_code = False
                break
        if no_code:
            return no_code

    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return False

    return False


# ==================================================================================================


def main():
    for f in sorted(os.listdir(benchmark_dir)):
        if f.endswith(".json"):
            filepath = os.path.join(benchmark_dir, f)
            if should_delete_file(filepath):
                os.remove(filepath)


# ==================================================================================================

if __name__ == "__main__":
    main()
