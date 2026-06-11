# PRD: How It Works Page Fixes

## Status: IN PROGRESS

## Root Cause Analysis
Two sources of problems:
1. **PageLayout.astro** renders `page.data.title` as an `<h1>` in the article header, but the markdown content also starts with `# How It Works` producing a second `<h1>`.
2. **how-it-works.md** is a raw WordPress dump with markdown artifacts, empty alt text, and duplicate links.

## Issues & Fixes

### Issue 1: Duplicate h1 headings
PageLayout renders `<h1>{page.data.title}</h1>` AND the markdown has `# How It Works`.
**Fix:** Remove the `# How It Works` heading from the markdown. PageLayout handles the page title.

### Issue 2: Markdown artifacts in YouTube links
YouTube links have `#### ` prefixes in the link text: `[#### Mapping your place-based...]`.
**Fix:** Remove the `#### ` prefix from all YouTube link text.

### Issue 3: Missing/unhelpful alt text
- Main diagram gif has filename-based alt: `terrastories-1920x1080-768x432-1`
- ACT guide cover image has empty alt: `![](...)`
- PDF icon has empty alt: `![](...)`
- EDT capture has empty alt: `![](...)`
**Fix:** Add meaningful alt text to all images.

### Issue 4: Duplicate PDF links
The ACT guide download section links to the same PDF 3 times (image link, PDF icon link, text link).
**Fix:** Consolidate to a single clear download link with descriptive text.

### Issue 5: Redundant "HOW IT WORKS" text
Line 25 has uppercase "HOW IT WORKS" right after the h1 heading.
**Fix:** Remove it.

## Files to Modify
- `src/content/pages/how-it-works.md` -- all content fixes
- `src/layouts/PageLayout.astro` -- skip excerpt on how-it-works (it starts with "HOW IT WORKS")
