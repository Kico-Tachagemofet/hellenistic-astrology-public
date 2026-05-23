"""
Hellenistic Reader Render — MD → HTML Pipeline
================================================
Reader-layer 渲染合并工具. 扫 charts/case-NN/reader/NN-<slug>.md 系列,
按数字前缀排序合并成单 HTML.

Usage:
  python report_builder.py <case_folder> [--name "Name"] [--asc "Leo 8°25"]
                                          [--lang cn] [--include character,family,...]

Layout:
  charts/case-NN/reader/
    ├── 00-overview.md
    ├── 01-character.md
    ├── 02-career.md
    ├── 03-wealth.md
    ├── 04-partnership-marriage.md
    ├── 05-family.md
    ├── 06-learning.md
    ├── 07-divination-spirituality.md
    ├── 08-body.md
    ├── 09-children.md             (optional)
    ├── 10-siblings.md             (optional)
    ├── 11-friends-benefactors.md
    ├── 12-illness.md              (optional)
    ├── 13-death.md                (optional)
    ├── 14-longevity.md            (optional)
    ├── 15-chart-signature.md
    ├── 16-timing.md
    └── 99-citation.md             (optional, 整盘 trailing technical 集中)

  自定义 topic 用 20+ 前缀: 20-synastry-with-XX.md, 21-transit-snapshot-YYYY.md

--include 可指定只合并某些 topic (按 slug 匹配, 不带数字前缀):
  --include character,family,career
  默认: 全合并 reader/ 下所有 NN-*.md

Requirements:  pip install markdown
"""

import os
import sys
import re
import glob
import argparse
from pathlib import Path

try:
    import markdown
except ImportError:
    print("ERROR: markdown library not installed. Run: pip install markdown")
    sys.exit(1)


# --- file discovery ---------------------------------------------------------

FILENAME_PATTERN = re.compile(r"^(\d{2})-(.+)\.md$")


def discover_reader_files(case_folder, include_slugs=None):
    """
    Scan case_folder/reader/ for NN-<slug>.md files, return sorted by numeric
    prefix. If include_slugs given (list of slugs without prefix), filter.
    """
    reader_dir = os.path.join(case_folder, "reader")
    if not os.path.isdir(reader_dir):
        return []

    candidates = []
    for fname in os.listdir(reader_dir):
        m = FILENAME_PATTERN.match(fname)
        if not m:
            continue
        prefix, slug = m.group(1), m.group(2)
        if include_slugs is not None and slug not in include_slugs:
            continue
        full = os.path.join(reader_dir, fname)
        candidates.append((int(prefix), slug, full))

    candidates.sort(key=lambda t: t[0])
    return candidates


# --- slug → display title ---------------------------------------------------

SLUG_TITLES_CN = {
    "overview": "整盘开场",
    "character": "性格",
    "career": "事业",
    "wealth": "财富",
    "partnership-marriage": "感情 / 伴侣",
    "family": "家庭",
    "learning": "学习",
    "divination-spirituality": "灵性 / 求知",
    "body": "身体",
    "children": "子女",
    "siblings": "兄弟姐妹",
    "friends-benefactors": "朋友 / 贵人",
    "illness": "疾病",
    "death": "死亡",
    "longevity": "寿命",
    "chart-signature": "整盘签名",
    "timing": "关键时机",
    "citation": "技术依据",
}

SLUG_TITLES_EN = {
    "overview": "Overview",
    "character": "Character",
    "career": "Career",
    "wealth": "Wealth",
    "partnership-marriage": "Partnership / Marriage",
    "family": "Family",
    "learning": "Learning",
    "divination-spirituality": "Spirituality / Divination",
    "body": "Body",
    "children": "Children",
    "siblings": "Siblings",
    "friends-benefactors": "Friends / Benefactors",
    "illness": "Illness",
    "death": "Death",
    "longevity": "Longevity",
    "chart-signature": "Chart Signature",
    "timing": "Timing",
    "citation": "Citations",
}


