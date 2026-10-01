"""Merges qualifying data-only merge requests (normal MRs, not the GitHub sync MR).

Merges open merge requests that only change files below TARGET_FOLDER, have at least
MIN_THUMBS_UP thumbs up, no thumbs down and a successful pipeline. Thumbs up only count if given
after the latest version of the MR, and only from accounts at least MIN_VOTER_ACCOUNT_AGE_DAYS
old.

MRs with more changed files than MAX_CHANGED_FILES or an incomplete file list are left alone and
need a manual merge. See github_sync.py for the bot that merges the GitHub mirror branch.
"""

import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Set

import requests

# ==================================================================================================

API = os.getenv("GITLAB_API", "https://gitlab.com/api/v4")
TOKEN = os.environ["GITLAB_TOKEN"]
PROJECT_ID = os.getenv("PROJECT_ID") or os.getenv("CI_PROJECT_ID")
TARGET_FOLDER = os.environ.get("TARGET_FOLDER", "").rstrip("/")
TARGET_BRANCH = os.environ.get("TARGET_BRANCH") or os.environ.get(
    "CI_DEFAULT_BRANCH", "main"
)
SYNC_BRANCH = os.environ.get("SYNC_BRANCH", "")  # its MR is left to github_sync.py
SQUASH_COMMITS = os.environ.get("SQUASH_COMMITS", "1") == "1"
MIN_THUMBS_UP = int(os.environ.get("MIN_THUMBS_UP", "2"))
MAX_CHANGED_FILES = int(os.environ.get("MAX_CHANGED_FILES", "20"))
MIN_VOTER_ACCOUNT_AGE_DAYS = int(os.environ.get("MIN_VOTER_ACCOUNT_AGE_DAYS", "365"))

if not PROJECT_ID:
    print("PROJECT_ID or CI_PROJECT_ID must be set", file=sys.stderr)
    sys.exit(2)

session = requests.Session()
session.headers.update({"PRIVATE-TOKEN": TOKEN})

_account_created: Dict[int, Optional[datetime]] = {}

# ==================================================================================================


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


# ==================================================================================================


def get_json(path: str, params: Optional[Dict[str, Any]] = None) -> Any:
    r = session.get(f"{API}{path}", params=params, timeout=60)
    r.raise_for_status()
    return r.json()


def get_all(path: str, params: Optional[Dict[str, Any]] = None) -> List[Any]:
    """Fetch all pages of a list endpoint."""

    items: List[Any] = []
    page = "1"
    while page:
        query = {"per_page": 100, "page": page, **(params or {})}
        r = session.get(f"{API}{path}", params=query, timeout=60)
        r.raise_for_status()
        items.extend(r.json())
        page = r.headers.get("X-Next-Page", "")
    return items


# ==================================================================================================


def list_open_mrs() -> List[Dict[str, Any]]:
    return get_all(
        f"/projects/{PROJECT_ID}/merge_requests",
        {"state": "opened", "target_branch": TARGET_BRANCH},
    )


def mr_changes(iid: int) -> Dict[str, Any]:
    return get_json(f"/projects/{PROJECT_ID}/merge_requests/{iid}/changes")


# ==================================================================================================


def only_in_folder(changes: List[Dict[str, Any]], folder: str) -> bool:
    if not folder:
        return True
    folder = folder.rstrip("/") + "/"
    # A renamed file has both a new and a previous path, both have to be inside the folder
    for ch in changes:
        for key in ("new_path", "old_path"):
            p = ch.get(key)
            if p and not p.startswith(folder):
                return False
    return True


def file_list_usable(
    details: Dict[str, Any], changes: Dict[str, Any], limit: int
) -> bool:
    """The file list must be complete and small, else a file could be hidden in it."""

    # Large MRs have a count like "1000+" and a truncated file list
    count = str(details.get("changes_count") or "")
    if changes.get("overflow") or not count.isdigit() or int(count) > limit:
        return False
    return len(changes.get("changes", [])) <= limit


# ==================================================================================================


def voter_old_enough(user_id: int) -> bool:
    if MIN_VOTER_ACCOUNT_AGE_DAYS <= 0:
        return True
    if user_id not in _account_created:
        created = get_json(f"/users/{user_id}").get("created_at")
        _account_created[user_id] = parse_time(created) if created else None

    created_at = _account_created[user_id]
    if created_at is None:
        # Without the creation date the age is unknown, so the vote does not count
        return False
    age = datetime.now(timezone.utc) - created_at
    return age >= timedelta(days=MIN_VOTER_ACCOUNT_AGE_DAYS)


