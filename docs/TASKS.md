# TASKS: Terrastories Website Codebase Review

**Created**: 2026-06-12
**Status**: In Progress
**Related**: `docs/PRD-codebase-review.md`

---

## Codebase Summary

| Metric | Value |
|---|---|
| Framework | Astro 6.x + Tailwind CSS 4 |
| Source files | 62 (excl. node_modules, dist, media) |
| Code lines | 1,056 (Python 735, JSON 156, CSS 117, TypeScript 33, JS 15) |
| Markdown content | 51 files (2,136 lines, classified as comments by pygount) |
| Components | 7 (Header, Footer, Seo, PostCard, PartnerLogo, PeopleGrid, + BaseLayout wraps) |
| Layouts | 3 (Base, Page, Post) |
| Page routes | 8 (index, [...slug], community, blog/index, blog/[slug], category/[category]) |
| Media | 160 files in public/, 149 in static/, ~62MB total |
| Build time | ~10s, 48 pages |
| Dependencies | astro, tailwindcss, @tailwindcss/typography, @tailwindcss/vite, @astrojs/sitemap, sharp |

---

## Review Batches

### Batch 1: Build & Configuration

**Files**: `package.json`, `astro.config.mjs`, `tsconfig.json`, `.gitignore`

**Checklist**:
- [ ] Dependencies pinned to compatible ranges (no `^` drift risk)
- [ ] astro.config.mjs: site URL correct, integrations configured properly
- [ ] astro.config.mjs: sharp image service compatible with Astro 6
- [ ] tsconfig.json: strict mode enabled and appropriate
- [ ] .gitignore: all necessary patterns present
- [ ] No unnecessary dependencies
- [ ] `npm run build` produces no warnings
- [ ] `astro check` (TypeScript checking) passes

---

### Batch 2: Content Collections & Schema

**Files**: `src/content.config.ts`

**Checklist**:
- [ ] Schema validates all frontmatter fields used across 44 content files
- [ ] Optional vs required fields are correctly designated
- [ ] Default values are sensible
- [ ] `glob` loader paths correct relative to project root
- [ ] No missing fields that would cause runtime errors
- [ ] Type safety: `CollectionEntry<'pages'>` and `CollectionEntry<'posts'>` correctly typed

---

### Batch 3: Layouts

**Files**: `src/layouts/BaseLayout.astro`, `src/layouts/PageLayout.astro`, `src/layouts/PostLayout.astro`

**Checklist**:
- [ ] BaseLayout: proper DOCTYPE, html lang, charset, viewport
- [ ] BaseLayout: font loading strategy (Google Fonts render-blocking?)
- [ ] BaseLayout: favicon links correct
- [ ] BaseLayout: skip-to-content link present and functional
- [ ] BaseLayout: proper `<main>` landmark with id matching skip link
- [ ] PageLayout: renders page content correctly with proper SEO
- [ ] PostLayout: category links work, date formatting correct
- [ ] PostLayout: author_name fallback works correctly
- [ ] All layouts: consistent heading hierarchy
- [ ] Slot usage correct (especially Seo component in named slot)

---

### Batch 4: Components — Header & Navigation

**Files**: `src/components/Header.astro`

**Checklist**:
- [ ] Desktop nav: dropdown menus accessible (keyboard, screen reader)
- [ ] Mobile nav: burger menu animates correctly
- [ ] Mobile nav: Escape key closes panel
- [ ] Mobile nav: overlay click closes panel
- [ ] Mobile nav: body scroll lock works
- [ ] Mobile nav: aria-expanded toggles correctly
- [ ] Current page highlighting works for all routes
- [ ] External links have proper target/rel attributes
- [ ] Skip-to-content link is first focusable element
- [ ] Dropdown focus-within works for keyboard navigation
- [ ] No z-index conflicts between header and other fixed elements
- [ ] Responsive breakpoint (lg:) appropriate for nav content

---

### Batch 5: Components — Footer

**Files**: `src/components/Footer.astro`

**Checklist**:
- [ ] Footer nav structure mirrors header nav
- [ ] Social links: Twitter icon updated to X logo (currently X logo used, correct)
- [ ] Social links: GitHub, mailing list links correct
- [ ] Footer layout responsive (single column mobile, two columns desktop)
- [ ] Copyright year dynamic
- [ ] External links have target="_blank" rel="noopener noreferrer"
- [ ] Proper aria-labels on nav sections

---

### Batch 6: Components — Seo & Meta

**Files**: `src/components/Seo.astro`

**Checklist**:
- [ ] Title tag: proper fallback when seo_title missing
- [ ] Meta description: proper fallback chain
- [ ] OG tags: type, title, description, url, image all set
- [ ] Twitter card: proper summary_large_image fallback
- [ ] Canonical URL constructed correctly
- [ ] No duplicate canonical/favicons (BaseLayout also has favicon links)
- [ ] Favicon SVG link in Seo duplicates BaseLayout favicon links
- [ ] OG image URL construction: relative paths resolved to absolute correctly

---

### Batch 7: Components — Content Display

**Files**: `src/components/PostCard.astro`, `src/components/PartnerLogo.astro`, `src/components/PeopleGrid.astro`

**Checklist**:
- [ ] PostCard: image aspect ratio maintained, lazy loading
- [ ] PostCard: proper article semantics, heading hierarchy
- [ ] PostCard: "Read more" button is a link (accessible)
- [ ] PostCard: line-clamp-3 works cross-browser
- [ ] PartnerLogo: opens in new tab with proper attributes
- [ ] PeopleGrid: images are round circles (user requirement)
- [ ] PeopleGrid: hover effects work, ring color transitions
- [ ] PeopleGrid: responsive grid (2/3/4/5 columns)

