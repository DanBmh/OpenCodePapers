"""Merges the sync MR that brings the GitHub-mirrored branch into TARGET_BRANCH.

SYNC_BRANCH is pull-mirrored from GitHub's intake branch. This opens an MR from SYNC_BRANCH into
TARGET_BRANCH if none exists yet, and merges it once its pipeline succeeds. The votes were
already collected on GitHub (see data_merge.py's counterpart there), so only the folder check and
the pipeline are required here. It is merged without squashing and the source branch is kept,
because the mirror needs it.

Does nothing if SYNC_BRANCH is not set: the sync isn't wired up yet.
"""

import os
import sys
from typing import Any, Dict, List, Optional

import requests

# ==================================================================================================

API = os.getenv("GITLAB_API", "https://gitlab.com/api/v4")
TOKEN = os.environ["GITLAB_TOKEN"]
PROJECT_ID = os.getenv("PROJECT_ID") or os.getenv("CI_PROJECT_ID")
TARGET_FOLDER = os.environ.get("TARGET_FOLDER", "").rstrip("/")
TARGET_BRANCH = os.environ.get("TARGET_BRANCH") or os.environ.get(
    "CI_DEFAULT_BRANCH", "main"
)
SYNC_BRANCH = os.environ.get("SYNC_BRANCH", "")
SYNC_MAX_CHANGED_FILES = int(os.environ.get("SYNC_MAX_CHANGED_FILES", "100"))

if SYNC_BRANCH and not PROJECT_ID:
    print("PROJECT_ID or CI_PROJECT_ID must be set", file=sys.stderr)
    sys.exit(2)
if SYNC_BRANCH and not TARGET_FOLDER:
    # Without a folder restriction the sync MR would let anything through
    print("TARGET_FOLDER must be set", file=sys.stderr)
    sys.exit(2)

session = requests.Session()
session.headers.update({"PRIVATE-TOKEN": TOKEN})

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


def current_user_id() -> int:
    return get_json("/user")["id"]


def find_sync_mr(bot_id: int) -> Optional[Dict[str, Any]]:
    """Only an MR created by the bot itself from the sync branch counts."""

    mrs = get_all(
        f"/projects/{PROJECT_ID}/merge_requests",
        {
            "state": "opened",
            "target_branch": TARGET_BRANCH,
            "source_branch": SYNC_BRANCH,
        },
    )
    for mr in mrs:
        if (
            mr.get("source_project_id") == mr.get("target_project_id")
            and (mr.get("author") or {}).get("id") == bot_id
        ):
            return mr
    return None


def create_sync_mr() -> Optional[Dict[str, Any]]:
    """Open the sync MR if the sync branch has commits the target branch does not have."""

    r = session.get(
        f"{API}/projects/{PROJECT_ID}/repository/compare",
        params={"from": TARGET_BRANCH, "to": SYNC_BRANCH},
        timeout=60,
    )
    if r.status_code == 404:
        print(f"Sync branch '{SYNC_BRANCH}' does not exist (yet).")
        return None
    r.raise_for_status()
    if not r.json().get("commits"):
        return None

    payload = {
        "source_branch": SYNC_BRANCH,
        "target_branch": TARGET_BRANCH,
        "title": f"Sync data from '{SYNC_BRANCH}' (GitHub)",
        "remove_source_branch": False,
        "squash": False,
    }
    r = session.post(
        f"{API}/projects/{PROJECT_ID}/merge_requests", json=payload, timeout=60
    )
    r.raise_for_status()
    mr = r.json()
    print(f"Created sync MR !{mr.get('iid')}")
    return mr


# ==================================================================================================


def only_in_folder(changes: List[Dict[str, Any]], folder: str) -> bool:
    prefix = folder.rstrip("/") + "/"
    # A renamed file has both a new and a previous path, both have to be inside the folder
    for ch in changes:
        for key in ("new_path", "old_path"):
            p = ch.get(key)
            if p and not p.startswith(prefix):
                return False
    return True


def file_list_usable(details: Dict[str, Any], changes: Dict[str, Any]) -> bool:
    """The file list must be complete and small, else a file could be hidden in it."""

    # Large MRs have a count like "1000+" and a truncated file list
    count = str(details.get("changes_count") or "")
    if (
        changes.get("overflow")
        or not count.isdigit()
        or int(count) > SYNC_MAX_CHANGED_FILES
    ):
        return False
    return len(changes.get("changes", [])) <= SYNC_MAX_CHANGED_FILES


# ==================================================================================================


def pipeline_succeeded(details: Dict[str, Any], sha: str) -> bool:
    head = details.get("head_pipeline") or {}
    # The pipeline has to belong to the current head commit. Right after a push, the old
    # pipeline of the previous commit would still be listed as the head pipeline.
    return head.get("status") == "success" and head.get("sha") == sha


# ==================================================================================================


def try_merge(iid: int, sha: str) -> bool:
    # The sha makes the merge fail if the MR got a new commit in the meantime
    payload = {
        "sha": sha,
        "merge_commit_message": f"Auto-merged sync MR !{iid} by CI bot.",
        "squash": False,
        "should_remove_source_branch": False,  # the mirror needs this branch
    }
    r = session.put(
        f"{API}/projects/{PROJECT_ID}/merge_requests/{iid}/merge",
        json=payload,
        timeout=60,
    )
    if r.ok:
        print(f"Merged sync MR !{iid}")
        return True
    print(f"Merge failed for sync MR !{iid}: {r.status_code} {r.text}", file=sys.stderr)
    return False


# ==================================================================================================


def main() -> int:
    if not SYNC_BRANCH:
        print("SYNC_BRANCH not set, nothing to sync.")
        return 0

    bot_id = current_user_id()
    mr = find_sync_mr(bot_id) or create_sync_mr()
    if mr is None:
        return 0

    iid = mr["iid"]
    details = get_json(f"/projects/{PROJECT_ID}/merge_requests/{iid}")
    changes = get_json(f"/projects/{PROJECT_ID}/merge_requests/{iid}/changes")
    if not file_list_usable(details, changes):
        print(f"Skip sync MR !{iid}: too many files or incomplete file list")
        return 0
    if not only_in_folder(changes.get("changes", []), TARGET_FOLDER):
        print(f"Skip sync MR !{iid}: touches files outside {TARGET_FOLDER}")
        return 0
    if details.get("has_conflicts"):
        print(f"Skip sync MR !{iid}: has conflicts")
        return 0

    sha = (
        details.get("sha")
        or details.get("diff_head_sha")
        or (details.get("merge_commit_sha") or "")
    )
    if not sha:
        print(f"Skip sync MR !{iid}: missing head sha", file=sys.stderr)
        return 0
    if not pipeline_succeeded(details, sha):
        print(f"Skip sync MR !{iid}: no successful pipeline for the current commit")
        return 0

    try_merge(iid, sha)
    return 0


# ==================================================================================================

if __name__ == "__main__":
    sys.exit(main())