def latest_version_time(iid: int) -> datetime:
    """Time of the latest push to the MR, taken from the GitLab server."""

    versions = get_all(f"/projects/{PROJECT_ID}/merge_requests/{iid}/versions")
    return max(parse_time(v["created_at"]) for v in versions)


def thumbs_summary(iid: int, author_id: int, since: datetime) -> Dict[str, int]:
    """Count thumbs up (only newer than 'since') and thumbs down (always, as a veto)."""

    pos: Set[int] = set()
    neg: Set[int] = set()
    # This endpoint only lists awards of the MR itself, not of its comments
    for a in get_all(f"/projects/{PROJECT_ID}/merge_requests/{iid}/award_emoji"):
        uid = (a.get("user") or {}).get("id")
        if uid is None or uid == author_id or not voter_old_enough(uid):
            continue
        name = a.get("name")
        if name == "thumbsdown":
            neg.add(uid)
        elif name == "thumbsup" and parse_time(a["created_at"]) > since:
            pos.add(uid)
    return {"pos": len(pos), "neg": len(neg)}


def has_enough_thumbs(iid: int, author_id: int) -> bool:
    thumbs = thumbs_summary(iid, author_id, latest_version_time(iid))
    print(f'MR !{iid}: {{"pos": {thumbs["pos"]}, "neg": {thumbs["neg"]}}}')
    return thumbs["neg"] == 0 and thumbs["pos"] >= MIN_THUMBS_UP


# ==================================================================================================


def pipeline_succeeded(details: Dict[str, Any], sha: str) -> bool:
    head = details.get("head_pipeline") or {}
    # The pipeline has to belong to the current head commit. Right after a push, the old
    # pipeline of the previous commit would still be listed as the head pipeline.
    return head.get("status") == "success" and head.get("sha") == sha


# ==================================================================================================


def try_merge(iid: int, sha: str, message: str) -> bool:
    # The sha makes the merge fail if the MR got a new commit in the meantime
    payload = {"sha": sha, "merge_commit_message": message, "squash": SQUASH_COMMITS}
    r = session.put(
        f"{API}/projects/{PROJECT_ID}/merge_requests/{iid}/merge",
        json=payload,
        timeout=60,
    )
    if r.ok:
        print(f"Merged MR !{iid}")
        return True
    print(f"Merge failed for !{iid}: {r.status_code} {r.text}", file=sys.stderr)
    return False


# ==================================================================================================


def process_mr(mr: Dict[str, Any]) -> None:
    iid = mr["iid"]
    details = get_json(f"/projects/{PROJECT_ID}/merge_requests/{iid}")
    changes = mr_changes(iid)
    if not file_list_usable(details, changes, MAX_CHANGED_FILES):
        print(f"Skip !{iid}: too many files or incomplete file list")
        return
    if not only_in_folder(changes.get("changes", []), TARGET_FOLDER):
        return
    if details.get("has_conflicts"):
        print(f"Skip !{iid}: has conflicts")
        return

    sha = (
        details.get("sha")
        or details.get("diff_head_sha")
        or (details.get("merge_commit_sha") or "")
    )
    if not sha:
        print(f"Skip !{iid}: missing head sha", file=sys.stderr)
        return
    if not pipeline_succeeded(details, sha):
        print(f"Skip !{iid}: no successful pipeline for the current commit")
        return

    author_id = (details.get("author") or {}).get("id") or -1
    if not has_enough_thumbs(iid, author_id):
        return

    try_merge(iid, sha, f"Auto-merged !{iid} by CI bot.")


# ==================================================================================================


def main() -> int:
    open_mrs = list_open_mrs()
    print(f"Found {len(open_mrs)} open merge requests.")

    for mr in open_mrs:
        if mr.get("work_in_progress") or mr.get("draft"):
            continue
        if SYNC_BRANCH and mr.get("source_branch") == SYNC_BRANCH:
            continue
        process_mr(mr)

    return 0


# ==================================================================================================

if __name__ == "__main__":
    sys.exit(main())
