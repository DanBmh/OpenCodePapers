import json
import os

# ==================================================================================================

benchmark_dir = "../dataset/benchmarks/"

# ==================================================================================================


def drop_markdown_keys():
    for f in sorted(os.listdir(benchmark_dir)):
        if f.endswith(".json"):
            filepath = os.path.join(benchmark_dir, f)

            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    data = json.load(file)

                # Drop "markdown" and "caption" from benchmark dict
                if "benchmark" in data:
                    data["benchmark"].pop("markdown", None)
                    data["benchmark"].pop("caption", None)

                # Write back to file
                with open(filepath, "w", encoding="utf-8") as outfile:
                    json.dump(data, outfile, indent=2, ensure_ascii=False)

                print(f"✓ Processed {f}")

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in {f}: {e}")
            except Exception as e:
                print(f"Error processing {f}: {e}")


# ==================================================================================================

if __name__ == "__main__":
    drop_markdown_keys()
