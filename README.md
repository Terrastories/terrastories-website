# Terrastories Website

Exported WordPress content as Markdown for the Terrastories static site migration.

## Structure

```
terrastories-website/
  content/
    pages/       # 11 pages (home, about, how-it-works, etc.)
    posts/       # 33 blog posts
  static/
    media/
      images/    # All WordPress images (all sizes)
      documents/ # PDFs and other documents
  data/
    site.json   # Categories, users, navigation menus, export metadata
  terrastories-migrate.py  # Migration script (re-runnable)
```

## Source

Exported from https://terrastories.app via WordPress REST API.

## Content

- 33 posts across 3 categories (User Stories, Dev Stories, Uncategorized)
- 11 pages
- 144 media items (610 files including all WP thumbnail sizes)
- 2 authors
- Full Yoast SEO metadata (title, description, OG image per page/post)

## Re-running the export

```bash
pip install requests markdownify beautifulsoup4 pyyaml
# Requires wpexportjson binary: https://github.com/tradik/wpexporter/releases
python3 terrastories-migrate.py --url https://terrastories.app --output ./export
```
