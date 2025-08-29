# PwC Extractor

Extract initial data from _PapersWithCode_ dumps.

- Download `datasets.json.gz` and `evaluation-tables.json.gz` from: \
  _<https://github.com/World-Snapshot/papers-with-code/tree/main/data>_

- Extract them to `extras/pwc-extractor/data/` folder and rename them to `datasets.json` and `evaluation-tables.json`.

- Run:
  
  ```bash
  cd extras/pwc-extractor/
  python3 extract_data.py
  ```
