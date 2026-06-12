import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import { unified } from '@astrojs/markdown-remark';

const ghBase = process.env.ASTRO_BASE || undefined;

const rootRelativeUrlAttributes = ['href', 'src'];

function withBasePath(url, base) {
  if (!base || typeof url !== 'string' || !url.startsWith('/') || url.startsWith('//')) {
    return url;
  }

  return `${base.replace(/\/$/, '')}${url}`;
}

function rehypeBasePathLinks({ base }) {
  return (tree) => {
    function visit(node) {
      if (node?.type === 'element' && node.properties) {
        for (const attr of rootRelativeUrlAttributes) {
          node.properties[attr] = withBasePath(node.properties[attr], base);
        }
      }

      if (Array.isArray(node?.children)) {
        for (const child of node.children) {
          visit(child);
        }
      }
    }

    visit(tree);
  };
}

export default defineConfig({
  site: 'https://terrastories.app',
  base: ghBase,
  server: {
    allowedHosts: true,
  },
  preview: {
    allowedHosts: true,
  },
  integrations: [
    // Skip sitemap for GitHub Pages subpath builds to avoid /terrastories-website/ URLs
    // conflicting with canonical terrastories.app URLs
    ...(!ghBase ? [sitemap()] : []),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    processor: unified({
      rehypePlugins: ghBase ? [[rehypeBasePathLinks, { base: ghBase }]] : [],
    }),
    shikiConfig: {
      theme: 'github-light',
    },
  },
});
