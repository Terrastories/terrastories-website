# PRD: Terrastories Website — Codebase Review

| Field | Value |
|---|---|
| **Status** | Draft |
| **Created** | 2026-06-12 |
| **Author** | Hermes Agent |
| **Epic** | Terrastories V2 — Website Quality |
| **Repo** | `Terrastories/terrastories-website` |
| **Reviewers** | DeepSeek (automated review) |

---

## 1. Problem Statement

The Terrastories website has been migrated from WordPress to a static Astro site. The migration produced a working build (48 pages, 10s build time), but the codebase has not undergone a systematic quality review. Before deploying to production, we need to audit the architecture, components, styling, accessibility, performance, SEO, and deployment readiness to ensure the site meets professional standards.

This PRD defines the scope, findings, and action items for that review.

---

## 2. Goals

| ID | Goal | Success Metric |
|---|---|---|
| G-1 | Achieve Lighthouse Performance >= 95 | All pages score 95+ on Lighthouse Performance |
| G-2 | Achieve Lighthouse Accessibility >= 95 | All pages pass WCAG 2.1 AA checks |
| G-3 | Achieve Lighthouse SEO >= 95 | All pages pass SEO audit |
| G-4 | Zero broken links or missing assets | Internal links resolve; images load; no 404s |
| G-5 | Clean, maintainable codebase | No dead code, no legacy artifacts, consistent patterns |
| G-6 | Deployment-ready for Cloudflare Pages | Build output deployable without modifications |

---

## 3. Architecture Overview

### 3.1 Stack

| Layer | Technology | Version |
|---|---|---|
| Framework | Astro | 6.x |
| Styling | Tailwind CSS | 4.x |
| Typography | @tailwindcss/typography | 0.5.x |
| Image processing | Sharp | 0.34.x |
| Sitemap | @astrojs/sitemap | 3.x |
| Language | TypeScript (strict) | 5.x |

### 3.2 Codebase Metrics

| Language | Files | Code Lines | Comment Lines |
|---|---|---|---|
| Python | 4 | 735 | 156 |
| JSON | 3 | 156 | 0 |
| CSS | 1 | 117 | 4 |
| TypeScript | 2 | 33 | 0 |
| JavaScript | 1 | 15 | 0 |
| Markdown (content) | 51 | 0 | 2,136 |
| **Total** | **78** | **1,056** | **2,296** |

### 3.3 Component Architecture

```
BaseLayout.astro (root HTML shell)
  ├── Header.astro (desktop + mobile nav with dropdowns)
  ├── <slot /> (page content)
  │   ├── PageLayout.astro (generic pages)
  │   ├── PostLayout.astro (blog posts)
  │   ├── index.astro (home page — custom sections)
  │   └── community.astro (custom page with PeopleGrid)
  └── Footer.astro (nav + social + copyright)

Components:
  Seo.astro — meta tags (OG, Twitter, canonical)
  PostCard.astro — blog post preview card
  PartnerLogo.astro — sponsor/partner logo link
  PeopleGrid.astro — circle photo grid for team members
```

### 3.4 Routing

| Route | File | Purpose |
|---|---|---|
| `/` | `index.astro` | Home page (custom layout) |
| `/:slug` | `[...slug].astro` | All pages except home, community |
| `/community` | `community.astro` | Community page (custom layout) |
| `/blog` | `blog/index.astro` | Blog listing |
| `/blog/:slug` | `blog/[slug].astro` | Individual blog post |
| `/category/:category` | `category/[category].astro` | Category filter (user-stories, dev-stories, uncategorized) |

### 3.5 Data Flow

- Content Collections (`src/content/pages/*.md`, `src/content/posts/*.md`) loaded via `glob` loader
- Schema defined in `src/content.config.ts` with Zod validation
- `data/site.json` contains categories, users, and navigation metadata (used only for reference, not in build)
- Media served from `public/media/images/` and `public/media/documents/`

---

## 4. Review Findings

### 4.1 Critical Issues

#### F-001: Duplicate favicon declarations

**Severity**: Medium
**Files**: `src/layouts/BaseLayout.astro` (lines 19-22), `src/components/Seo.astro` (line 44)

BaseLayout declares favicon links (ico, 32x32, 16x16, apple-touch-icon) AND Seo.astro declares another favicon link (`<link rel="icon" href="/favicon.svg">`). This results in duplicate favicon references in `<head>`.

**Fix**: Remove the favicon link from Seo.astro. Keep all favicon declarations in BaseLayout only.

#### F-002: Duplicate media directories (public/ vs static/)

**Severity**: Medium
**Files**: `public/media/`, `static/media/`

