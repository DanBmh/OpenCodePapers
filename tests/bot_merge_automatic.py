import os
import sys
from typing import Any, Dict, List, Set

import requests

# ==================================================================================================

API = os.getenv("GITLAB_API", "https://gitlab.com/api/v4")
TOKEN = os.environ["GITLAB_TOKEN"]
PROJECT_ID = os.getenv("PROJECT_ID") or os.getenv("CI_PROJECT_ID")
TARGET_FOLDER = os.environ.get("TARGET_FOLDER", "").rstrip("/")
REQUIRE_SUCCESS_PIPELINE = os.environ.get("REQUIRE_SUCCESS_PIPELINE", "1") == "1"
MIN_THUMBS_UP = 2

if not PROJECT_ID:
    print("PROJECT_ID or CI_PROJECT_ID must be set", file=sys.stderr)
    sys.exit(2)

session = requests.Session()
session.headers.update({"PRIVATE-TOKEN": TOKEN})

# ==================================================================================================


def list_open_mrs(project_id: str) -> List[Dict[str, Any]]:

    mrs: List[Dict[str, Any]] = []
    page = 1
    while True:
        r = session.get(
            f"{API}/projects/{project_id}/merge_requests",
            params={"state": "opened", "per_page": 100, "page": page},
            timeout=30,
        )
        r.raise_for_status()
        batch = r.json()
        mrs.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    return mrs


# ==================================================================================================


def mr_details(project_id: str, iid: int) -> Dict[str, Any]:
    r = session.get(f"{API}/projects/{project_id}/merge_requests/{iid}", timeout=30)
    r.raise_for_status()
    return r.json()


def mr_changes(project_id: str, iid: int) -> List[Dict[str, Any]]:
    r = session.get(
        f"{API}/projects/{project_id}/merge_requests/{iid}/changes", timeout=60
    )
    r.raise_for_status()
    return r.json().get("changes", [])


def mr_awards(project_id: str, iid: int) -> List[Dict[str, Any]]:
    r = session.get(
        f"{API}/projects/{project_id}/merge_requests/{iid}/award_emoji", timeout=30
    )
    r.raise_for_status()
    return r.json()


# ==================================================================================================


def only_in_folder(changes: List[Dict[str, Any]], folder: str) -> bool:
    if not folder:
        return True
    folder = folder.rstrip("/") + "/"
    for ch in changes:
        for key in ("new_path", "old_path"):
            p = ch.get(key)
            if p and not p.startswith(folder):
                return False
    return True


# ==================================================================================================


def thumbs_summary(project_id: str, iid: int, author_id: int) -> Dict[str, Any]:
    awards = mr_awards(project_id, iid)
    pos: Set[int] = set()
    neg: Set[int] = set()
    for a in awards:
        uid = (a.get("user") or {}).get("id")
        if uid == author_id:
            continue
        name = a.get("name")
        if name == "thumbsup":
            pos.add(uid)
        elif name == "thumbsdown":
            neg.add(uid)
    return {
        "pos": len(pos),
        "neg": len(neg),
        "pos_users": list(pos),
        "neg_users": list(neg),
    }


# ==================================================================================================


def head_pipeline_status(mr: Dict[str, Any]) -> str:
    head = mr.get("head_pipeline") or {}
    # success, failed, running, pending, canceled, skipped, manual
    return head.get("status") or "unknown"


# ==================================================================================================


def try_merge(
    project_id: str, iid: int, sha: str, message: str, wait_for_success: bool
) -> bool:

    payload = {"sha": sha, "merge_commit_message": message}
    if not wait_for_success:
        # Use merge_when_pipeline_succeeds when allowed
        payload["merge_when_pipeline_succeeds"] = True
    r = session.put(
        f"{API}/projects/{project_id}/merge_requests/{iid}/merge",
        data=payload,
        timeout=60,
    )

    if r.ok:
        print(f"Merged MR !{iid}")
        return True
    else:
        print(f"Merge failed for !{iid}: {r.status_code} {r.text}", file=sys.stderr)
        return False


# ==================================================================================================


def main() -> int:

    merged_any = False
    open_mrs = list_open_mrs(PROJECT_ID)
    print(f"Found {len(open_mrs)} open merge requests.")

    for mr in open_mrs:
        if mr.get("work_in_progress") or mr.get("draft"):
            continue
        iid = mr.get("iid")
        details = mr_details(PROJECT_ID, iid)
        author_id = (details.get("author") or {}).get("id") or -1

        changes = mr_changes(PROJECT_ID, iid)
        if not only_in_folder(changes, TARGET_FOLDER):
            continue

        thumbs = thumbs_summary(PROJECT_ID, iid, author_id)
        print(f'MR !{iid}: {{"pos": {thumbs["pos"]}, "neg": {thumbs["neg"]}}}')
        if thumbs["neg"] > 0 or thumbs["pos"] < MIN_THUMBS_UP:
            continue

        # Pipeline gate
        status = head_pipeline_status(details)
        if REQUIRE_SUCCESS_PIPELINE:
            if status != "success":
                print(f"Skip !{iid}: pipeline status={status}")
                continue
            merge_when_success = False
        else:
            merge_when_success = status != "success"

        sha = (
            details.get("sha")
            or details.get("diff_head_sha")
            or (details.get("merge_commit_sha") or "")
        )
        if not sha:
            print(f"Skip !{iid}: missing head sha", file=sys.stderr)
            continue

        msg = (
            f"Auto-merged by CI bot: all changes within '{TARGET_FOLDER}', "
            f"{thumbs['pos']}x up, 0x down."
        )
        if try_merge(
            PROJECT_ID,
            iid,
            sha,
            msg,
            wait_for_success=REQUIRE_SUCCESS_PIPELINE is True
            and merge_when_success is False,
        ):
            merged_any = True

    return 0 if merged_any else 0


# ==================================================================================================

if __name__ == "__main__":
    sys.exit(main())
