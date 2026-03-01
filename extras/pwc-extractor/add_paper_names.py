import json
import os

# ==================================================================================================

benchmark_dir = "../../dataset/benchmarks/"

# ==================================================================================================


def process_datasets(data: list):
    results = {}
    for item in data:
        for v in item["variants"]:
            url = ""
            paper = ""

            if item["homepage"] != "":
                url = item["homepage"]
            elif "paper" in item and item["paper"] is not None:
                if "url" in item["paper"]:
                    if "paperswithcode.com" not in item["paper"]["url"]:
                        url = item["paper"]["url"]

            if "paper" in item and item["paper"] is not None:
                if "title" in item["paper"]:
                    paper = item["paper"]["title"]

            results[v] = {"url": url, "paper": paper}
    return results


# ==================================================================================================


def main():

    # Load datasets information
    path = "data/datasets.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data_ds = process_datasets(data)

    # Reorder data_ds by url
    data_ds = {v["url"]: v for _, v in data_ds.items()}

    for f in sorted(os.listdir(benchmark_dir)):
        if f.endswith(".json"):
            filepath = os.path.join(benchmark_dir, f)

            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            link = data.get("dataset-info", {}).get("link", "")
            paper = ""
            if link != "" and link in data_ds:
                paper = data_ds[link].get("paper", "")
            data["dataset-info"]["paper"] = paper

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

    print("Done updating benchmark files.")


# ==================================================================================================


if __name__ == "__main__":
    main()