Both `public/` and `static/` contain media files. In Astro, only `public/` is served as static assets. The `static/` directory appears to be a vestige from the migration process. It contains similar (possibly identical) files with some format differences (some `.jpg` in public/ are `.png` in static/).

**Fix**: Audit both directories. If `static/` is unused, remove it entirely and update `.gitignore`. If it serves a purpose, document it.

#### F-003: Google Fonts render-blocking

**Severity**: Medium
**Files**: `src/layouts/BaseLayout.astro` (lines 16-18)

Fonts loaded via `<link>` tags without `font-display: swap`. This blocks first contentful paint on slow connections.

**Fix**: Add `&display=swap` to the Google Fonts URL. Consider preloading the font files or self-hosting.

#### F-004: No 404 page

**Severity**: Medium
**Files**: Missing `src/pages/404.astro`

Astro supports a `404.astro` page for static hosting. Without it, visitors to invalid URLs get the hosting provider's default 404.

**Fix**: Create `src/pages/404.astro` matching the site's layout.

### 4.2 Medium Issues

#### F-005: Legacy color aliases in CSS

**Severity**: Low
**Files**: `src/styles/global.css` (lines 12-18)

Six legacy color aliases defined (forest, moss, clay, river, ink, paper) that duplicate the primary palette. None appear to be used in any component.

**Fix**: Remove legacy aliases to prevent confusion.

#### F-006: Hardcoded data in components

**Severity**: Low
**Files**: `src/pages/index.astro` (lines 19-31), `src/pages/community.astro` (lines 10-23)

Sponsors, partners, stewards, and alumni are hardcoded arrays in page components. Adding or changing any of these requires editing Astro files.

**Fix**: Consider moving to data files in `data/` directory (e.g., `data/team.json`, `data/partners.json`) for easier editing by non-developers.

#### F-007: Sharp dependency in Astro config

**Severity**: Low
**Files**: `astro.config.mjs` (lines 19-21)

Explicit Sharp image service configuration. Astro 6 uses Sharp by default. This is redundant but not harmful.

**Fix**: Remove explicit image service config to use Astro defaults.

#### F-008: Non-prose images not centered

**Severity**: Low
**Files**: `src/styles/global.css` (lines 160-163)

Only `.prose img` is centered via CSS. Images outside prose blocks (e.g., partner logos, hero sections) rely on component-level centering. Inconsistent but functional.

#### F-009: No robots.txt

**Severity**: Low
**Files**: Missing `public/robots.txt`

No robots.txt file. The sitemap is generated, but search engines may not discover it without a robots.txt reference.

**Fix**: Create `public/robots.txt` with sitemap reference.

#### F-010: Mobile nav not tested for screen readers

**Severity**: Medium
**Files**: `src/components/Header.astro`

The mobile navigation uses `aria-expanded` and `aria-label` toggling, which is good. However, the slide-in panel does not trap focus, meaning keyboard users can tab to elements behind the overlay.

**Fix**: Add focus trapping to the mobile panel when open.

### 4.3 Low Issues

#### F-011: Category descriptions incomplete

**Severity**: Low
**Files**: `src/pages/category/[category].astro` (lines 25-30)

Hardcoded descriptions for "User Stories" and "Developer Community" exist, but "Dev Stories" is a category slug (from WP) while the description key is "Developer Community". The mapping between category slugs and display names could be cleaner.

#### F-012: `data/site.json` unused at build time

**Severity**: Low
**Files**: `data/site.json`

The site.json file contains categories, users, and navigation data exported from WordPress, but it is not imported by any component. Navigation is hardcoded in Header/Footer and categories come from content frontmatter. This file is reference-only.

**Fix**: Either use it programmatically or document it as reference data.

#### F-013: Video source MIME type incorrect

**Severity**: Low
**Files**: `src/pages/index.astro` (line 73)

The second `<source>` for the hero video has `type="image/webp"` which is not a video MIME type. This is a fallback image source incorrectly placed inside a `<video>` element.

**Fix**: Remove the webp source or restructure the fallback.

---

## 5. Action Items

### Priority 1 — Must Fix Before Deployment

| ID | Finding | Action | Effort |
|---|---|---|---|
| A-1 | F-001 | Remove duplicate favicon from Seo.astro | S |
| A-2 | F-002 | Audit and remove `static/` directory if vestigial | M |
| A-3 | F-003 | Add `display=swap` to Google Fonts URL | S |
| A-4 | F-004 | Create 404.astro page | S |
| A-5 | F-009 | Create robots.txt with sitemap reference | S |

### Priority 2 — Should Fix (Quality)

