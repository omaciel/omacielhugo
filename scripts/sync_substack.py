#!/usr/bin/env python3
"""
Sync new Substack posts into this Hugo mirror.

Flow:
  1. Scan content/posts/ to find the most recent YYYY-MM-DD-*.md filename.
  2. Fetch https://ogmaciel.substack.com/api/v1/archive and pick every public
     post with a post_date strictly after that date.
  3. For each new post, fetch the post page, download embedded images into
     content/images/ (renamed as <slug>-NN.<ext>), convert the article body
     from HTML to Markdown, and write content/posts/YYYY-MM-DD-<slug>.md
     with Hugo-style frontmatter matching the existing mirror posts.

Usage (from the repo root):
    pip install requests beautifulsoup4 markdownify
    python3 sync_substack.py                 # dry-run preview
    python3 sync_substack.py --write         # actually write files
    python3 sync_substack.py --since 2026-01-08 --write
    python3 sync_substack.py --only <slug> --write

The script is idempotent: existing files under content/posts/ and
content/images/ are never overwritten.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as html_to_md
except ImportError:
    sys.exit(
        "Missing deps. Install with:\n"
        "    pip install requests beautifulsoup4 markdownify"
    )

SUBSTACK_BASE = "https://ogmaciel.substack.com"
ARCHIVE_API = f"{SUBSTACK_BASE}/api/v1/archive"
POSTS_DIR = Path("content/posts")
IMAGES_DIR = Path("content/images")
DEFAULT_AUTHOR = "Og Maciel"
UA = "Mozilla/5.0 (compatible; omacielhugo-sync/1.0)"
VALID_IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic", ".avif", ".svg"}


# ---------- helpers ---------------------------------------------------------


def find_latest_repo_date() -> dt.date:
    pat = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-")
    latest = dt.date(1970, 1, 1)
    if not POSTS_DIR.exists():
        return latest
    for p in POSTS_DIR.glob("*.md"):
        m = pat.match(p.name)
        if not m:
            continue
        d = dt.date(int(m[1]), int(m[2]), int(m[3]))
        if d > latest:
            latest = d
    return latest


def parse_post_date(iso: str) -> dt.date:
    return dt.date.fromisoformat(iso[:10])


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[\u2018\u2019\u201C\u201D]", "", s)  # smart quotes
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


# ---------- Substack fetchers ----------------------------------------------


def fetch_archive() -> list[dict]:
    out: list[dict] = []
    offset, limit = 0, 50
    while True:
        r = requests.get(
            ARCHIVE_API,
            params={"sort": "new", "search": "", "offset": offset, "limit": limit},
            headers={"User-Agent": UA},
            timeout=30,
        )
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        out.extend(batch)
        if len(batch) < limit:
            break
        offset += limit
    return out


def fetch_post_html(slug: str) -> str:
    r = requests.get(
        f"{SUBSTACK_BASE}/p/{slug}", headers={"User-Agent": UA}, timeout=60
    )
    r.raise_for_status()
    return r.text


# ---------- article parsing ------------------------------------------------


def extract_article(html: str):
    """Return (article_node, subtitle_text)."""
    soup = BeautifulSoup(html, "html.parser")
    # Substack renders the main body inside .available-content > .body.markup
    body = soup.select_one("div.available-content div.body.markup")
    if body is None:
        body = soup.select_one("div.available-content") or soup.find("article") or soup
    subtitle_el = soup.select_one("h3.subtitle") or soup.find(
        attrs={"class": re.compile(r"subtitle")}
    )
    subtitle = subtitle_el.get_text(strip=True) if subtitle_el else ""
    return body, subtitle


def _guess_ext(resp, url: str) -> str:
    ct = (resp.headers.get("Content-Type") or "").lower()
    for frag, ext in (
        ("webp", ".webp"),
        ("png", ".png"),
        ("jpeg", ".jpg"),
        ("jpg", ".jpg"),
        ("gif", ".gif"),
        ("heic", ".heic"),
        ("avif", ".avif"),
        ("svg", ".svg"),
    ):
        if frag in ct:
            return ext
    path_ext = os.path.splitext(urlparse(url).path)[1].lower()
    if path_ext in VALID_IMG_EXTS:
        return path_ext
    # Substack wraps remote URLs as .../fetch/.../<pct-encoded URL>
    m = re.search(r"https?%3A%2F%2F[^/?#]+(%2F[^?#]+)", url)
    if m:
        inner = unquote(m.group(0))
        inner_ext = os.path.splitext(urlparse(inner).path)[1].lower()
        if inner_ext in VALID_IMG_EXTS:
            return inner_ext
    return ".png"


def download_images(article, slug: str) -> dict[str, str]:
    """Download every <img> in the article, save as <slug>-NN.<ext> under
    content/images/, and return {original_src: "/images/<name>"}."""
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, str] = {}
    seen_srcs: list[str] = []
    idx = 0
    for img in article.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        if not src or src in seen_srcs:
            continue
        seen_srcs.append(src)
        idx += 1
        try:
            r = requests.get(src, headers={"User-Agent": UA}, timeout=60)
            r.raise_for_status()
        except Exception as e:
            print(f"    ! image fetch failed for {src}: {e}", file=sys.stderr)
            continue
        ext = _guess_ext(r, src)
        local_name = f"{slug}-{idx:02d}{ext}"
        local_path = IMAGES_DIR / local_name
        if not local_path.exists():
            local_path.write_bytes(r.content)
            print(f"    img -> {local_path}")
        mapping[src] = f"/images/{local_name}"
    return mapping


def rewrite_images(article, mapping: dict[str, str]) -> None:
    for img in article.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        if src in mapping:
            img["src"] = mapping[src]
        # strip remote-variant metadata so markdown stays clean
        for attr in ("srcset", "data-src", "data-srcset", "sizes", "loading"):
            img.attrs.pop(attr, None)


def to_markdown(article) -> str:
    # Drop picture wrappers so markdownify sees the bare <img>
    for picture in article.find_all("picture"):
        img = picture.find("img")
        if img is not None:
            picture.replace_with(img)
    return html_to_md(
        str(article),
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    ).strip()


# ---------- output writer --------------------------------------------------


def write_post(meta: dict, subtitle: str, body_md: str) -> Path:
    slug = slugify(meta["title"])
    date = parse_post_date(meta["post_date"])
    out = POSTS_DIR / f"{date.isoformat()}-{slug}.md"
    if out.exists():
        print(f"  = exists, skipping: {out}")
        return out

    desc_raw = (meta.get("description") or meta.get("subtitle") or subtitle or "").strip()
    desc = desc_raw.replace("\\", "\\\\").replace('"', '\\"')

    fm = [
        "---",
        "author:",
        f"- {DEFAULT_AUTHOR}",
        f"date: {date.isoformat()}",
        f'description: "{desc}"',
        f'title: "{meta["title"]}"',
        "tags:",
        " - substack",
        "type: post",
        "---",
        "",
        f"# {meta['title']}",
        "",
    ]
    if subtitle and subtitle.lower() != meta["title"].lower():
        fm += [f"## {subtitle}", ""]
    fm.append(body_md)
    out.write_text("\n".join(fm) + "\n", encoding="utf-8")
    return out


# ---------- main -----------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--since",
        help="Only import posts strictly after this date (YYYY-MM-DD). "
             "Default: the latest date found in content/posts/.",
    )
    ap.add_argument(
        "--only",
        help="Only import the single post with this exact slug (debug).",
    )
    ap.add_argument(
        "--write",
        action="store_true",
        help="Actually write files. Without this flag the script just previews.",
    )
    args = ap.parse_args()

    if not POSTS_DIR.exists():
        print(f"error: {POSTS_DIR} not found — run this from the repo root.", file=sys.stderr)
        return 2

    since = dt.date.fromisoformat(args.since) if args.since else find_latest_repo_date()
    print(f"Latest post in repo: {since.isoformat()}")
    print(f"Fetching archive from {SUBSTACK_BASE} ...")
    archive = fetch_archive()
    print(f"  archive has {len(archive)} post(s)")

    if args.only:
        candidates = [p for p in archive if p.get("slug") == args.only]
    else:
        candidates = [p for p in archive if parse_post_date(p["post_date"]) > since]

    candidates.sort(key=lambda p: parse_post_date(p["post_date"]))
    print(f"New posts to import: {len(candidates)}")
    for p in candidates:
        print(f"  - {parse_post_date(p['post_date']).isoformat()}  {p['title']}  "
              f"(slug={p.get('slug')})")

    if not args.write:
        print("\n(dry-run) pass --write to actually create files.")
        return 0

    for meta in candidates:
        print(f"\n==> {meta['title']}")
        try:
            html = fetch_post_html(meta["slug"])
        except Exception as e:
            print(f"  ! fetch failed: {e}", file=sys.stderr)
            continue
        article, subtitle = extract_article(html)
        if article is None:
            print("  ! could not find article body, skipping", file=sys.stderr)
            continue
        slug = slugify(meta["title"])
        mapping = download_images(article, slug)
        rewrite_images(article, mapping)
        body_md = to_markdown(article)
        path = write_post(meta, subtitle, body_md)
        print(f"  wrote {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
