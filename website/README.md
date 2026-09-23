# Website

The core website of _OpenCodePapers_.

It is a static site: the scripts in this folder read the JSON files in `dataset/`
and write plain HTML into `public/`, which is also what the CI creates and publishes.

## Building

Run from the repository root, in this order:

```bash
python3 website/build_tasks_data.py
python3 website/build_website_bench.py
python3 website/build_website_tasks.py
python3 website/build_website_papers.py
```

Afterwards open `public/index.html` in a browser.