| ID | Finding | Action | Effort |
|---|---|---|---|
| A-6 | F-010 | Add focus trap to mobile nav panel | M |
| A-7 | F-005 | Remove legacy CSS color aliases | S |
| A-8 | F-013 | Fix video source MIME type | S |
| A-9 | F-012 | Document or integrate data/site.json | S |

### Priority 3 — Nice to Have (Maintainability)

| ID | Finding | Action | Effort |
|---|---|---|---|
| A-10 | F-006 | Move hardcoded data to JSON files | M |
| A-11 | F-007 | Remove explicit Sharp config | S |
| A-12 | F-011 | Clean up category display name mapping | S |

---

## 6. Performance Baseline

| Metric | Current | Target |
|---|---|---|
| Build time | ~10s (48 pages) | < 15s |
| dist/ size | 64 MB | < 70 MB |
| Google Fonts | 2 families, render-blocking | 2 families, display=swap |
| Image optimization | Lazy loading on content images | Lazy loading + Astro Image component |
| JavaScript bundle | Minimal (only mobile nav script) | < 5KB |

---

## 7. Review Methodology

1. **Static analysis**: Read all source files, identify patterns and issues
2. **Build verification**: `npm run build` passes cleanly
3. **Automated review**: DeepSeek (via opencode) reviews this PRD for completeness
4. **Manual verification**: Spot-check key pages via cloudflared tunnel
5. **Lighthouse audit**: Run against deployed preview URL

---

## 8. Revision Log

| Date | Author | Changes |
|---|---|---|
| 2026-06-12 | Hermes Agent | Initial codebase review PRD with 13 findings, 12 action items |
| 2026-06-12 | DeepSeek Review | Corrected F-003 (invalid — already has display=swap), identified M-001 (community page missing SEO — Critical), M-002 (broken image), M-003 (heading hierarchy), added 8 low-severity findings, 7 new action items (A-13 through A-19). See docs/REVIEW-DEEPSEEK.md for full review. |

---

## 9. Corrected Findings Summary (Post-Review)

### PRD Corrections
- **F-003 REMOVED**: Google Fonts URL already includes `display=swap`. Action A-3 cancelled.
- **F-001 UPDATED**: Seo.astro adds a unique SVG favicon format, not a strict duplicate. Fix: move SVG favicon to BaseLayout.
- **F-002 UPGRADED to Critical**: static/ contains 116MB dead weight + broken image reference in blog content.
- **F-011 UPGRADED to Medium**: Dev Stories is nav-linked and has a generic fallback description.
- **F-009 UPGRADED to Medium**: Sitemap generated but undiscoverable without robots.txt.

### New Findings from Review
- **M-001 (Critical)**: Community page has zero SEO meta tags — no title, charset, viewport, OG tags
- **M-002 (Medium)**: Broken image in blog post (static/media/2020/08/ path doesn't exist)
- **M-003 (Medium)**: Heading hierarchy violation (h1 -> h4 skip on homepage)
- **M-004 through M-011 (Low)**: Various cleanup, accessibility, and performance items

### Updated Action Items

**Priority 1 — Must Fix Before Deployment**

| ID | Finding | Action | Effort |
|---|---|---|---|
| A-1 | F-001 | Move SVG favicon from Seo.astro to BaseLayout | S |
| A-2 | F-002 | Audit/remove static/ dir; fix broken image ref in content | M |
| A-4 | F-004 | Create 404.astro page | S |
| A-5 | F-009 | Create robots.txt with sitemap reference | S |
| **A-13** | **M-001** | **Add Seo component to community.astro** | **S** |
| **A-14** | **M-002** | **Fix broken image path in blog post content** | **S** |
| A-15 | M-003 | Fix heading hierarchy on home page (h4 -> h2) | S |

**Priority 2 — Should Fix**

| ID | Finding | Action | Effort |
|---|---|---|---|
| A-6 | F-010 | Add focus trap to mobile nav panel | M |
| A-7 | F-005 | Remove legacy CSS color aliases | S |
| A-8 | F-013 | Fix video source MIME type | S |
| A-9 | F-012 | Document or integrate data/site.json | S |
| A-12 | F-011 | Fix Dev Stories category description | S |

**Priority 3 — Nice to Have**

| ID | Finding | Action | Effort |
|---|---|---|---|
| A-10 | F-006 | Move hardcoded data to JSON files | M |
| A-11 | F-007 | Remove explicit Sharp config | S |
| A-16 | M-004 | Add static/ to .gitignore (or remove static/) | S |
| A-17 | M-007 | Extract nav data to shared config | M |
| A-18 | M-008 | Add JSON-LD structured data | M |
| A-19 | M-011 | Migrate to Astro Image component | M |