---

### Batch 8: Pages & Routing

**Files**: `src/pages/index.astro`, `src/pages/[...slug].astro`, `src/pages/community.astro`, `src/pages/blog/index.astro`, `src/pages/blog/[slug].astro`, `src/pages/category/[category].astro`

**Checklist**:
- [ ] index.astro: all sections render (hero, intro, video, latest stories, CTA, sponsors, partners)
- [ ] index.astro: video fallback chain works (mp4 → webp → poster image)
- [ ] [...slug].astro: correctly excludes home and community pages
- [ ] [...slug].astro: community has its own page, not caught by catch-all
- [ ] community.astro: people grid renders with correct stewards/alumni
- [ ] blog/index.astro: all posts listed, sorted by date descending
- [ ] blog/[slug].astro: getStaticPaths generates paths for all posts
- [ ] category/[category].astro: categorySlug mapping correct
- [ ] category/[category].astro: descriptions for known categories
- [ ] No 404 page (should there be one?)
- [ ] All internal links between pages resolve correctly

---

### Batch 9: Styles & Design System

**Files**: `src/styles/global.css`

**Checklist**:
- [ ] Tailwind 4 `@theme` syntax correct (CSS-first config)
- [ ] Brand colors defined: orange (#d97b29), gold (#dea826), teal (#09697e), body (#3a3a3a)
- [ ] Legacy color aliases still referenced anywhere? (forest, moss, clay, river, ink, paper)
- [ ] Typography scale appropriate
- [ ] .btn and .btn-outline styles consistent with original WP site
- [ ] Focus-visible styles defined (accessibility)
- [ ] ::selection styles set
- [ ] Responsive font sizes at breakpoints
- [ ] prose img centering (Tailwind Typography override)
- [ ] iframe aspect-ratio (16:9) applied
- [ ] No unused legacy aliases that could confuse contributors

---

### Batch 10: Utility Code

**Files**: `src/utils/category.ts`

**Checklist**:
- [ ] categorySlug handles special chars (& → and)
- [ ] categorySlug produces URL-safe slugs matching content file paths
- [ ] No edge cases (empty string, unicode, special chars)

---

### Batch 11: Python Scripts

**Files**: `scripts/clean-content.py`, `scripts/compress-media.py`, `scripts/resize-images.py`

**Checklist**:
- [ ] clean-content.py: all 7 tasks work correctly
- [ ] clean-content.py: dry-run mode produces correct output
- [ ] clean-content.py: frontmatter regex handles edge cases (multiline values, special chars)
- [ ] compress-media.py: JPEG quality appropriate (82)
- [ ] compress-media.py: PNG→JPEG conversion threshold reasonable
- [ ] compress-media.py: animated GIF handling correct (skip)
- [ ] resize-images.py: MAX_WIDTH/HEIGHT (1200) appropriate
- [ ] resize-images.py: backup to _originals/ before resizing
- [ ] resize-images.py: handles RGBA, P mode images
- [ ] All scripts: error handling for corrupt images

---

### Batch 12: Media & Static Assets

**Files**: `public/`, `static/`, `_originals/`

**Checklist**:
- [ ] Duplicate media: public/ vs static/ — both exist, clarify purpose
- [ ] static/ directory: still needed or vestigial from migration?
- [ ] Image formats: mix of JPG, PNG, GIF, WebP — any unoptimized?
- [ ] Video file: 27_terrastories.mp4 in public/ — size appropriate?
- [ ] PDF documents: accessible and linked correctly
- [ ] Favicons: complete set (ico, 16, 32, svg, apple-touch)
- [ ] _originals/: excluded from build and git

---

### Batch 13: SEO & Performance Audit

**Checklist**:
- [ ] Lighthouse Performance score (target >= 95)
- [ ] Lighthouse SEO score (target >= 95)
- [ ] Lighthouse Accessibility score (target >= 95)
- [ ] Google Fonts render-blocking: should use font-display: swap
- [ ] Image lazy loading applied consistently
- [ ] Sitemap generated correctly
- [ ] No broken internal links
- [ ] No broken external links
- [ ] Proper heading hierarchy on every page (single h1, logical h2/h3/h4)
- [ ] Alt text on all images

---

### Batch 14: Content Quality

**Files**: `src/content/pages/*.md`, `src/content/posts/*.md`

**Checklist**:
- [ ] All 11 pages render without errors
- [ ] All 33 posts render without errors
- [ ] No remaining WordPress artifacts in content
- [ ] No broken image references
- [ ] No broken internal links
- [ ] Category assignments correct
- [ ] Author attribution correct
- [ ] Dates valid and reasonable

---

### Batch 15: Deployment Readiness

**Checklist**:
- [ ] `npm run build` produces clean dist/
- [ ] dist/ size reasonable
- [ ] Cloudflare Pages compatible (no server-side requirements)
- [ ] _redirects or headers file needed?
- [ ] 404 page exists
- [ ] robots.txt needed?
- [ ] No hardcoded localhost or internal URLs

---

## Execution Notes

- Each batch should be run as a focused review pass
- Issues found should be documented with file, line number, severity
- Critical issues block deployment; medium issues tracked for fix; low issues are nice-to-have
- After all batches complete, findings feed into `PRD-codebase-review.md` action items
