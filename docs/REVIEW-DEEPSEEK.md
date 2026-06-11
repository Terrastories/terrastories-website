# DeepSeek Review: Terrastories Website Codebase Review

| Field | Value |
|---|---|
| **Status** | Complete |
| **Date** | 2026-06-12 |
| **Reviewer** | DeepSeek (via Hermes Agent) |
| **PRD Reviewed** | `docs/PRD-codebase-review.md` |
| **Verdict** | PRD is mostly accurate but misses 1 critical bug and several medium issues |

---

## 1. PRD Accuracy Verification (F-001 through F-013)

### F-001: Duplicate favicon declarations — CONFIRMED

**PRD Claim**: BaseLayout declares favicon links (ico, 32x32, 16x16, apple-touch-icon) AND Seo.astro declares another favicon link.

**Verification**:
- `src/layouts/BaseLayout.astro` lines 19-22: Declares `favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png` — **CONFIRMED**
- `src/components/Seo.astro` line 44: `<link rel="icon" href="/favicon.svg" />` — **CONFIRMED**

The SVG favicon in Seo.astro is actually a *different* favicon format than the ones in BaseLayout (ICO/PNG), so technically both sets serve a purpose. However, having favicon declarations split across two components is poor organization. The SVG favicon (line 44) should be moved to BaseLayout alongside the others.

**PRD Severity**: Medium — **AGREE**
**Correction**: The PRD should note that Seo.astro adds a *fifth* favicon format (SVG), not a strict duplicate. The fix should be to move the SVG favicon link to BaseLayout, not just delete it.

---

### F-002: Duplicate media directories (public/ vs static/) — CONFIRMED

**PRD Claim**: Both `public/` and `static/` contain media files. `static/` appears vestigial.

**Verification**:
- `public/` contains 62MB of media (favicon files + `media/` directory)
- `static/` contains 116MB of media (with `media/images/` and `media/documents/`)
- Many files differ in format (e.g., `.jpg` in public/ vs `.png` in static/)
- **Critical finding**: One content file references `/static/media/...` path: `src/content/posts/act-partakes-in-ruby-for-good-2018-to-develop-offline-geostorytelling-app-terrastories-for-remote-communities.md` line 48 references `/static/media/2020/08/terrastories-team-1024x768.jpg`
- Neither `public/media/images/2020/` nor `static/media/2020/` directories exist — **this is a broken image**

**PRD Severity**: Medium — **UPGRADE TO CRITICAL**  
The static/ directory is not just vestigial; it contains content that may have been lost during migration. The broken image reference in the blog post is a real user-facing bug.

---

### F-003: Google Fonts render-blocking — INCORRECT (Already Fixed)

**PRD Claim**: Fonts loaded via `<link>` tags without `font-display: swap`.

**Verification**: `src/layouts/BaseLayout.astro` line 18:
```
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Oswald:wght@400;500;600&display=swap" rel="stylesheet" />
```

The URL already includes `&display=swap`. **The PRD finding is incorrect.** This is not a current issue.

**PRD Severity**: Medium — **NOT APPLICABLE** (already fixed)
**Correction**: Remove F-003 and action item A-3 from the PRD entirely.

---

### F-004: No 404 page — CONFIRMED

**PRD Claim**: Missing `src/pages/404.astro`.

**Verification**:
- `ls src/pages/` shows: `[...slug].astro`, `blog/`, `category/`, `community.astro`, `index.astro`
- No `404.astro` exists — **CONFIRMED**

**PRD Severity**: Medium — **AGREE**

---

### F-005: Legacy color aliases in CSS — CONFIRMED

**PRD Claim**: Six legacy color aliases (forest, moss, clay, river, ink, paper) that duplicate the primary palette.

**Verification**: `src/styles/global.css` lines 12-18:
```css
--color-forest: #09697e;   /* = teal */
--color-moss: #d97b29;     /* = orange */
--color-clay: #d97b29;     /* = orange (duplicate!) */
--color-river: #d97b29;    /* = orange (duplicate!) */
--color-ink: #3a3a3a;      /* = body */
--color-paper: #ffffff;     /* = white */
```

