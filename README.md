<div align="center">

<img src="public/media/images/nav-logo.png" alt="Terrastories" width="300">

# Terrastories Website

[![Astro](https://img.shields.io/badge/Astro-6.0-BC52EE?style=for-the-badge&logo=astro&logoColor=white)](https://astro.build)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.0-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**Static website for Terrastories — a free and open-source geostorytelling application built for communities to map, protect, and share place-based oral histories.**

[Live Site](https://terrastories.app) · [GitHub Pages](https://terrastories.github.io/terrastories-website) · [Report Bug](https://github.com/Terrastories/terrastories-website/issues) · [Request Feature](https://github.com/Terrastories/terrastories-website/issues)

</div>

---

## About

Terrastories is a geostorytelling application built to enable Indigenous and other local communities to locate and map their own oral storytelling traditions about places of significant meaning or value to them. Community members can add places and stories through a user-friendly interface, and make decisions about designating certain stories as private or restricted. Terrastories works both online and offline, so that remote communities can access the application entirely without needing internet connectivity.

This repository contains the **static website** for the Terrastories project — built with Astro and Tailwind CSS — serving as the project's public face, blog, documentation hub, and community portal.

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | [Astro 6](https://astro.build) — static site generation |
| Styling | [Tailwind CSS 4](https://tailwindcss.com) — utility-first CSS |
| Typography | [@tailwindcss/typography](https://tailwindcss.com/docs/typography-plugin) — prose styling |
| Images | [Sharp](https://sharp.pixelplumbing.com/) — image optimization |
| Sitemap | [@astrojs/sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/) — auto-generated |
| Content | [Astro Content Collections](https://docs.astro.build/en/guides/content-collections/) — Markdown + type-safe queries |
| TypeScript | Strict mode throughout |

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Terrastories/terrastories-website.git
cd terrastories-website

# Install dependencies
npm install

# Start development server
npm run dev

# Production build
npm run build

# Preview production build locally
npm run preview
```

The dev server runs at `http://localhost:4321`. Content hot-reloads on save.

## 📁 Project Structure

```
terrastories-website/
├── src/
│   ├── components/       # Header, Footer, SEO, PostCard, PartnerLogo, PeopleGrid
│   ├── layouts/          # BaseLayout, PageLayout, PostLayout
│   ├── pages/            # index.astro, community.astro, 404.astro, [slug].astro
│   ├── content/
│   │   ├── pages/        # 11 Markdown content pages
│   │   └── posts/        # 33 Markdown blog posts
│   ├── data/
│   │   └── nav.ts        # Navigation, sponsors, partners, social links
│   ├── styles/
│   │   └── global.css    # Tailwind theme, brand colors, typography
│   └── utils/            # Category helpers, base path utility
├── public/
│   └── media/            # 160+ images, documents, favicons
├── scripts/              # Content migration & image processing utilities
├── astro.config.mjs      # Astro configuration
├── package.json          # Dependencies and scripts
└── README.md
```

## 🚢 Deployment

### Production (terrastories.app)
Deployed to Cloudflare Pages. Every push to `main` triggers a production build:

```bash
npm run build   # Outputs to dist/
```

### GitHub Pages Preview
A subpath preview is deployed at `https://terrastories.github.io/terrastories-website` via GitHub Actions workflow:

```bash
ASTRO_BASE=/terrastories-website npm run build
```

The `ASTRO_BASE` environment variable activates subpath support — all asset URLs, images, and links are automatically prefixed with `/terrastories-website/` while canonical URLs remain set to `terrastories.app`.

## 🙏 Acknowledgments

Terrastories is sponsored by:

- **[Awana Digital](https://awana.digital)** — Design, mapping, and technology for social and environmental justice

---

<div align="center">

Built with ❤️ by the Terrastories community. [Become a partner →](https://terrastories.app/sponsor-us)

</div>
