"""Merge bot for GitHub (counterpart of .gitlab/bots/data_merge.py on GitLab).

Merges open pull requests into the intake branch if they

- change at most MAX_CHANGED_FILES files and only below TARGET_FOLDER (renames are checked on
  both the old and the new path),
- got at least MIN_THUMBS_UP thumbs up that were given AFTER the current head commit was first
  checked by CI (votes cannot be collected on a harmless version and kept after a new push),
- have no thumbs down,
- have a successful run of the required check for the current head commit.

Only reactions on the pull request itself count, not reactions on comments. Pull requests that
do not qualify are left alone and need a manual merge by a maintainer.
"""

import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Set, Tuple

import requests

# ==================================================================================================

API = os.getenv("GITHUB_API_URL", "https://api.github.com")
TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
TARGET_BRANCH = os.environ.get("TARGET_BRANCH", "github")
TARGET_FOLDER = os.environ.get("TARGET_FOLDER", "dataset/benchmarks/").rstrip("/")
REQUIRED_CHECK = os.environ.get("REQUIRED_CHECK", "validate_data / validate")
MERGE_METHOD = os.environ.get("MERGE_METHOD", "merge")  # merge | squash | rebase
MIN_THUMBS_UP = int(os.environ.get("MIN_THUMBS_UP", "2"))
MAX_CHANGED_FILES = int(os.environ.get("MAX_CHANGED_FILES", "20"))
MIN_VOTER_ACCOUNT_AGE_DAYS = int(os.environ.get("MIN_VOTER_ACCOUNT_AGE_DAYS", "365"))

# One page of the files endpoint holds up to 100 files, more than we ever accept
FILES_PER_PAGE = 100