**CONFIRMED**. Also notable: moss, clay, and river are all the same color (#d97b29), suggesting these were distinct colors in the original design that got collapsed during migration.

**PRD Severity**: Low — **AGREE**

---

### F-006: Hardcoded data in components — CONFIRMED

**PRD Claim**: Sponsors, partners, stewards, and alumni are hardcoded arrays.

**Verification**:
- `src/pages/index.astro` lines 19-31: `sponsors` (1 item) and `partners` (8 items) arrays — **CONFIRMED**
- `src/pages/community.astro` lines 10-23: `stewards` (5 items) and `alumni` (4 items) arrays — **CONFIRMED**

**PRD Severity**: Low — **AGREE**

---

### F-007: Sharp dependency in Astro config — CONFIRMED

**PRD Claim**: Explicit Sharp image service configuration is redundant in Astro 6.

**Verification**: `astro.config.mjs` lines 18-22:
```js
image: {
  service: {
    entrypoint: 'astro/assets/services/sharp',
  },
},
```

**CONFIRMED**. Astro 6 defaults to Sharp. This config is redundant.

**PRD Severity**: Low — **AGREE**

---

### F-008: Non-prose images not centered — CONFIRMED

**PRD Claim**: Only `.prose img` is centered via CSS. Images outside prose blocks rely on component-level centering.

**Verification**: `src/styles/global.css` lines 160-163:
```css
.prose img {
  margin-left: auto;
  margin-right: auto;
}
```

**CONFIRMED**. However, this is a design choice, not a bug. Components handle their own layout.

**PRD Severity**: Low — **AGREE** (cosmetic only)

---

### F-009: No robots.txt — CONFIRMED

**PRD Claim**: No `public/robots.txt` file.

**Verification**: `ls public/robots.txt` returns nothing. **CONFIRMED**.

**PRD Severity**: Low — **AGREE**

---

### F-010: Mobile nav not tested for screen readers — PARTIALLY CONFIRMED

**PRD Claim**: Mobile nav panel does not trap focus.

**Verification**: `src/components/Header.astro`:
- Line 99: `aria-expanded="false"` — present, correct
- Lines 216/228: `aria-expanded` toggles between "false"/"true" — correct
- Lines 217/229: `aria-label` toggles between "Open menu"/"Close menu" — correct
- Line 243: Escape key handler closes menu — correct
- Line 239: Overlay click closes menu — correct
- Line 231: Body scroll lock (`overflow: hidden`) — correct

**However**, there is **no focus trap** when the panel is open. A keyboard user can tab past the panel to elements behind the overlay. This is an accessibility gap.

**PRD Severity**: Medium — **AGREE**

---

### F-011: Category descriptions incomplete — CONFIRMED

**PRD Claim**: Hardcoded descriptions exist but slug-to-name mapping could be cleaner.

**Verification**: `src/pages/category/[category].astro` lines 25-30:
```js
const descriptions: Record<string, string> = {
  'User Stories': '...',
  'Developer Community': '...',
  'Field Notes': '...',
};
```

The `titleFromSlug` function (line 8) converts `dev-stories` to "Dev Stories", but the descriptions key is "Developer Community" — a mismatch. The description for "Dev Stories" will fall through to the default `Terrastories posts in the ${title} category.`

**CONFIRMED**. The mapping is inconsistent.

**PRD Severity**: Low — **UPGRADE TO MEDIUM**
The "Dev Stories" category is prominently linked from the main navigation, so its missing description is user-visible.

---

### F-012: data/site.json unused at build time — CONFIRMED

**PRD Claim**: `data/site.json` is not imported by any component.

**Verification**: `grep -rn "data/site.json" src/` returns no results. **CONFIRMED**.

**PRD Severity**: Low — **AGREE**

---

### F-013: Video source MIME type incorrect — CONFIRMED

**PRD Claim**: Second `<source>` for hero video has `type="image/webp"`.

**Verification**: `src/pages/index.astro` line 73:
```html
<source src="/media/images/27_terrastories.webp" type="image/webp" />
```

**CONFIRMED**. A `<source>` inside `<video>` with `type="image/webp"` is invalid. Browsers will reject this source. The webp file itself is likely an animated image, not a video. The fallback `<img>` on lines 74-78 will handle this, but the webp source should be removed.

**PRD Severity**: Low — **AGREE**

---

## 2. Missing Findings (Issues the PRD Did Not Capture)

### M-001: Community page has NO SEO meta tags — CRITICAL

**Files**: `src/pages/community.astro` (lines 26-31), `src/layouts/BaseLayout.astro` (lines 6-8)

**Description**: The community page (`src/pages/community.astro`) passes `title`, `description`, `canonical`, and `ogImage` props to `BaseLayout`, but `BaseLayout` only accepts `bodyClass` (line 7-8). The community page does **not** import or use the `Seo` component. As a result:
- No `<title>` tag
- No `<meta charset="utf-8">`
- No `<meta name="viewport">`
- No `<meta name="description">`
- No Open Graph tags
- No Twitter Card tags
- No canonical URL

This is a **critical SEO failure** on a page linked from the main navigation.

**Severity**: **Critical**

---

### M-002: Broken image in blog post content — MEDIUM

**File**: `src/content/posts/act-partakes-in-ruby-for-good-2018-to-develop-offline-geostorytelling-app-terrastories-for-remote-communities.md` (line 48)

**Description**: This post references `/static/media/2020/08/terrastories-team-1024x768.jpg`. Astro serves static files from `public/`, not `static/`. Additionally, neither `public/media/2020/` nor `static/media/2020/` directories exist — the image file is missing entirely. This will render as a broken image on the live page.

**Severity**: **Medium**

---

### M-003: Heading hierarchy violation (h1 → h4 skip) — MEDIUM

**File**: `src/pages/index.astro` (lines 41-44, lines 109-110)

**Description**: The home page uses `<h1>` followed directly by `<h4>` (lines 41→44 and 109→110), skipping h2 and h3. This violates WCAG 2.1 SC 1.3.1 (Info and Relationships) which requires logical heading hierarchy. Screen reader users navigate by heading levels and expect a sequential order.

**Severity**: **Medium** (accessibility)
**Fix**: Change `<h4>` to `<h2>` on lines 44 and 110. Use CSS for visual sizing independent of semantic heading level.

---

### M-004: static/ directory missing from .gitignore — LOW

**File**: `.gitignore`

**Description**: The `.gitignore` file includes `node_modules/`, `dist/`, `.astro/`, `.DS_Store`, `_originals/` but does NOT include `static/`. If the static directory is vestigial (per F-002), it should be gitignored. If not, its 116MB of files is tracked in git, bloating the repository size.

**Severity**: **Low**

---

### M-005: No `<meta name="generator">` or build-time cache-busting — LOW

**Files**: `src/layouts/BaseLayout.astro`

**Description**: The site has no mechanism for cache-busting static assets referenced in the HTML (CSS, JS, images). For a static site deployed to Cloudflare Pages, stale caches could serve outdated assets after redeployment. Astro handles CSS/JS bundling with content hashes automatically, but manually referenced images (e.g., nav-logo.png) will be cached indefinitely.

**Severity**: **Low** (Astro's build pipeline handles most of this)

---

### M-006: Category page queries all posts twice — LOW

**File**: `src/pages/category/[category].astro` (lines 10-22)

**Description**: `getStaticPaths()` calls `getCollection('posts')` to build the category list (line 11), and then the page body calls `getCollection('posts')` again to filter and display posts (line 20). This is redundant. The posts could be passed as props from `getStaticPaths()`.

**Severity**: **Low** (performance — only affects build time, not runtime)

---

### M-007: Footer nav duplication with Header — LOW (Code Quality)

**Files**: `src/components/Header.astro`, `src/components/Footer.astro`

**Description**: Navigation items are defined independently in both Header (lines 1-32) and Footer (lines 1-51). This violates DRY. If a nav item changes, it must be updated in two places. Consider extracting nav data to a shared config file (e.g., `src/data/nav.ts`).

**Severity**: **Low**

---

### M-008: No structured data (JSON-LD) — LOW

**Files**: `src/components/Seo.astro`, `src/layouts/PostLayout.astro`

**Description**: The Seo component handles basic meta tags and OG/Twitter cards, but there is no JSON-LD structured data (Schema.org). Blog posts should include `Article` or `BlogPosting` schema. The organization should have `Organization` schema. This would improve search engine rich results.

**Severity**: **Low** (SEO enhancement)

---

### M-009: Non-unique `aria-label` on footer nav sections — LOW

**File**: `src/components/Footer.astro` (lines 109, 139)

**Description**: Footer has `<nav aria-label="Footer navigation left">` and `<nav aria-label="Footer navigation right">`. The "left"/"right" labels are spatial and won't make sense on mobile where both columns stack vertically. Consider more descriptive labels like "Footer: Resources" and "Footer: Community".

**Severity**: **Low** (accessibility)

---

### M-010: Button elements lack accessible names for icon-only contexts — LOW

**File**: `src/components/Header.astro` (lines 95-107)

**Description**: The burger menu button has both `aria-label="Open menu"` (line 98) and a child `<span class="sr-only">Toggle navigation</span>` (line 101). These are redundant — `aria-label` is sufficient. The sr-only text says "Toggle navigation" while aria-label says "Open menu", which could confuse screen readers about which takes precedence.

**Severity**: **Low** (accessibility)

---

### M-011: Content images not using Astro Image component — LOW

**Files**: Multiple components and pages

**Description**: All images use raw `<img>` tags with static paths rather than Astro's `<Image>` component. The Astro Image component provides automatic width/height, format optimization (WebP/AVIF), responsive srcsets, and lazy loading. The site is missing significant performance optimization by not using it. For example:
- `src/pages/index.astro` lines 88-89: UN goal images are PNG, unoptimized
- `src/components/Header.astro` line 47: nav-logo.png loaded at full resolution
- `src/components/PeopleGrid.astro` line 15-19: portrait images loaded without optimization

**Severity**: **Low** (performance enhancement — the site is small enough that this isn't critical)

---

## 3. Severity Assessment Summary

| ID | Finding | PRD Severity | Review Severity | Rationale |
|---|---|---|---|---|
| F-001 | Duplicate favicon declarations | Medium | Low | Not truly duplicate (different formats); cosmetic organization issue |
| F-002 | Duplicate media directories | Medium | **Critical** | Contains broken image reference + 116MB dead weight |
| F-003 | Google Fonts render-blocking | Medium | **N/A (Invalid)** | Already has `display=swap`; PRD finding is wrong |
| F-004 | No 404 page | Medium | Medium | Standard deployment gap |
| F-005 | Legacy color aliases | Low | Low | Cleanup task |
| F-006 | Hardcoded data | Low | Low | Maintainability concern |
| F-007 | Sharp config redundant | Low | Low | Cleanup task |
| F-008 | Non-prose image centering | Low | Low | Design choice, not bug |
| F-009 | No robots.txt | Low | Medium | SEO — sitemap is generated but undiscoverable |
| F-010 | Mobile nav focus trap | Medium | Medium | Accessibility gap |
| F-011 | Category descriptions | Low | Medium | "Dev Stories" nav-linked category has generic fallback |
| F-012 | data/site.json unused | Low | Low | Documentation task |
| F-013 | Video MIME type | Low | Low | Cosmetic — fallback img handles it |
| **M-001** | **Community page missing all SEO** | — | **Critical** | No title, charset, viewport, description, or OG tags |
| **M-002** | **Broken image in blog post** | — | **Medium** | User-facing broken image |
| **M-003** | **Heading hierarchy violation** | — | **Medium** | WCAG 2.1 AA accessibility issue |
| **M-004** | static/ not gitignored | — | Low | Repository bloat |
| **M-005** | No cache-busting for manual refs | — | Low | Astro handles most of this |
| **M-006** | Category page double query | — | Low | Build-time only |
| **M-007** | Nav duplication Header/Footer | — | Low | DRY violation |
| **M-008** | No JSON-LD structured data | — | Low | SEO enhancement |
| **M-009** | Non-unique footer aria-labels | — | Low | Accessibility minor |
| **M-010** | Redundant burger a11y labels | — | Low | Accessibility minor |
| **M-011** | Not using Astro Image component | — | Low | Performance enhancement |

---

## 4. Completeness Check

### PRD Action Items Assessment

| Action | Finding | Effort | Assessment |
|---|---|---|---|
| A-1 | Remove duplicate favicon | S | **Correct** — should clarify: move SVG to BaseLayout |
| A-2 | Audit/remove static/ | M | **Correct** — but should also fix broken image ref in content |
| A-3 | Add display=swap | S | **INVALID** — already has display=swap; remove this action |
| A-4 | Create 404.astro | S | **Correct** |
| A-5 | Create robots.txt | S | **Correct** |
| A-6 | Focus trap mobile nav | M | **Correct** — effort estimate reasonable |
| A-7 | Remove legacy CSS aliases | S | **Correct** |
| A-8 | Fix video MIME type | S | **Correct** |
| A-9 | Document/integrate site.json | S | **Correct** |
| A-10 | Move data to JSON | M | **Correct** — but this is subjective; could stay as-is |
| A-11 | Remove Sharp config | S | **Correct** |
| A-12 | Category display names | S | **Correct** — but effort may be S (just fix the descriptions map) |

### Missing Action Items

| Action | Finding | Effort | Priority |
|---|---|---|---|
| **A-13** | **Fix community page: add Seo component** | S | **P1 — Must Fix** |
| **A-14** | **Fix broken image in blog post** | S | **P1 — Must Fix** |
| **A-15** | **Fix heading hierarchy on home page** | S | **P2 — Should Fix** |
| A-16 | Add static/ to .gitignore | S | P2 |
| A-17 | Extract nav data to shared config | M | P3 |
| A-18 | Add JSON-LD structured data | M | P3 |
| A-19 | Migrate to Astro Image component | M | P3 |

---

## 5. Architecture Review

### Component Architecture Assessment: SOUND

The overall architecture is well-structured for an Astro static site:

**Strengths**:
- Clean separation of layouts (Base → Page/Post) with proper slot usage
- Seo component handles meta tags centrally (except the community page bug)
- Content Collections with Zod validation ensures type-safe content
- Minimal JavaScript (only mobile nav script) — excellent for performance
- Proper use of Astro's `glob` loader for content

**Structural Issues**:

1. **BaseLayout accepts `bodyClass` but community.astro passes `title`/`description`/`canonical`/`ogImage`** — These props are silently ignored. BaseLayout should either accept and use these props, or community.astro should use Seo component like other pages. **Recommendation**: community.astro should follow the same pattern as other pages (use Seo component in seo slot).

2. **Navigation data duplication** — Header and Footer define identical nav structures. This should be extracted to `src/data/nav.ts`.

3. **Content schema has WordPress artifacts** — Fields like `featured_image_id`, `status`, `type`, `link` are WordPress migration artifacts that serve no purpose in the static site. Consider cleaning these from the schema once content is verified.

4. **Layout nesting is flat** — PageLayout and PostLayout both extend BaseLayout directly. This is correct for this site's scale. No structural changes needed.

5. **CSS architecture is minimal** — Single `global.css` with Tailwind. For this site's size, this is appropriate. No CSS modules or scoped styles needed beyond what's already in Header.astro.

### Recommended Architecture Changes

1. **Immediate**: Fix community.astro to use `<Seo slot="seo" ... />` pattern
2. **Short-term**: Extract nav data to shared module
3. **Optional**: Consider a `src/data/` directory for partners, team members, and nav data
4. **Optional**: Adopt Astro `<Image>` component for automatic optimization

---

## 6. Summary

### Critical Issues (Must Fix Before Deployment)
1. **M-001**: Community page has zero SEO meta tags — no title, charset, viewport, description, or OG tags
2. **F-002**: static/ directory contains 116MB of dead weight + broken image reference in content

### PRD Corrections Required
1. **F-003 is invalid** — Google Fonts URL already includes `display=swap`
2. **F-001 is partially wrong** — Seo.astro adds a unique SVG favicon, not a strict duplicate
3. **F-011 severity should be Medium**, not Low — affects a nav-linked category page
4. **F-009 severity should be Medium**, not Low — sitemap exists but is undiscoverable without robots.txt

### Overall Assessment
The PRD captured 13 findings which is thorough. One finding (F-003) is invalid, and one critical bug (M-001: community page SEO) was missed. The codebase is well-architected for a small Astro site. The remaining issues are mostly cleanup tasks, accessibility improvements, and SEO enhancements. After fixing the two critical issues, the site should be deployment-ready.