def slug_to_title(slug, lang):
    table = SLUG_TITLES_CN if lang == "cn" else SLUG_TITLES_EN
    return table.get(slug, slug.replace("-", " ").title())


# --- markdown rendering ------------------------------------------------------

def read_md(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def md_to_html(md_text):
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "sane_lists", "nl2br"],
    )


def build_section_html(prefix, slug, filepath, lang):
    title = slug_to_title(slug, lang)
    md_text = read_md(filepath)
    html_body = md_to_html(md_text)
    section_id = f"sec-{prefix:02d}-{slug}"
    return f"""<section id="{section_id}" class="section">
<h2 class="section-title">{title}</h2>
<article class="file-body">{html_body}</article>
</section>"""


# --- HTML scaffolding --------------------------------------------------------

CSS = """
:root {
  --fg: #1a1a1a;
  --muted: #666;
  --bg: #fafaf7;
  --card-bg: #fff;
  --border: #e3e0d8;
  --accent: #6b4d2e;
  --code-bg: #f0ede5;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
    "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  line-height: 1.75;
  color: var(--fg);
  background: var(--bg);
  margin: 0;
  padding: 0;
  font-size: 16px;
}
header.page-header {
  background: var(--accent);
  color: #fff;
  padding: 2rem 1.5rem;
  text-align: center;
}
header.page-header h1 { margin: 0; font-weight: 600; font-size: 1.6rem; }
header.page-header .meta {
  margin-top: 0.6rem; opacity: 0.85; font-size: 0.95rem;
}
nav.toc {
  position: sticky; top: 0;
  background: rgba(255,255,255,0.95);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
  padding: 0.6rem 1rem;
  font-size: 0.88rem;
  z-index: 10;
  overflow-x: auto;
  white-space: nowrap;
}
nav.toc a {
  color: var(--accent); text-decoration: none;
  margin-right: 0.6rem; padding: 0.2rem 0.4rem;
  border-radius: 3px;
  display: inline-block;
}
nav.toc a:hover { background: var(--code-bg); }
main {
  max-width: 760px;
  margin: 0 auto;
  padding: 1.5rem;
}
section.section {
  margin-bottom: 3rem;
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 1.5rem 1.8rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.section-title {
  font-size: 1.5rem;
  color: var(--accent);
  border-bottom: 2px solid var(--accent);
  padding-bottom: 0.4rem;
  margin-top: 0;
  margin-bottom: 1rem;
}
.file-body h1, .file-body h2, .file-body h3, .file-body h4 {
  color: var(--accent);
  margin-top: 1.4rem;
  margin-bottom: 0.5rem;
}
.file-body h1 { font-size: 1.3rem; }
.file-body h2 { font-size: 1.15rem; }
.file-body h3 { font-size: 1.05rem; }
.file-body h4 { font-size: 1.0rem; }
.file-body p {
  margin: 0.9rem 0;
}
.file-body strong {
  color: var(--accent);
}
.file-body table {
  border-collapse: collapse;
  width: 100%;
  margin: 1rem 0;
  font-size: 0.92rem;
}
.file-body table th, .file-body table td {
  border: 1px solid var(--border);
  padding: 0.5rem 0.7rem;
  text-align: left;
}
.file-body table th {
  background: var(--code-bg);
  font-weight: 600;
}
.file-body code {
  background: var(--code-bg);
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-size: 0.88em;
  font-family: "SF Mono", Consolas, monospace;
}
.file-body pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 0.8rem;
  overflow-x: auto;
  font-size: 0.85rem;
}
.file-body pre code { background: none; padding: 0; }
.file-body blockquote {
  border-left: 3px solid var(--accent);
  margin: 1rem 0;
  padding: 0.4rem 1rem;
  background: var(--code-bg);
  color: var(--fg);
}
.file-body ul, .file-body ol { padding-left: 1.5rem; }
.file-body hr {
  border: none;
  border-top: 1px dashed var(--border);
  margin: 1.5rem 0;
}
footer.page-footer {
  text-align: center;
  padding: 2rem 1rem;
  color: var(--muted);
  font-size: 0.85rem;
  border-top: 1px solid var(--border);
  margin-top: 3rem;
}
@media (max-width: 600px) {
  main { padding: 0.8rem; }
  section.section { padding: 1.1rem 1.2rem; }
  header.page-header h1 { font-size: 1.3rem; }
}
@media (prefers-color-scheme: dark) {
  :root {
    --fg: #e0ddd5;
    --muted: #9a9590;
    --bg: #1a1916;
    --card-bg: #242320;
    --border: #3a3830;
    --accent: #c9a87c;
    --code-bg: #2a2820;
  }
  header.page-header { background: #3d3020; }
  nav.toc { background: rgba(26,25,22,0.95); }
}
"""


