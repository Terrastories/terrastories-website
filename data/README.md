# Reference Data

This directory contains data exported from the original WordPress site.

## `site.json`

Exported from `terrastories.app` via WordPress REST API on 2026-06-10.
Contains categories, users, navigation menus, and export metadata.

**Not used at build time.** The Astro site uses:
- Navigation: `src/data/nav.ts`
- Content: `src/content/pages/` and `src/content/posts/`
- Categories: derived from post frontmatter

Kept for reference only.
