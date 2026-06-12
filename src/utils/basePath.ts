/**
 * Returns the site base path for the current build.
 * In GitHub Pages builds (ASTRO_BASE=/terrastories-website), this returns '/terrastories-website'.
 * In production/local builds, this returns '' (empty string = root).
 */
export const basePath = (import.meta.env.BASE_URL || '/').replace(/\/$/, '');

/**
 * Prefixes a root-relative path with the base path.
 * basePathOf('/media/images/foo.png') => '/terrastories-website/media/images/foo.png' on GH Pages
 * basePathOf('/media/images/foo.png') => '/media/images/foo.png' in production
 */
export function basePathOf(path: string): string {
  if (!path.startsWith('/')) return path;
  return basePath + path;
}