def build_full_html(name, asc, lang, sections):
    title_label = "Hellenistic 占星报告" if lang == "cn" else "Hellenistic Astrology Report"
    asc_meta = f" — Asc {asc}" if asc else ""

    toc_links = []
    for prefix, slug, _ in sections:
        title = slug_to_title(slug, lang)
        section_id = f"sec-{prefix:02d}-{slug}"
        toc_links.append(f'<a href="#{section_id}">{title}</a>')
    toc_html = "".join(toc_links)

    body_parts = []
    for prefix, slug, fp in sections:
        body_parts.append(build_section_html(prefix, slug, fp, lang))
    body_html = "\n".join(body_parts)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_label} — {name}</title>
<style>{CSS}</style>
</head>
<body>
<header class="page-header">
  <h1>{title_label}</h1>
  <div class="meta">{name}{asc_meta}</div>
</header>
<nav class="toc">{toc_html}</nav>
<main>
{body_html}
</main>
<footer class="page-footer">
  Generated by hellenistic-render-unguarded · scripts/report_builder.py
</footer>
</body>
</html>"""


# --- main --------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Hellenistic Reader Render — merge case-folder reader/ MD files into HTML.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("case_folder", help="Path to the case folder (e.g., charts/case-10/)")
    parser.add_argument("--name", default=None, help="Subject name for header (default: folder name)")
    parser.add_argument("--asc", default=None, help="Asc display string (e.g., 'Leo 8°25')")
    parser.add_argument("--lang", default="cn", choices=["cn", "en"], help="UI language (default: cn)")
    parser.add_argument(
        "--include",
        default=None,
        help="Comma-separated slugs to include (without numeric prefix). Default: all NN-*.md in reader/",
    )
    parser.add_argument("--out", default=None, help="Output HTML path (default: <case_folder>/report.html)")
    args = parser.parse_args()

    case_folder = os.path.abspath(args.case_folder)
    if not os.path.isdir(case_folder):
        print(f"ERROR: not a directory: {case_folder}")
        sys.exit(1)

    include_slugs = None
    if args.include:
        include_slugs = [s.strip() for s in args.include.split(",") if s.strip()]

    sections = discover_reader_files(case_folder, include_slugs=include_slugs)
    if not sections:
        print(f"ERROR: no reader/NN-*.md files found in {case_folder}/reader/")
        if include_slugs:
            print(f"  (filtered by --include={args.include})")
        sys.exit(1)

    print(f"Found {len(sections)} reader file(s):")
    for prefix, slug, fp in sections:
        rel = os.path.relpath(fp, case_folder)
        print(f"  [{prefix:02d}] {slug} — {rel}")

    name = args.name or os.path.basename(case_folder.rstrip("/").rstrip("\\"))
    full_html = build_full_html(name, args.asc, args.lang, sections)

    out_path = args.out or os.path.join(case_folder, "report.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"\nDone. Wrote {out_path} ({size_kb:.1f} KB, {len(sections)} sections).")


if __name__ == "__main__":
    main()
