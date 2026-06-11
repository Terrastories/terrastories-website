#!/usr/bin/env python3
"""
Terrastories WordPress to Static Markdown Migration Script
===========================================================
Exports ALL content from a WordPress site via REST API, downloads all media,
converts HTML to clean Markdown, and enriches frontmatter with SEO metadata.

Requirements:
  - wpexportjson binary in PATH (https://github.com/tradik/wpexporter/releases)
  - Python 3.8+ with: requests, markdownify, beautifulsoup4, pyyaml

Usage:
  pip install requests markdownify beautifulsoup4 pyyaml
  python terrastories-migrate.py --url https://terrastories.app --output ./site
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

try:
    import requests
    from markdownify import markdownify as md, MarkdownConverter
    from bs4 import BeautifulSoup
    import yaml
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install requests markdownify beautifulsoup4 pyyaml")
    sys.exit(1)


# ============================================================
# CONFIG
# ============================================================
DEFAULT_URL = "https://terrastories.app"
API_BASE = "/wp-json/wp/v2"
REQUEST_TIMEOUT = 30
REQUEST_DELAY = 0.5  # seconds between API calls


# ============================================================
# STEP 1: Full API export via wpexportjson
# ============================================================
def run_wpexportjson(site_url: str, output_dir: str) -> dict:
    """Run wpexportjson to get all content + metadata + media."""
    print(f"\n{'='*60}")
    print("STEP 1: Exporting via wpexportjson")
    print(f"{'='*60}")

    raw_dir = os.path.join(output_dir, "_raw_export")

    wpexportjson_bin = os.environ.get("WPEXPORTJSON_BIN", "wpexportjson")
    cmd = [
        wpexportjson_bin,
        "export",
        "--url", site_url,
        "--format", "markdown",
        "--output", raw_dir,
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

    if result.returncode != 0:
        print(f"ERROR: wpexportjson failed: {result.stderr}")
        sys.exit(1)

    print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)

    # Load metadata
    meta_path = os.path.join(raw_dir, "metadata.json")
    with open(meta_path) as f:
        metadata = json.load(f)

    stats = metadata.get("stats", {})
    print(f"\nExported: {stats.get('total_posts',0)} posts, "
          f"{stats.get('total_pages',0)} pages, "
          f"{stats.get('media_downloaded',0)} media files, "
          f"{len(metadata.get('categories',[]))} categories, "
          f"{len(metadata.get('users',[]))} users")

    return metadata


# ============================================================
# STEP 2: Fetch Yoast SEO data from API
# ============================================================
def fetch_yoast_data(site_url: str, post_type: str, total: int) -> dict:
    """Fetch Yoast SEO metadata for all posts/pages."""
    print(f"\n{'='*60}")
    print(f"STEP 2: Fetching Yoast SEO data for {post_type}")
    print(f"{'='*60}")

    yoast_data = {}
    page = 1
    per_page = 20

    while True:
        url = f"{site_url}{API_BASE}/{post_type}"
        resp = requests.get(url, params={
            "per_page": per_page,
            "page": page,
            "_fields": "id,slug,yoast_head_json"
        }, timeout=REQUEST_TIMEOUT)

        if resp.status_code != 200:
            print(f"  API returned {resp.status_code}, stopping")
            break

        items = resp.json()
        if not items:
            break

        for item in items:
            yoast = item.get("yoast_head_json", {})
            yoast_data[item["id"]] = {
                "slug": item.get("slug", ""),
                "seo_title": yoast.get("title", ""),
                "seo_description": yoast.get("description", ""),
                "og_image": yoast.get("og_image", [{}])[0].get("url", "") if yoast.get("og_image") else "",
                "canonical": yoast.get("canonical", ""),
                "twitter_card": yoast.get("twitter_card", ""),
                "og_type": yoast.get("og_type", ""),
            }

        print(f"  Page {page}: fetched {len(items)} {post_type}")
        page += 1
        import time
        time.sleep(REQUEST_DELAY)

    return yoast_data


# ============================================================
# STEP 3: Fetch menu structure
# ============================================================
def fetch_menus(site_url: str) -> list:
    """Try to fetch navigation menus."""
    print(f"\n{'='*60}")
    print("STEP 3: Fetching navigation menus")
    print(f"{'='*60}")

    menus = []

    # Try the navigation endpoint
    try:
        resp = requests.get(f"{site_url}{API_BASE}/navigation", timeout=REQUEST_TIMEOUT)
        if resp.status_code == 200 and resp.json():
            menus = resp.json()
            print(f"  Found {len(menus)} navigation items")
        else:
            print("  Navigation endpoint empty or unavailable")
    except Exception as e:
        print(f"  Could not fetch menus: {e}")

    # Fallback: scrape the homepage to extract nav links
    if not menus:
        print("  Falling back to scraping homepage for nav links...")
        try:
            resp = requests.get(site_url, timeout=REQUEST_TIMEOUT)
            soup = BeautifulSoup(resp.text, "html.parser")

            nav_links = []
            for nav in soup.find_all("nav"):
                for a in nav.find_all("a", href=True):
                    nav_links.append({
                        "text": a.get_text(strip=True),
                        "href": a["href"],
                    })

            if nav_links:
                menus = nav_links
                print(f"  Found {len(nav_links)} nav links from homepage")
        except Exception as e:
            print(f"  Could not scrape homepage: {e}")

    return menus


# ============================================================
# STEP 4: Clean HTML to proper Markdown
# ============================================================
class WPCleanConverter(MarkdownConverter):
    """Custom markdownify converter that handles WordPress HTML quirks."""

    def convert_figure(self, el, text, parent):
        """Convert <figure> to markdown image with caption."""
        img = el.find("img")
        if img:
            src = img.get("src", "")
            alt = img.get("alt", "")
            title = img.get("title", "")
            figcaption = el.find("figcaption")
            caption = figcaption.get_text(strip=True) if figcaption else ""
            title_part = title or caption
            if title_part:
                return f"\n![{alt}]({src} \"{title_part}\")\n"
            return f"\n![{alt}]({src})\n"
        return text

    def convert_figcaption(self, el, text, parent):
        return ""  # Handled in convert_figure


def html_to_clean_markdown(html: str) -> str:
    """Convert WordPress HTML to clean Markdown."""
    if not html:
        return ""

    # Pre-clean: remove WP-specific junk
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style tags
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()

    # Remove WP block comments
    clean_html = str(soup)
    clean_html = re.sub(r"<!--\s*wp:.*?-->", "", clean_html)
    clean_html = re.sub(r"<!--\s*/wp:.*?-->", "", clean_html)
    clean_html = re.sub(r"<!--.*?-->", "", clean_html)

    # Convert to markdown
    # markdownify doesn't allow both convert and strip simultaneously
    # First strip useless wrapper tags, then convert
    strip_tags = ["span", "div", "section", "article", "main",
                  "header", "footer", "noscript", "iframe"]
    for tag in strip_tags:
        clean_html = re.sub(rf"<{tag}[^>]*>", "", clean_html, flags=re.IGNORECASE)
        clean_html = re.sub(rf"</{tag}>", "", clean_html, flags=re.IGNORECASE)

    result = md(
        clean_html,
        heading_style="atx",
        bullets="-",
    )

    # Post-clean
    result = re.sub(r"\n{3,}", "\n\n", result)  # Max 2 newlines
    result = result.replace("\xa0", " ")  # Non-breaking spaces
    result = result.strip()

    return result


def clean_markdown_file(filepath: str) -> str:
    """Read a wpexportjson .md file, clean its HTML content, return clean MD."""
    with open(filepath) as f:
        content = f.read()

    # Extract frontmatter
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        return content

    frontmatter_str = match.group(1)
    body = match.group(2)

    # Clean the body HTML to markdown
    clean_body = html_to_clean_markdown(body)

    return frontmatter_str, clean_body


# ============================================================
# STEP 5: Build the static site structure
# ============================================================
def build_site(output_dir: str, raw_metadata: dict,
               yoast_posts: dict, yoast_pages: dict,
               menus: list, site_url: str):
    """Process all content into a clean static site structure."""
    print(f"\n{'='*60}")
    print("STEP 5: Building clean static site")
    print(f"{'='*60}")

    raw_dir = os.path.join(output_dir, "_raw_export")
    site_dir = os.path.join(output_dir, "site")

    # Create structure
    dirs = {
        "content": os.path.join(site_dir, "content"),
        "posts": os.path.join(site_dir, "content", "posts"),
        "pages": os.path.join(site_dir, "content", "pages"),
        "media": os.path.join(site_dir, "static", "media"),
        "data": os.path.join(site_dir, "data"),
    }
    for d in dirs.values():
        os.makedirs(d, exist_ok=True)

    # Build category map
    categories = {c["id"]: c for c in raw_metadata.get("categories", [])}

    # Build user map
    users = {u["id"]: u for u in raw_metadata.get("users", [])}

    # Process pages
    pages_processed = 0
    raw_pages_dir = os.path.join(raw_dir, "pages")
    if os.path.isdir(raw_pages_dir):
        for fname in os.listdir(raw_pages_dir):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(raw_pages_dir, fname)
            result = clean_markdown_file(fpath)
            if result is None or result is False or not isinstance(result, tuple):
                continue
            fm_str, body = result

            # Parse frontmatter
            fm = yaml.safe_load(fm_str) or {}
            page_id = fm.get("id")

            # Enrich with Yoast
            seo = yoast_pages.get(page_id, {}) if page_id else {}
            if seo:
                fm["seo_title"] = seo.get("seo_title", "")
                fm["seo_description"] = seo.get("seo_description", "")
                fm["og_image"] = seo.get("og_image", "")
                fm["canonical"] = seo.get("canonical", "")

            # Add author name
            author_id = fm.get("author_id")
            if author_id and author_id in users:
                fm["author_name"] = users[author_id].get("name", fm.get("author", ""))

            # Rewrite image paths to local media
            body = rewrite_media_paths(body, site_url)

            # Write clean file
            slug = fm.get("slug", fname.replace(".md", ""))
            out_path = os.path.join(dirs["pages"], f"{slug}.md")
            write_md_file(out_path, fm, body)
            pages_processed += 1

    print(f"  Processed {pages_processed} pages")

    # Process posts
    posts_processed = 0
    raw_posts_dir = os.path.join(raw_dir, "posts")
    if os.path.isdir(raw_posts_dir):
        for category_dir in os.listdir(raw_posts_dir):
            cat_path = os.path.join(raw_posts_dir, category_dir)
            if not os.path.isdir(cat_path):
                continue
            for fname in os.listdir(cat_path):
                if not fname.endswith(".md"):
                    continue
                fpath = os.path.join(cat_path, fname)
                result = clean_markdown_file(fpath)
                if result is None or result is False or not isinstance(result, tuple):
                    continue
                fm_str, body = result

                fm = yaml.safe_load(fm_str) or {}
                post_id = fm.get("id")

                # Enrich with Yoast
                seo = yoast_posts.get(post_id, {}) if post_id else {}
                if seo:
                    fm["seo_title"] = seo.get("seo_title", "")
                    fm["seo_description"] = seo.get("seo_description", "")
                    fm["og_image"] = seo.get("og_image", "")

                # Add category and author
                cat_ids = fm.get("category_ids", [])
                if cat_ids:
                    fm["categories"] = [categories.get(cid, {}).get("name", str(cid))
                                       for cid in cat_ids if cid in categories]

                author_id = fm.get("author_id")
                if author_id and author_id in users:
                    fm["author_name"] = users[author_id].get("name", fm.get("author", ""))

                body = rewrite_media_paths(body, site_url)

                slug = fm.get("slug", fname.replace(".md", ""))
                out_path = os.path.join(dirs["posts"], f"{slug}.md")
                write_md_file(out_path, fm, body)
                posts_processed += 1

    print(f"  Processed {posts_processed} posts")

    # Copy media files
    raw_media = os.path.join(raw_dir, "media")
    if os.path.isdir(raw_media):
        import shutil
        # Copy only original (full-size) images, not all thumbnails
        for subdir in os.listdir(raw_media):
            src_subdir = os.path.join(raw_media, subdir)
            if not os.path.isdir(src_subdir):
                continue
            dst_subdir = os.path.join(dirs["media"], subdir)
            os.makedirs(dst_subdir, exist_ok=True)
            for f in os.listdir(src_subdir):
                src_file = os.path.join(src_subdir, f)
                shutil.copy2(src_file, os.path.join(dst_subdir, f))
        print(f"  Copied media files")

    # Save site data
    site_data = {
        "site_url": site_url,
        "export_date": datetime.now().isoformat(),
        "stats": {
            "posts": posts_processed,
            "pages": pages_processed,
            "media": raw_metadata.get("stats", {}).get("total_media", 0),
            "categories": len(categories),
            "users": len(users),
        },
        "categories": {str(k): v for k, v in categories.items()},
        "users": {str(k): {"name": v.get("name",""), "slug": v.get("slug","")}
                  for k, v in users.items()},
        "menus": menus,
    }

    with open(os.path.join(dirs["data"], "site.json"), "w") as f:
        json.dump(site_data, f, indent=2)

    print(f"\n  Site data saved to {dirs['data']}/site.json")

    # Print summary
    print(f"\n{'='*60}")
    print("EXPORT COMPLETE")
    print(f"{'='*60}")
    print(f"  Output: {site_dir}")
    print(f"  Pages:  {pages_processed}")
    print(f"  Posts:  {posts_processed}")
    print(f"  Media:  {site_data['stats']['media']} items")
    print(f"  Categories: {len(categories)}")
    print(f"  Users:  {len(users)}")
    print(f"\n  Structure:")
    print(f"    {site_dir}/")
    print(f"      content/")
    print(f"        pages/   ({pages_processed} .md files)")
    print(f"        posts/   ({posts_processed} .md files)")
    print(f"      static/")
    print(f"        media/   (images + documents)")
    print(f"      data/")
    print(f"        site.json  (metadata, categories, users, menus)")

    return site_data


def rewrite_media_paths(body: str, site_url: str) -> str:
    """Rewrite absolute WP media URLs to relative local paths."""
    # Rewrite https://terrastories.app/wp-content/uploads/... -> /static/media/...
    pattern = re.escape(site_url) + r"/wp-content/uploads/([^\"\s)]+)"
    body = re.sub(pattern, r"/static/media/\1", body)
    return body


def write_md_file(filepath: str, frontmatter: dict, body: str):
    """Write a clean markdown file with YAML frontmatter."""
    # Clean frontmatter - remove raw IDs and internal fields
    clean_fm = {}
    for key in ["title", "slug", "date", "modified", "status", "type", "link",
                "author", "author_name", "categories", "excerpt",
                "featured_image", "featured_image_id", "template",
                "seo_title", "seo_description", "og_image", "canonical",
                "menu_order", "parent"]:
        if key in frontmatter and frontmatter[key]:
            clean_fm[key] = frontmatter[key]

    with open(filepath, "w") as f:
        f.write("---\n")
        f.write(yaml.dump(clean_fm, default_flow_style=False, allow_unicode=True))
        f.write("---\n\n")
        f.write(body)
        if not body.endswith("\n"):
            f.write("\n")


# ============================================================
# MAIN
# ============================================================
def main():
    parser = argparse.ArgumentParser(
        description="Export WordPress site to clean Markdown for static site migration")
    parser.add_argument("--url", default=DEFAULT_URL, help="WordPress site URL")
    parser.add_argument("--output", default="./terrastories-export", help="Output directory")
    parser.add_argument("--skip-media", action="store_true", help="Skip media download")
    args = parser.parse_args()

    print(f"Terrastories WP -> Static Site Migration")
    print(f"Source: {args.url}")
    print(f"Output: {args.output}")

    os.makedirs(args.output, exist_ok=True)

    # Step 1: Bulk export via wpexportjson
    metadata = run_wpexportjson(args.url, args.output)

    # Step 2: Fetch Yoast SEO data
    yoast_posts = fetch_yoast_data(args.url, "posts",
                                   metadata.get("stats", {}).get("total_posts", 0))
    yoast_pages = fetch_yoast_data(args.url, "pages",
                                   metadata.get("stats", {}).get("total_pages", 0))

    # Step 3: Fetch menus
    menus = fetch_menus(args.url)

    # Step 4-5: Clean HTML and build site
    site_data = build_site(args.output, metadata, yoast_posts, yoast_pages, menus, args.url)

    print(f"\nDone! Your clean static site is at: {args.output}/site/")


if __name__ == "__main__":
    main()
