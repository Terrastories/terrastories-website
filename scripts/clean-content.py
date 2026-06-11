#!/usr/bin/env python3
"""Clean WordPress content for Astro migration.

Handles:
1. Unescape backslash-escaped markdown
2. Decode HTML entities to UTF-8
3. Strip WordPress read-more HTML from excerpt
4. Map absolute featured_image/og_image URLs to local paths
5. Rewrite internal terrastories.app links to relative
6. Remove empty heading markers
7. Deduplicate WordPress thumbnail media files

Usage:
    python scripts/clean-content.py --dry-run   # preview only
    python scripts/clean-content.py --write      # modify files
"""

import argparse
import html
import re
import sys
import urllib.parse
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE / "content"
IMAGES_DIR = BASE / "static" / "media" / "images"

# --- Shared Parsing ---

FRONTMATTER_RE = re.compile(r"\A---\n(?P<frontmatter>.*?)\n---\n(?P<body>.*)\Z", re.S)

# --- Task 1: Unescape Markdown ---

ESCAPED_MARKDOWN_RE = re.compile(r"\\([\\`*_{}\[\]()<>#+\-.!|])")

FENCE_RE = re.compile(r"(?ms)(^```.*?^```|^~~~.*?^~~~)")


def unescape_markdown(text: str) -> str:
    """Unescape markdown in body only, skipping fenced code blocks."""
    parts = FENCE_RE.split(text)
    for i in range(len(parts)):
        if not FENCE_RE.match(parts[i]):
            parts[i] = ESCAPED_MARKDOWN_RE.sub(r"\1", parts[i])
    return "".join(parts)


# --- Task 2: HTML Entities ---

HTML_ENTITY_RE = re.compile(r"&(?:#\d+|#x[0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]+);")


def decode_entities(text: str) -> str:
    """Decode all HTML entities to UTF-8."""
    text = HTML_ENTITY_RE.sub(lambda m: html.unescape(m.group(0)), text)
    text = text.replace("\u00a0", " ")  # nbsp -> normal space
    return text


# --- Task 3: Strip WP Read-More from Excerpt ---

EXCERPT_BLOCK_RE = re.compile(
    r"(?ms)^excerpt:(?P<value>.*?)(?=^[A-Za-z_][A-Za-z0-9_]*:|\Z)"
)

FRONTMATTER_KEY_RE = re.compile(
    r"(?m)(?P<prefix>[^\n_])"
    r"(?P<key>author|author_name|canonical|categories|date|excerpt|featured_image|"
    r"featured_image_id|link|modified|og_image|seo_description|seo_title|slug|"
    r"status|title|type):(?=[ \t])"
)

READ_MORE_RE = re.compile(
    r"""(?is)\n*[ \t]*<p\s+class=["']read-more["'][^>]*>.*?</a>[ \t]*""",
    re.X,
)

HTML_TAG_RE = re.compile(r"(?s)<[^>]+>")


def clean_excerpt(excerpt_value: str) -> str:
    """Remove WP read-more HTML and all tags from excerpt."""
    excerpt_value = READ_MORE_RE.sub("", excerpt_value)
    excerpt_value = HTML_TAG_RE.sub("", excerpt_value)
    excerpt_value = re.sub(r"\n{3,}", "\n\n", excerpt_value)
    return excerpt_value.rstrip()


def strip_excerpt_html(frontmatter: str) -> str:
    """Strip HTML from the excerpt field in frontmatter."""
    return EXCERPT_BLOCK_RE.sub(
        lambda m: "excerpt:" + clean_excerpt(m.group("value")) + "\n",
        frontmatter,
    )


def repair_glued_frontmatter_keys(frontmatter: str) -> str:
    """Repair keys accidentally glued to the previous scalar value."""
    return FRONTMATTER_KEY_RE.sub(
        lambda m: f"{m.group('prefix')}\n{m.group('key')}:",
        frontmatter,
    )


# --- Task 4: Fix Featured Image URLs ---

UPLOAD_URL_RE = re.compile(
    r"^(?:https?://terrastories\.app)?/*wp-content/uploads/\d{4}/\d{2}/(?P<filename>[^?#\s]+)(?:[?#]\S*)?$"
)

WP_SIZE_SUFFIX_RE = re.compile(
    r"-(?P<w>\d{2,5})x(?P<h>\d{2,5})(?=\.[A-Za-z0-9]+$)"
)

FEATURED_ID_RE = re.compile(r"(?m)^featured_image_id:[ \t]*(?P<id>\d+)[ \t]*$")

IMAGE_FIELD_RE = re.compile(
    r"(?m)^(?P<key>featured_image|og_image):[ \t]*(?P<url>\S+)[ \t]*$"
)


