import argparse
import os
import re

# ==================================================================================================

HTML_SCAFFOLD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>OpenCodePapers</title>
<style>
  :root {
    --bg: #ffffff;
    --text: #111827;
    --muted: #4b5563;
    --border: #e5e7eb;
    --accent: #2563eb;
    --accent-weak: #dbeafe;
    --chip: #f3f4f6;
    --hover: #f9fafb;
  }
  html, body {
    background: var(--bg);
    color: var(--text);
    margin: 0;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
  }
  .wrap { max-width: 1100px; margin: 28px auto; padding: 0 16px 48px; }
  .hero {
    background: linear-gradient(135deg, #2563eb, #9333ea);
    color: white;
    padding: 60px 20px;
    text-align: center;
  }
  .hero-inner {
    max-width: 800px;
    margin: 0 auto;
  }
  .hero-title {
    font-size: 40px;
    margin: 0 0 12px;
    font-weight: 700;
  }
  .hero-sub {
    font-size: 18px;
    color: #e0e7ff;
    margin: 0;
  }
  header.sticky {
    position: sticky; top: 0; z-index: 50;
    background: rgba(255,255,255,0.9); backdrop-filter: saturate(1.1) blur(6px);
    border-bottom: 1px solid var(--border);
  }
  header .inner { max-width: 1100px; margin: 0 auto; padding: 10px 16px; display: grid; grid-template-columns: 1fr auto; gap: 12px; align-items: center;}
  h1 { font-size: 24px; margin: 0; }
  .controls { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
  .btn {
    border: 1px solid var(--border); background: white; color: var(--text);
    padding: 8px 10px; border-radius: 8px; font-size: 14px; cursor: pointer;
  }
  .btn:hover { background: var(--hover); }
  .btn.primary { border-color: var(--accent); background: var(--accent); color: white; }
  .search {
    display: flex; gap: 8px; align-items: center; margin: 10px 0 0;
  }
  .search input[type="search"]{
    width: 100%; font-size: 14px; padding: 10px 12px; border: 1px solid var(--border);
    border-radius: 10px; outline: none;
  }
  .search input[type="search"]:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-weak); }
  .stats { color: var(--muted); font-size: 12px; }
  /* Tree styling */
  .tree { margin-top: 16px; }
  details { border: 1px solid var(--border); border-radius: 10px; padding: 6px 10px; background: white; }
  details + details { margin-top: 8px; }
  details > summary {
    list-style: none; cursor: pointer; font-weight: 600; display: flex; align-items: center; gap: 8px;
  }
  details > summary::-webkit-details-marker { display: none; }
  .caret { width: 0; height: 0; border-top: 5px solid transparent; border-bottom: 5px solid transparent; border-left: 7px solid var(--muted); transition: transform .15s ease; }
  details[open] > summary .caret { transform: rotate(90deg); }
  summary .badge {
    background: var(--chip); border: 1px solid var(--border); color: var(--muted);
    font-size: 12px; padding: 2px 6px; border-radius: 999px;
  }
  details > div { margin-top: 8px; padding-left: 14px; }
  /* Nested details indentation */
  details details { margin-top: 8px; }
  details details > summary { font-weight: 600; }
  /* Lists */
  ul { margin: 8px 0; padding-left: 18px; }
  li { margin: 4px 0; }
  a { color: var(--accent); text-decoration: none; }
  a:hover { text-decoration: underline; }
  /* Filtered (hidden) nodes */
  .hidden { display: none !important; }
  /* Hit highlight */
  mark { background: #fff3a3; padding: 0 2px; }
  /* Footer */
  .footer-note { color: var(--muted); font-size: 12px; margin-top: 16px; }
</style>
</head>
<body>
<section class="hero">
  <div class="hero-inner">
    <h1 class="hero-title">OpenCodePapers</h1>
    <p class="hero-sub">A collection of benchmark results and code links from many research papers.</p>
  </div>
</section>
<header class="sticky">
  <div class="inner">
    <h1>Tasks</h1>
    <div class="controls">
      <button class="btn" id="expand-all">Expand all</button>
      <button class="btn" id="collapse-all">Collapse all</button>
    </div>
    <div class="search" style="grid-column: 1 / -1;">
      <input id="q" type="search" placeholder="Filter tasks… (e.g., ‘pose estimation’ or ‘coco’)">
      <span class="stats" id="stats"></span>
    </div>
  </div>
</header>

<div class="wrap">
  <div id="tree" class="tree">
    <!--TREE-->
  </div>
  <div class="footer-note">Tip: Use the search box to filter categories and leaf pages. Matching parents auto-open.</div>
</div>

<script>
(function(){
  const tree = document.getElementById('tree');
  const stats = document.getElementById('stats');
  const inp = document.getElementById('q');
  const BTN_EXPAND_ALL = document.getElementById('expand-all');
  const BTN_COLLAPSE_ALL = document.getElementById('collapse-all');

  // Add carets + badges
  const summaries = tree.querySelectorAll('summary');
  summaries.forEach(sm => {
    const caret = document.createElement('span');
    caret.className = 'caret';
    sm.prepend(caret);
  });

  // Count descendant links for each <details> once
  function computeCounts() {
    tree.querySelectorAll('details').forEach(d => {
      const n = d.querySelectorAll('a').length;
      const sm = d.querySelector(':scope > summary');
      if (!sm) return;
      const badge = document.createElement('span');
      badge.className = 'badge';
      badge.textContent = n;
      sm.appendChild(badge);
    });
    updateStats();
  }

  function updateStats(visibleOnly=true) {
    const allLinks = tree.querySelectorAll('a');
    let visible = 0;
    allLinks.forEach(a => {
      if (visibleOnly) {
        // visible if itself and all ancestors are not hidden
        let el = a;
        let ok = true;
        while (el && el !== tree) {
          if (el.classList && el.classList.contains('hidden')) { ok = false; break; }
          el = el.parentElement;
        }
        if (ok) visible++;
      } else {
        visible++;
      }
    });
    stats.textContent = visible + ' items';
  }

  // Expanders
  BTN_EXPAND_ALL.addEventListener('click', () => {
    tree.querySelectorAll('details').forEach(d => d.open = true);
  });
  BTN_COLLAPSE_ALL.addEventListener('click', () => {
    tree.querySelectorAll('details').forEach(d => d.open = false);
  });

  // Simple debounce
  let t = 0;
  inp.addEventListener('input', () => {
    clearTimeout(t);
    t = setTimeout(() => applyFilter(inp.value.trim().toLowerCase()), 150);
  });

  function clearHighlights() {
    tree.querySelectorAll('mark').forEach(m => {
      const parent = m.parentNode;
      parent.replaceChild(document.createTextNode(m.textContent), m);
      parent.normalize();
    });
  }

  function highlight(el, q) {
    if (!q) return;
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
    const texts = [];
    while (walker.nextNode()) { texts.push(walker.currentNode); }
    texts.forEach(node => {
      const idx = node.nodeValue.toLowerCase().indexOf(q);
      if (idx >= 0) {
        const span = document.createElement('span');
        const before = node.nodeValue.slice(0, idx);
        const hit = node.nodeValue.slice(idx, idx + q.length);
        const after = node.nodeValue.slice(idx + q.length);
        span.innerHTML = (before ? before.replace(/&/g,'&amp;').replace(/</g,'&lt;') : '') +
                         '<mark>' + hit.replace(/&/g,'&amp;').replace(/</g,'&lt;') + '</mark>' +
                         (after ? after.replace(/&/g,'&amp;').replace(/</g,'&lt;') : '');
        node.parentNode.replaceChild(span, node);
      }
    });
  }

  function applyFilter(q) {
    clearHighlights();
    // Fast path: empty query shows everything collapsed
    if (!q) {
      tree.querySelectorAll('.hidden').forEach(el => el.classList.remove('hidden'));
      BTN_COLLAPSE_ALL.click();
      updateStats();
      return;
    }
    // hide everything first
    tree.querySelectorAll('li, details').forEach(el => el.classList.add('hidden'));
    tree.querySelectorAll('details').forEach(d => d.open = false);

    // show matching links and open their ancestor details
    const links = tree.querySelectorAll('a');
    const qParts = q.split(/\s+/).filter(Boolean);
    links.forEach(a => {
      const text = a.textContent.toLowerCase();
      const ok = qParts.every(part => text.includes(part));
      if (ok) {
        // highlight
        highlight(a, q);
        // unhide the <li>
        const li = a.closest('li');
        if (li) li.classList.remove('hidden');
        // open/unhide all ancestor <details> and their summaries
        let p = a.parentElement;
        while (p && p !== tree) {
          if (p.tagName === 'DETAILS') {
            p.classList.remove('hidden');
            p.open = true;
          }
          if (p.tagName === 'LI') p.classList.remove('hidden');
          p = p.parentElement;
        }
      }
    });
    // keep visible summaries' immediate <summary> also unhidden
    tree.querySelectorAll('details').forEach(d => {
      if (!d.classList.contains('hidden') && d.open) {
        const sm = d.querySelector(':scope > summary');
        if (sm) sm.classList.remove('hidden');
      }
    });
    updateStats();
  }

  computeCounts();
  BTN_COLLAPSE_ALL.click();
})();
</script>
</body>
</html>
"""

MD_TO_HTML_HREF = re.compile(r'href="([^"]+?)\.md(\#[^"]*)?"', re.IGNORECASE)

# ==================================================================================================


def rewrite_md_links_to_html(s: str) -> str:
    def _rep(m):
        path = m.group(1)
        frag = m.group(2) or ""
        return f'href="{path}.html{frag}" target="_blank" rel="noopener noreferrer"'

    return MD_TO_HTML_HREF.sub(_rep, s)


# ==================================================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Build a light-themed tasks landing page from tasks.md"
    )
    parser.add_argument("--input", "-i", default="dataset/tasks.md")
    parser.add_argument("--output", "-o", default="public/index.html")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        raise SystemExit(f"Not found: {args.input}")

    with open(args.input, "r", encoding="utf-8") as f:
        content = f.read()

    # If tasks.md is Markdown, it already contains raw HTML; take as-is
    # Just ensure all benchmark links point to generated .html pages
    content = rewrite_md_links_to_html(content)

    html = HTML_SCAFFOLD.replace("<!--TREE-->", content)

    out_dir = os.path.dirname(os.path.abspath(args.output))
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)


# ==================================================================================================

if __name__ == "__main__":
    main()
