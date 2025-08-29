import copy
import json

# ==================================================================================================


cont_url = (
    "https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md"
)
row_template = {
    "fields": [
        {"key": "p", "label": "Paper"},
        {"key": "c", "label": "Code"},
        # {"key": "m1", "label": "Metric1", "sortable": "true"},
        # {"key": "m2", "label": "Metric2", "sortable": "true"},
        # {"key": "m3", "label": "Metric3", "sortable": "true"},
        {"key": "n", "label": "ModelName"},
        {"key": "d", "label": "ReleaseDate", "sortable": "true"},
    ],
    "items": [],
    "markdown": "true",
    "caption": f"Check out how to [contribute]({cont_url}) new results.",
}

file_template = """# {}

[Dataset Link]({}) \\
Task Hierarchy: {}

<br>

```json:table
{}
```
"""

task_name_replacers = {
    "1 Image, 2*2 Stitchi": "",
    "1 Image, 2*2 Stitching": "",
    "10-shot image generation": "",
    "16k": "",
    "4K 60Fps": "",
    "3D": "",
    "Unsupervised Anomaly Detection with Specified Settings -- 0.1% anomaly": "Unsupervised Anomaly Detection",
    "Unsupervised Anomaly Detection with Specified Settings -- 1% anomaly": "Unsupervised Anomaly Detection",
    "Unsupervised Anomaly Detection with Specified Settings -- 10% anomaly": "Unsupervised Anomaly Detection",
    "Unsupervised Anomaly Detection with Specified Settings -- 20% anomaly": "Unsupervised Anomaly Detection",
    "Unsupervised Anomaly Detection with Specified Settings -- 30% anomaly": "Unsupervised Anomaly Detection",
}

# ==================================================================================================


def process_evaluation_tables(data: list, task_hierarchy: list):
    results = []

    for item in data:
        tsh = list(task_hierarchy)

        if "task" in item:
            task = item["task"]
            if task in task_name_replacers:
                task = task_name_replacers[task]

            if task != "":
                tsh.append(task)

        if "subtasks" in item:
            res = process_evaluation_tables(item["subtasks"], list(tsh))
            results.extend(res)

        if "datasets" in item:
            for ds in item["datasets"]:
                if len(ds["sota"]["rows"]) >= 3:
                    res = {
                        "bench_url": ds["dataset_links"][0]["url"],
                        "task_hierarchy": list(tsh),
                        "dataset": ds["dataset"],
                        "sota": ds["sota"],
                    }
                    results.append(res)

    return results


# ==================================================================================================


def process_datasets(data: list):
    results = {}
    for item in data:
        for v in item["variants"]:
            url = ""

            if item["homepage"] != "":
                url = item["homepage"]
            elif "paper" in item and item["paper"] is not None:
                if "url" in item["paper"]:
                    if "paperswithcode.com" not in item["paper"]["url"]:
                        url = item["paper"]["url"]

            results[v] = url
    return results


# ==================================================================================================


def build_sota_data(data: dict):
    metrics = data["metrics"]
    mdata = []
    for i in range(len(metrics)):
        mdata.append(
            {
                "key": "m" + str(i + 1),
                "label": metrics[i],
                "sortable": "true",
            }
        )

    sota_data = copy.deepcopy(row_template)
    sota_data["fields"] = (
        [f for f in sota_data["fields"] if f["key"] in ["p", "c"]]
        + mdata
        + [f for f in sota_data["fields"] if f["key"] in ["n", "d"]]
    )

    items = []
    for row in data["rows"]:
        item = {
            "p": f"[{row['paper_title']}]({row['paper_url']})",
            "c": (
                f"[&check;&nbsp;Link]({row['code_links'][0]['url']})"
                if len(row["code_links"]) > 0
                else ""
            ),
            "n": row["model_name"],
            "d": row["paper_date"],
        }
        for i in range(len(mdata)):
            if mdata[i]["label"] in row["metrics"]:
                item[mdata[i]["key"]] = row["metrics"][mdata[i]["label"]]
        items.append(item)
    sota_data["items"] = items

    return sota_data


# ==================================================================================================


def main():

    path = "data/evaluation-tables.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data_et = process_evaluation_tables(data, [])

    path = "data/datasets.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data_ds = process_datasets(data)

    # Map dataset links to evaluation tables
    for et in data_et:
        if et["dataset"] in data_ds:
            et["data_url"] = data_ds[et["dataset"]]
        else:
            et["data_url"] = ""

    # Build files
    path = "../../benchmarks/{}.md"
    for et in data_et:
        sdata = build_sota_data(et["sota"])
        name = et["bench_url"].replace("https://paperswithcode.com/sota/", "")

        fdata = file_template.format(
            name, et["data_url"], et["task_hierarchy"], json.dumps(sdata, indent=2)
        )

        fpath = path.format(name)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(fdata)


# ==================================================================================================


if __name__ == "__main__":
    main()