def build_image_lookup():
    """Build a dict mapping media_id -> list of local filenames."""
    lookup = {}
    for f in IMAGES_DIR.iterdir():
        if not f.is_file():
            continue
        name = f.name
        # Extract ID prefix: everything before the first _
        parts = name.split("_", 1)
        if len(parts) == 2 and parts[0].isdigit():
            mid = parts[0]
            lookup.setdefault(mid, []).append(name)
    return lookup


def strip_size_suffix(filename: str) -> str:
    return WP_SIZE_SUFFIX_RE.sub("", filename)


def find_image_candidate(filename: str, media_id: str | None, lookup: dict) -> str | None:
    """Find a local image by media ID first, then by basename."""
    base_filename = strip_size_suffix(filename)
    candidates = lookup.get(media_id, []) if media_id else []

    for c in candidates:
        c_name = c.split("_", 1)[1] if "_" in c else c
        if strip_size_suffix(c_name) == base_filename:
            return c

    for all_candidates in lookup.values():
        for c in all_candidates:
            c_name = c.split("_", 1)[1] if "_" in c else c
            if strip_size_suffix(c_name) == base_filename:
                return c

    if candidates:
        candidates.sort(key=lambda c: (IMAGES_DIR / c).stat().st_size, reverse=True)
        return candidates[0]

    return None


def resolve_image_url(url: str, media_id: str | None, lookup: dict) -> str:
    """Convert WP image URLs and local thumbnail paths to existing local paths."""
    if url.startswith("/media/images/"):
        filename = urllib.parse.unquote(Path(url).name)
        local_path = IMAGES_DIR / filename
        tm = THUMBNAIL_FILE_RE.match(filename)
        if tm:
            original = tm.group("stem") + tm.group("ext")
            if (IMAGES_DIR / original).exists():
                return f"/media/images/{original}"
        if local_path.exists():
            return url
        candidate = find_image_candidate(filename, media_id, lookup)
        return f"/media/images/{candidate}" if candidate else url

    m = UPLOAD_URL_RE.match(url)
    if not m:
        return url  # external URL, leave alone

    filename = urllib.parse.unquote(m.group("filename"))
    candidate = find_image_candidate(filename, media_id, lookup)
    if candidate:
        return f"/media/images/{candidate}"

    return url  # couldn't resolve, leave as-is


def fix_image_urls(frontmatter: str, lookup: dict) -> str:
    """Fix featured_image and og_image URLs in frontmatter."""

    def get_media_id(fm):
        m = FEATURED_ID_RE.search(fm)
        return m.group("id") if m else None

    media_id = get_media_id(frontmatter)

    def replace_field(m):
        key = m.group("key")
        url = m.group("url")
        local = resolve_image_url(url, media_id, lookup)
        return f"{key}: {local}"

    return IMAGE_FIELD_RE.sub(replace_field, frontmatter)


# --- Task 5: Rewrite Internal Links ---

INTERNAL_URL_RE = re.compile(
    r"https?://(?:www\.)?terrastories\.app(?P<path>/(?!wp-content/uploads/)[^\s<>'\"\)\]]*)?"
)


def rewrite_internal_url(match):
    path = match.group("path") or ""
    if not path:
        return "/"
    # Preserve query/hash
    split = re.match(r"(?P<pathname>[^?#]*)(?P<suffix>[?#].*)?$", path)
    pathname = split.group("pathname") or "/"
    suffix = split.group("suffix") or ""
    if pathname != "/":
        pathname = pathname.rstrip("/")
    return pathname + suffix


def rewrite_internal_links(text: str) -> str:
    return INTERNAL_URL_RE.sub(rewrite_internal_url, text)


# --- Task 6: Remove Empty Heading Markers ---

EMPTY_HEADING_RE = re.compile(r"(?m)^[ \t]{0,3}#{1,6}[ \t]*\n")


def remove_empty_headings(body: str) -> str:
    return EMPTY_HEADING_RE.sub("", body)


# --- Task 7: Deduplicate Media ---

THUMBNAIL_FILE_RE = re.compile(
    r"^(?P<stem>.+)-(?P<w>\d{2,5})x(?P<h>\d{2,5})(?P<ext>\.(?:jpe?g|png|gif|webp))$",
    re.I,
)

MEDIA_THUMB_REF_RE = re.compile(
    r"(?P<prefix>(?:\.\./)?/?media/images/)"
    r"(?P<filename>[^)\]\s\"']+-\d{2,5}x\d{2,5}\.(?:jpe?g|png|gif|webp))",
    re.I,
)


def rewrite_thumbnail_refs(text: str) -> str:
    """Rewrite thumbnail references in markdown to point to originals."""

    def replacer(m):
        filename = m.group("filename")
        tm = THUMBNAIL_FILE_RE.match(filename)
        if not tm:
            return m.group(0)
        original = tm.group("stem") + tm.group("ext")
        if (IMAGES_DIR / original).exists():
            return m.group("prefix") + original
        return m.group(0)

    return MEDIA_THUMB_REF_RE.sub(replacer, text)


# --- Main ---

