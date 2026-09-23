import os
import re
from functools import lru_cache

# ==================================================================================================

# Maximum length of a generated paper slug, to keep file names sane
MAX_SLUG_LENGTH = 120

# The HTML templates and snippets the pages are built from
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

# ==================================================================================================


@lru_cache(maxsize=None)
def load_template(name: str) -> str:
    """Load an HTML template or snippet from the templates folder."""

    path = os.path.join(TEMPLATE_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ==================================================================================================


def paper_slug(name: str, link: str) -> str:
    """Build the file name (without extension) of the paper page.

    Papers are identified by their name, so that the different publication versions of
    one paper (preprint, proceedings, ...) end up on a single page. Papers without a
    name fall back to their link.
    """

    base = (name or "").strip() or (link or "").strip()
    if not base:
        return ""

    # Keep the '+' of names like 'MS-TCN++', else it would clash with the base paper
    base = base.replace("+", "p")

    base = base.replace("/", "--")
    base = re.sub(r"[^A-Za-z0-9]", "-", base)
    base = re.sub(r"-+", "-", base)
    return base.lower().strip("-")[:MAX_SLUG_LENGTH]
