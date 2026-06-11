# Terrastories Website

Static website for Terrastories, built with Astro 6 and Tailwind CSS 4.

## Stack

- **Framework**: Astro 6.x (static site generation)
- **Styling**: Tailwind CSS 4.x with CSS-first configuration
- **Typography**: @tailwindcss/typography
- **Images**: Sharp (via Astro's built-in image optimization)
- **Sitemap**: @astrojs/sitemap
- **TypeScript**: Strict mode

## Project Structure

```
terrastories-website/
  src/
    content/
      pages/          # 11 Markdown pages (home, how-it-works, community, etc.)
      posts/          # 33 Markdown blog posts
    data/
      nav.ts          # Shared navigation, sponsors, partners, team data
    layouts/
      BaseLayout.astro    # Root HTML shell (fonts, favicons, SEO slot)
      PageLayout.astro    # Generic page wrapper
      PostLayout.astro    # Blog post wrapper
    pages/
      index.astro         # Home page
      community.astro     # Community page (stewards, alumni, contributors)
      [...slug].astro     # Catch-all for pages
      blog/
        index.astro       # Blog listing
        [slug].astro      # Individual blog post
      category/
        [category].astro  # Category filter pages
    components/
      Header.astro        # Desktop + mobile navigation with focus trap
      Footer.astro        # Nav + social + copyright
      Seo.astro           # Meta tags, OG, Twitter, JSON-LD
      PostCard.astro      # Blog post preview card
      PartnerLogo.astro   # Sponsor/partner logo link
      PeopleGrid.astro    # Circle photo grid for team members
    styles/
      global.css          # Tailwind theme + brand colors + typography
    utils/
      category.ts         # Category slug helpers
  public/
    media/
      images/             # Original images (compressed from _originals/)
      documents/          # PDFs (guides, research papers)
    favicon.*             # Favicon variants (ico, svg, png)
    robots.txt            # Search engine directives
  scripts/
    clean-content.py      # Content cleanup pipeline
    compress-media.py     # Image compression
    resize-images.py      # Image resizing with backup
    terrastories-migrate.py  # WordPress-to-Markdown migration script
  docs/
    PRD.md                # Original migration PRD
    PRD-codebase-review.md    # Codebase review findings
    REVIEW-DEEPSEEK.md    # Automated review corrections
    TASKS.md              # Review batch checklist
  data/
    site.json             # Reference data from WordPress export (categories, users, nav)
                          # Not used at build time; kept for reference
```

## Content

- 11 pages: home, how-it-works, community, contact-us, contribute, demo, funding-needs, mailing-list, maintenance, sponsor-us, try-terrastories
- 33 blog posts across 3 categories: User Stories (18), Dev Stories (12), Uncategorized (5)
- 160+ media images (originals only, no WordPress thumbnails)
- Full SEO metadata (title, description, OG image, canonical, JSON-LD per page)

## Commands

```bash
# Development
npm run dev

# Production build
npm run build

# The build outputs to dist/ (not tracked in git)
```

## Deployment

Built for Cloudflare Pages:
1. `npm run build` produces static files in `dist/`
2. Deploy `dist/` to Cloudflare Pages
3. Sitemap auto-generated at `/sitemap-index.xml`
