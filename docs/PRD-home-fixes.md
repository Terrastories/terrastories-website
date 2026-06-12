# PRD: Home Page Design Fixes

## Status: IN PROGRESS

## Problem Statement
The Home page has 8 design/rendering issues caused by the WordPress content being dumped as a single markdown blob. The markdown contains embedded blog cards, partner logos, CTA sections, and headings that should be separate Astro components or structured sections -- not raw markdown rendered inside a single `<div class="prose">`.

## Root Cause Analysis
The file `src/content/pages/home.md` contains the ENTIRE WordPress homepage content as one markdown file. When rendered by Astro's markdown pipeline, this creates:
- A single `<p>` wrapping block elements (invalid HTML)
- Uppercase plain text where headings should be
- Empty alt attributes on images
- Zero-width joiner characters from WordPress
- Duplicate "Latest Stories" sections
- Partner logos without proper accessibility attributes

## Issues (from user feedback)

### Issue 1: Invalid HTML nesting
The markdown renders as one continuous `<p>` containing block elements (h4, img, links). This is invalid HTML.
**Fix:** Split home.md content into separate sections in index.astro. Only the hero/description stays as markdown.

### Issue 2: Missing heading styling
"LATEST STORIES" and "HELP US GROW" are plain uppercase text in a paragraph, not heading elements.
**Fix:** Replace with proper `<h2>` / `<h3>` elements in the Astro template.

### Issue 3: Missing alt text
UN SDG images and hero images have empty `alt` attributes.
**Fix:** Add meaningful alt text to all images in the restructured content.

### Issue 4: Stray invisible characters and extra spaces
Zero-width joiner (`\u200d`) before "Awana Digital", double space before "Explore Terrastories".
**Fix:** Clean these from the markdown content and use proper text in the template.

### Issue 5: Duplicate "Latest Stories" content
Two "Latest Stories" sections: one embedded in markdown (plain text), one properly built with PostCard components.
**Fix:** Remove the inline blog cards from home.md entirely. The PostCard grid in index.astro handles this.

### Issue 6: Broken section delineation
"Help us grow" CTA and sponsor logos are crammed into the same markdown paragraph.
**Fix:** Create separate Astro sections: CTA section + sponsor/partner grid section.

### Issue 7: Canonical/OG metadata uses primary domain
The `<link rel="canonical">` points to terrastories.app, not the preview URL.
**Fix:** This is CORRECT behavior. Canonical should always point to the production domain, even on preview. No change needed. Will note this in the PRD.

### Issue 8: Accessibility for partner logo links
Partner logos use images without `aria-label` attributes, and link text is just the logo image.
**Fix:** Add `aria-label` to partner logo links with the organization name.

## Implementation Plan

### Phase A: Restructure home.md
- Strip home.md to ONLY the hero content: tagline, description paragraph, hero GIF, UN SDG logos
- Remove all inline blog cards, CTA text, and partner logos from the markdown
- Fix alt text on remaining images
- Remove zero-width characters

### Phase B: Update index.astro
- Keep hero section rendering the cleaned markdown
- Keep existing PostCard grid section (already works)
- Add new "Help Us Grow" CTA section with styled buttons
- Add new Partners/Sponsors section with accessible logo grid
- All new sections use proper semantic HTML (sections, headings, aria-labels)

### Phase C: Create PartnerLogo component
- New component for partner/sponsor logos
- Accepts name, url, image path, and optional ariaLabel props
- Always includes aria-label for accessibility

### Phase D: Codex review
- Submit changes for Codex review
- Fix any issues found
- Commit

## Files to Modify
- `src/content/pages/home.md` -- strip to hero content only
- `src/pages/index.astro` -- add CTA + partners sections
- `src/components/PartnerLogo.astro` -- NEW accessible logo component

## Files NOT Modified
- `src/components/Seo.astro` -- canonical behavior is correct (points to production domain)