def process_file(filepath: Path, lookup: dict, write: bool) -> dict:
    """Process a single markdown file. Returns stats dict."""
    stats = {f"task{i}": 0 for i in range(1, 8)}
    original = filepath.read_text(encoding="utf-8")

    m = FRONTMATTER_RE.match(original)
    if not m:
        print(f"  WARNING: {filepath} does not match frontmatter pattern, skipping")
        return stats

    frontmatter = m.group("frontmatter")
    body = m.group("body")

    # Repair keys glued to previous values by earlier cleanup runs.
    before = frontmatter
    frontmatter = repair_glued_frontmatter_keys(frontmatter)
    if frontmatter != before:
        stats["task3"] += 1

    # Task 2: Decode HTML entities (frontmatter + body)
    before = frontmatter + body
    frontmatter = decode_entities(frontmatter)
    body = decode_entities(body)
    if frontmatter + body != before:
        stats["task2"] += 1

    # Task 3: Strip WP read-more HTML from excerpt
    before = frontmatter
    frontmatter = strip_excerpt_html(frontmatter)
    if frontmatter != before:
        stats["task3"] += 1

    # Task 4: Fix image URLs
    before = frontmatter
    frontmatter = fix_image_urls(frontmatter, lookup)
    if frontmatter != before:
        stats["task4"] += 1

    # Task 5: Rewrite internal links (frontmatter + body)
    before = frontmatter + body
    frontmatter = rewrite_internal_links(frontmatter)
    body = rewrite_internal_links(body)
    if frontmatter + body != before:
        stats["task5"] += 1

    # Task 1: Unescape markdown (body only)
    before = body
    body = unescape_markdown(body)
    if body != before:
        stats["task1"] += 1

    # Task 6: Remove empty headings (body only)
    before = body
    body = remove_empty_headings(body)
    if body != before:
        stats["task6"] += 1

    # Task 7: Rewrite thumbnail refs in body (content part - file deletion is separate)
    before = body
    body = rewrite_thumbnail_refs(body)
    if body != before:
        stats["task7"] += 1

    result = f"---\n{frontmatter}\n---\n{body}"

    if write and result != original:
        filepath.write_text(result, encoding="utf-8")

    return stats


def dedup_media(write: bool) -> int:
    """Remove WordPress thumbnail files. Returns count of deleted files."""
    deleted = 0
    kept = 0
    for f in sorted(IMAGES_DIR.iterdir()):
        if not f.is_file():
            continue
        m = THUMBNAIL_FILE_RE.match(f.name)
        if not m:
            continue
        original = IMAGES_DIR / f"{m.group('stem')}{m.group('ext')}"
        if original.exists():
            if write:
                f.unlink()
            deleted += 1
        else:
            kept += 1
    if kept:
        print(f"  WARNING: {kept} thumbnails have no original, keeping them")
    return deleted


def main():
    parser = argparse.ArgumentParser(description="Clean WordPress content for Astro")
    parser.add_argument("--write", action="store_true", help="Write changes (default: dry-run)")
    args = parser.parse_args()

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"=== Content Cleanup ({mode}) ===\n")

    # Build image lookup
    lookup = build_image_lookup()
    print(f"Image lookup: {len(lookup)} media IDs indexed")

    # Process markdown files
    md_files = sorted(CONTENT_DIR.rglob("*.md"))
    print(f"Processing {len(md_files)} markdown files...\n")

    total_stats = {f"task{i}": 0 for i in range(1, 8)}

    for f in md_files:
        rel = f.relative_to(BASE)
        stats = process_file(f, lookup, args.write)
        changes = sum(1 for v in stats.values() if v > 0)
        if changes:
            tasks = [f"task{i}" for i in range(1, 8) if stats[f"task{i}"]]
            print(f"  {rel}: modified ({', '.join(tasks)})")
        for k in total_stats:
            total_stats[k] += stats[k]

    # Dedup media
    print(f"\nDeduplicating media...")
    deleted = dedup_media(args.write)
    print(f"  Thumbnails {'would be ' if not args.write else ''}deleted: {deleted}")

    remaining = len(list(IMAGES_DIR.iterdir())) if not args.write else "N/A (dry-run)"
    if args.write:
        remaining = len(list(IMAGES_DIR.iterdir()))

    # Summary
    print(f"\n=== Summary ===")
    task_names = {
        "task1": "Unescaped markdown",
        "task2": "Decoded HTML entities",
        "task3": "Stripped excerpt HTML",
        "task4": "Fixed image URLs",
        "task5": "Rewrote internal links",
        "task6": "Removed empty headings",
        "task7": "Rewrote thumbnail refs",
    }
    for k, name in task_names.items():
        print(f"  {name}: {total_stats[k]} files")
    print(f"  Media thumbnails deleted: {deleted}")
    print(f"  Remaining media files: {remaining}")

    if not args.write:
        print(f"\n  Run with --write to apply changes")


if __name__ == "__main__":
    main()
