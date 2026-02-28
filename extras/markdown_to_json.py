import json
import os
import re
from pathlib import Path

# ==================================================================================================

benchmark_dir = "../dataset/benchmarks/"
output_dir = "../dataset/benchmarks_json/"

# regex to extract the json block between ```json:table ... ```
json_block_pattern = re.compile(r"```json:table\s*(\{.*?\})\s*```", re.DOTALL)

# ==================================================================================================


def markdown_to_json():
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for f in sorted(os.listdir(benchmark_dir)):
        if f.endswith(".md"):
            filepath = os.path.join(benchmark_dir, f)

            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    text = file.read()
                data = {}

                # Extract title from the first H1 heading
                title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
                if title_match:
                    data["title"] = title_match.group(1)

                # Extract task from Task Hierarchy line
                task_match = re.search(r"Task Hierarchy:\s*\[(.+?)\]", text)
                if task_match:
                    tasks = [
                        t.strip().strip("'\"") for t in task_match.group(1).split(",")
                    ]
                    data["task-hierarchy"] = tasks

                # Extract dataset from Dataset Link line
                dataset_match = re.search(r"\[Dataset Link\]\((.+?)\)", text)
                if dataset_match:
                    data["dataset-info"] = {}
                    data["dataset-info"]["link"] = dataset_match.group(1)

                # Extract JSON block
                match = json_block_pattern.search(text)
                if not match:
                    print(f"Skipping {f}: no json block found")
                    continue
                data["benchmark"] = json.loads(match.group(1))

                # Create output filename
                output_filename = Path(f).stem + ".json"
                output_filepath = os.path.join(output_dir, output_filename)

                # Write JSON to file
                with open(output_filepath, "w", encoding="utf-8") as outfile:
                    json.dump(data, outfile, indent=2, ensure_ascii=False)

                print(f"✓ Converted {f} -> {output_filename}")

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in {f}: {e}")
            except Exception as e:
                print(f"Error processing {f}: {e}")


# ==================================================================================================

if __name__ == "__main__":
    markdown_to_json()
