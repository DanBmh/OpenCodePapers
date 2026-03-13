import json
import os
import re
from typing import Any, Dict, List, Optional

# ==================================================================================================

benchmark_dir = "../../dataset/benchmarks/"

# ==================================================================================================


def normalize_title(title: Any) -> str:
    if not isinstance(title, str):
        return ""
    return " ".join(title.strip().lower().split())


def normalize_url(url: Any) -> str:
    if not isinstance(url, str) or not url:
        return ""

    normalized = url.strip().lower()
    normalized = re.sub(r"^https?://", "", normalized)
    normalized = normalized.replace("www.", "")

    if normalized.endswith("/"):
        normalized = normalized[:-1]

    if "arxiv.org/abs/" in normalized or "arxiv.org/pdf/" in normalized:
        normalized = re.sub(
            r"(arxiv\.org/(?:abs|pdf)/\d+\.\d+)(v\d+)?(?:\.pdf)?$", r"\1", normalized
        )

    return normalized


# ==================================================================================================


def build_indexes(papers: List[Dict[str, Any]]):
    by_title: Dict[str, List[Dict[str, Any]]] = {}
    by_link: Dict[str, List[Dict[str, Any]]] = {}

    for paper in papers:
        title = paper.get("title", "")
        title_key = normalize_title(title)
        if title_key:
            by_title.setdefault(title_key, []).append(paper)

        links = [
            paper.get("paper_url", ""),
            paper.get("url_abs", ""),
            paper.get("url_pdf", ""),
            paper.get("conference_url_abs", ""),
            paper.get("conference_url_pdf", ""),
        ]

        for link in links:
            link_key = normalize_url(link)
            if link_key:
                by_link.setdefault(link_key, []).append(paper)

    return by_title, by_link


# ==================================================================================================


def resolve_paper(
    paper_name: str,
    paper_link: str,
    by_title: Dict[str, List[Dict[str, Any]]],
    by_link: Dict[str, List[Dict[str, Any]]],
) -> Optional[Dict[str, Any]]:
    title_key = normalize_title(paper_name)
    title_candidates = by_title.get(title_key, []) if title_key else []

    # Prefer title match when unique. If duplicate/no title match, fallback to link.
    if len(title_candidates) == 1:
        return title_candidates[0]

    link_key = normalize_url(paper_link)
    link_candidates = by_link.get(link_key, []) if link_key else []
    if len(link_candidates) == 1:
        return link_candidates[0]
    return None


# ==================================================================================================


def main():

    path = "data/papers.json"
    with open(path, "r", encoding="utf-8") as f:
        papers = json.load(f)
    by_title, by_link = build_indexes(papers)

    total_items = 0
    matched_items = 0

    for filename in sorted(os.listdir(benchmark_dir)):
        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(benchmark_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        changed = False
        items = data.get("benchmark", {}).get("items", [])
        for item in items:
            paper_info = item.get("p")
            if not isinstance(paper_info, dict):
                continue

            total_items += 1
            paper_name = paper_info.get("name", "")
            paper_link = paper_info.get("link", "")

            matched_paper = resolve_paper(paper_name, paper_link, by_title, by_link)
            authors_list = matched_paper.get("authors", []) if matched_paper else []
            authors = ", ".join(authors_list) if authors_list else ""

            if paper_info.get("authors") != authors:
                paper_info["authors"] = authors
                changed = True

            if authors_list:
                matched_items += 1

        if changed:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

    print(
        f"Updated benchmark files. Matched authors for {matched_items}/{total_items} entries."
    )


# ==================================================================================================


if __name__ == "__main__":
    main()