session = requests.Session()
session.headers.update(
    {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
)

_account_created: Dict[str, datetime] = {}

# ==================================================================================================


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


# ==================================================================================================


def get_json(url: str, params: Optional[Dict[str, Any]] = None) -> Any:
    r = session.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def get_all(
    url: str, params: Optional[Dict[str, Any]] = None, key: Optional[str] = None
) -> List[Any]:
    """Fetch all pages of a list endpoint. Use 'key' if the list is wrapped in an object."""

    items: List[Any] = []
    query: Optional[Dict[str, Any]] = {"per_page": 100, **(params or {})}
    next_url: Optional[str] = url
    while next_url:
        r = session.get(next_url, params=query, timeout=30)
        r.raise_for_status()
        data = r.json()
        items.extend(data[key] if key else data)
        next_url = r.links.get("next", {}).get("url")
        # The next-url already contains the query parameters
        query = None
    return items


# ==================================================================================================


def only_in_folder(files: List[Dict[str, Any]], folder: str) -> bool:
    if not folder:
        return True
    prefix = folder.rstrip("/") + "/"
    for f in files:
        # A renamed file has both a new and a previous path, both have to be inside the folder
        for key in ("filename", "previous_filename"):
            p = f.get(key)
            if p and not p.startswith(prefix):
                return False
    return True


def is_data_only(number: int, details: Dict[str, Any]) -> bool:
    """Small enough and only touching the data folder."""

    changed = details.get("changed_files")
    if not isinstance(changed, int) or changed > MAX_CHANGED_FILES:
        print(
            f"Skip #{number}: more than {MAX_CHANGED_FILES} files, needs manual merge"
        )
        return False

    # A single page is enough, the number of files is already limited above
    files = get_json(
        f"{API}/repos/{REPO}/pulls/{number}/files", {"per_page": FILES_PER_PAGE}
    )
    if len(files) != changed:
        print(f"Skip #{number}: file list does not match the number of changed files")
        return False
    return only_in_folder(files, TARGET_FOLDER)


# ==================================================================================================


def required_check_state(sha: str) -> Tuple[bool, Optional[datetime]]:
    """Return if the latest run of the required check succeeded, and when it was first started.

    The start time of the first run for this commit is used as the point in time after which
    votes count. It comes from the GitHub server and cannot be set by the pull request author.
    """

    runs = get_all(
        f"{API}/repos/{REPO}/commits/{sha}/check-runs",
        {"check_name": REQUIRED_CHECK, "filter": "all"},
        key="check_runs",
    )
    # Only trust check runs created by GitHub Actions itself
    runs = [
        r
        for r in runs
        if (r.get("app") or {}).get("slug") == "github-actions" and r.get("started_at")
    ]
    if not runs:
        return False, None

    runs.sort(key=lambda r: r["started_at"])
    first_started = parse_time(runs[0]["started_at"])
    latest = runs[-1]
    ok = latest.get("status") == "completed" and latest.get("conclusion") == "success"
    return ok, first_started


# ==================================================================================================


def voter_old_enough(login: str) -> bool:
    if MIN_VOTER_ACCOUNT_AGE_DAYS <= 0:
        return True
    if login not in _account_created:
        data = get_json(f"{API}/users/{login}")
        _account_created[login] = parse_time(data["created_at"])
    age = datetime.now(timezone.utc) - _account_created[login]
    return age >= timedelta(days=MIN_VOTER_ACCOUNT_AGE_DAYS)


def thumbs_summary(number: int, author_id: int, since: datetime) -> Dict[str, int]:
    """Count thumbs up (only newer than 'since') and thumbs down (always, as a veto)."""

    pos: Set[int] = set()
    neg: Set[int] = set()
    # This endpoint only lists reactions of the pull request itself, not of its comments
    for rx in get_all(f"{API}/repos/{REPO}/issues/{number}/reactions"):
        user = rx.get("user") or {}
        uid = user.get("id")
        if uid is None or uid == author_id or user.get("type") == "Bot":
            continue
        if not voter_old_enough(user.get("login", "")):
            continue

        content = rx.get("content")
        if content == "-1":
            neg.add(uid)
        elif content == "+1" and parse_time(rx["created_at"]) > since:
            pos.add(uid)

    return {"pos": len(pos), "neg": len(neg)}


def is_approved(number: int, details: Dict[str, Any]) -> Optional[str]:
    """Return the head sha if check and votes are fine, else None."""

    sha = (details.get("head") or {}).get("sha")
    if not sha:
        print(f"Skip #{number}: missing head sha", file=sys.stderr)
        return None

    check_ok, since = required_check_state(sha)
    if not check_ok or since is None:
        print(f"Skip #{number}: check '{REQUIRED_CHECK}' not successful")
        return None

    author_id = (details.get("user") or {}).get("id") or -1
    thumbs = thumbs_summary(number, author_id, since)
    print(f'PR #{number}: {{"pos": {thumbs["pos"]}, "neg": {thumbs["neg"]}}}')
    if thumbs["neg"] > 0 or thumbs["pos"] < MIN_THUMBS_UP:
        return None
    return sha


# ==================================================================================================


def try_merge(number: int, sha: str, message: str) -> bool:
    # The sha makes the merge fail if the pull request got a new commit in the meantime
    payload = {"sha": sha, "merge_method": MERGE_METHOD, "commit_title": message}
    r = session.put(
        f"{API}/repos/{REPO}/pulls/{number}/merge", json=payload, timeout=60
    )

    if r.ok:
        print(f"Merged PR #{number}")
        return True
    print(f"Merge failed for #{number}: {r.status_code} {r.text}", file=sys.stderr)
    return False


# ==================================================================================================


def main() -> int:

    open_prs = get_all(
        f"{API}/repos/{REPO}/pulls", {"state": "open", "base": TARGET_BRANCH}
    )
    print(f"Found {len(open_prs)} open pull requests for branch '{TARGET_BRANCH}'.")

    for pr in open_prs:
        if pr.get("draft"):
            continue
        number = pr["number"]
        details = get_json(f"{API}/repos/{REPO}/pulls/{number}")

        if not is_data_only(number, details):
            continue
        sha = is_approved(number, details)
        if sha is None:
            continue

        try_merge(number, sha, f"Auto-merged #{number} by CI bot.")

    return 0


# ==================================================================================================

if __name__ == "__main__":
    sys.exit(main())
