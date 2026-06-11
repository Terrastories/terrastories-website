# PRD: Terrastories Static Website Migration

| Field | Value |
|---|---|
| **Status** | In Progress |
| **Created** | 2026-06-11 |
| **Author** | Hermes Agent |
| **Epic** | Terrastories V2 Website |
| **Repo** | `Terrastories/terrastories-website` |
| **Stakeholders** | Terrastories team |

---

## 1. Problem Statement

Terrastories currently runs on WordPress at `terrastories.app`. The site is content-heavy (44 pages/posts, 606 media files) with minimal interactivity. WordPress adds operational overhead, security surface, and performance costs that are unnecessary for a site that is essentially static marketing content. We need to migrate to a fast, secure, low-maintenance static site that preserves all existing content and SEO equity.

## 2. Goals & Non-Goals

### Goals

| ID | Goal | Success Metric |
|---|---|---|
| G-1 | Migrate all WordPress content to a static site framework | All 44 pages/posts render correctly with all media |
| G-2 | Achieve top-tier performance | Lighthouse Performance score >= 95 |
| G-3 | Preserve SEO equity | All existing URLs redirect or resolve; meta tags preserved |
| G-4 | Enable zero-cost hosting | Site deploys to Cloudflare Pages or similar free tier |
| G-5 | Make content editable by non-developers | Markdown files that anyone can edit via GitHub |
| G-6 | Achieve a publicly accessible preview | Cloudflared tunnel URL for team review |

### Non-Goals

- Rebuilding the Terrastories app itself (this is the marketing/info site only)
- Adding a CMS or admin dashboard (Markdown + GitHub is sufficient)
- Multilingual support in Phase 1 (future consideration)
- User authentication or dynamic features
- Preserving the Mailchimp embedded form (will be replaced with a link)

---

## 3. Background & Context

### Current State

- **Source**: WordPress site at `terrastories.app` with public REST API
- **Content exported**: All content scraped and converted to Markdown via custom pipeline
- **Export location**: `/home/coder/projects/terrastories-website/`
- **Repository**: `Terrastories/terrastories-website` (private, GitHub)

### Content Inventory

| Type | Count | Notes |
|---|---|---|
| Pages | 11 | home, how-it-works, community, contact-us, contribute, demo, funding-needs, mailing-list, maintenance, sponsor-us, try-terrastories |
| Blog posts | 33 | Across 3 categories: User Stories (18), Dev Stories (12), Uncategorized (5) |
| Media images | 606 | Including all WordPress thumbnail sizes |
| Documents | 4 | PDFs (guides, research papers) |
| Authors | 2 | rkemper, Terrastories |

### Navigation Structure (from current site)

**Top Nav**: How It Works | Documentation | Demo | User Stories | Developer Community | Contact Us | Sponsor Us | Explore Terrastories

**Footer Nav**:
- How It Works > Videos, Methodology, Practical Guide, Try Terrastories
- Documentation (external link to docs.terrastories.app)
- Demo
- User Stories (blog category filter)
- Developer Community > Dev Stories, Contribute
- Contact Us
- Sponsor Us

### Technology Decision: Astro

Selected Astro over Hugo, Next.js, Eleventy, and others based on:
- Zero JavaScript by default (fastest page loads)
- Native Markdown + MDX with type-safe Content Collections
- Built-in image optimization
- Framework-agnostic (can add React/Vue/Svelte components later)
- Perfect Lighthouse scores out of the box
- Free hosting on Cloudflare Pages
- Most popular new SSG in 2026 with strongest momentum

**Stack**: Astro 6 + Tailwind CSS, deployed to Cloudflare Pages

---

## 4. Requirements

### FR-001: Content Cleanup

**Priority**: High

Before building the Astro site, the exported Markdown must be cleaned:

| Issue | Occurrences | Fix |
|---|---|---|
| Escaped markdown (`\\*\\*text\\*\\*` instead of `**text**`) | 126 | Unescape all backslash-escaped markdown syntax |
| HTML entities (`&#8217;`, `&hellip;`, `&nbsp;`, etc.) | 31 | Decode to proper UTF-8 characters |
| WordPress "read-more" HTML in excerpt field | 21 | Strip all raw HTML from excerpt frontmatter |
| Absolute WP URLs in `featured_image` frontmatter | 34 | Map `https://terrastories.app/wp-content/uploads/YYYY/MM/filename.ext` to `/media/images/{id}_{filename.ext}` using the media ID mapping |
| Internal WP links in markdown body | 62 | Rewrite `https://terrastories.app/{slug}/` to `/{slug}` |
| Empty heading markers (bare `#` on its own line) | 22 | Remove these WordPress artifacts |
| Mailing list page embedded form | 1 | Replace with link to external Mailchimp signup |
| Duplicate WP thumbnail image sizes | ~400 | Keep only original (largest) images, remove thumbnails |

**Acceptance criteria**:
- Zero escaped markdown remains (`grep -rn '\\*\\*' content/` returns nothing)
- Zero HTML entities remain (`grep -rn '&#' content/` returns nothing)
- Zero raw HTML in excerpts (`grep -rn '<p class' content/` returns nothing)
- All featured_image paths are local (`grep -rn 'featured_image: https://' content/` returns nothing)
- All internal links are relative
- Media directory contains only original images (no `150x150`, `300x200`, etc. suffixes)

### FR-002: Astro Project Scaffolding

**Priority**: High

Create a new Astro project in the same repository that uses the cleaned content:

| Requirement | Detail |
|---|---|
| Framework | Astro 6.x |
| Styling | Tailwind CSS |
| Content | Astro Content Collections with TypeScript schemas |
| Routing | File-based routing matching existing URL structure |
| Image handling | Astro's built-in `<Image />` component with optimization |
| Sitemap | `@astrojs/sitemap` integration |
| SEO | Per-page meta tags from frontmatter (seo_title, seo_description, og_image) |

**Project structure**:
```
terrastories-website/
  src/
    content/
      config.ts
      pages/          # 11 pages
      posts/          # 33 posts
    layouts/
      BaseLayout.astro
      PageLayout.astro
      PostLayout.astro
    pages/
      index.astro
      [...slug].astro
      blog/
        index.astro
        [slug].astro
      category/
        [category].astro
    components/
      Header.astro
      Footer.astro
      PostCard.astro
      Seo.astro
    styles/
      global.css
  public/
    media/
      images/         # Original images only
      documents/      # PDFs
  astro.config.mjs
  tailwind.config.mjs
  package.json
```

**Content Collection schemas**:

Pages collection:
```typescript
{
  title: string;
  slug: string;
  date: Date;
  modified: Date;
  author: string;
  excerpt: string;
  seo_title: string;
  seo_description: string;
  featured_image?: string;
  og_image?: string;
  canonical?: string;
}
```

Posts collection (extends pages):
```typescript
{
  // ... all page fields
  categories: string[];
}
```

**Acceptance criteria**:
- `npm run build` completes without errors
- `npm run dev` serves the site locally
- All 11 pages resolve at their correct URLs (`/how-it-works`, `/community`, etc.)
- All 33 blog posts resolve at `/blog/{slug}`
- Category pages work at `/category/user-stories`, `/category/dev-stories`
- Images load correctly
- Navigation matches the current site structure

### FR-003: Public Preview via Cloudflared

**Priority**: High

Expose the dev server via a cloudflared tunnel URL so the team can review the site.

**Acceptance criteria**:
- A cloudflared tunnel is running and serving the Astro dev server
- A public `*.trycloudflare.com` URL is accessible
- The team can browse all pages and posts

### FR-004: SEO Preservation

**Priority**: Medium

| Requirement | Detail |
|---|---|
| Meta titles | Use `seo_title` from frontmatter in `<title>` |
| Meta descriptions | Use `seo_description` in `<meta name="description">` |
| Open Graph | Use `og_image` for `<meta property="og:image">` |
| Canonical URLs | Set canonical URL for each page |
| Sitemap | Auto-generated `sitemap.xml` |
| 301 redirects | Old WP URLs redirect to new paths if different |

---

## 5. Phased Plan

### Phase 1: Content Cleanup
- **Deliverable**: Cleaned Markdown files + deduplicated media
- **Agent**: Codex (GPT-5.5)
- **Steps**:
  1. Write a Python cleanup script (`scripts/clean-content.py`)
  2. Run against all 44 files in `content/`
  3. Deduplicate media (keep originals, remove WP thumbnails)
  4. Verify all acceptance criteria pass
  5. Review, fix any issues, commit
- **Estimated time**: 15-20 minutes

### Phase 2: Astro Project Scaffolding
- **Deliverable**: Working Astro site with all content
- **Agent**: Codex (GPT-5.5)
- **Steps**:
  1. Initialize Astro project (`npm create astro@latest`)
  2. Add Tailwind, sitemap integrations
  3. Set up Content Collections with schemas
  4. Build BaseLayout, PageLayout, PostLayout
  5. Build Header, Footer, PostCard, Seo components
  6. Wire up routing (pages, blog, categories)
  7. Move cleaned content into Astro's content directory
  8. Move media into `public/`
  9. Verify `npm run build` passes
- **Estimated time**: 20-30 minutes

### Phase 3: Public Preview
- **Deliverable**: Live cloudflared URL
- **Steps**:
  1. Start Astro dev server
  2. Start cloudflared tunnel pointing to dev server
  3. Share URL with team
- **Estimated time**: 2 minutes

---

## 6. Risks & Mitigations

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| R-1 | Featured image URL to local path mapping may not always match (media ID vs filename) | Medium | Build a lookup table from `data/site.json`; fallback to original WP URL |
| R-2 | Some markdown may have edge-case escaping patterns | Low | Automated verification checks after cleanup |
| R-3 | Astro version compatibility with Codex-generated code | Low | Pin Astro version in package.json |
| R-4 | Cloudflared tunnel stability for review | Low | Tunnel is temporary; production will use Cloudflare Pages |

---

## 7. Testing Strategy

| What | How |
|---|---|
| Content cleanup completeness | Grep-based assertions (zero escaped markdown, zero HTML entities, zero absolute URLs) |
| Build success | `npm run build` exits with code 0 |
| Page rendering | Manual verification via cloudflared URL |
| Image loading | Check that all `media/images/` references resolve to actual files |
| SEO tags | View source on each page, verify meta tags present |

---

## 8. Definition of Done

- [ ] All content cleanup acceptance criteria pass (FR-001)
- [ ] Astro project builds successfully (FR-002)
- [ ] All 44 pages/posts render at correct URLs
- [ ] Navigation works
- [ ] Images display correctly
- [ ] SEO meta tags present on all pages
- [ ] Public cloudflared URL accessible
- [ ] All changes committed to `main` branch

---

## 9. Change Log

| Date | Author | Change |
|---|---|---|
| 2026-06-11 | Hermes Agent | Initial PRD created |
