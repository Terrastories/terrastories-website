# Media Optimization Plan — Terrastories Website

## Current State (Post Initial Compression)

- **145 images** totaling **~75 MB** (after restoring animated GIF)
- **58 images** are over 1200px wide (max: 2880px, avg: 1130px)
- **1 animated GIF** (27_terrastories.gif): 1280x720, 31 frames, **11 MB**
- **1 static GIF** (160_terrastories-1920x1080-768x432-1.gif): 768x432, 1 frame, 182 KB (should be PNG/JPEG)
- Width distribution: 33 images are 1600+px, 25 are 1201-1600px

## Problem

1. **Animated GIFs were destroyed** by Pillow's `save()` — it only kept frame 0
2. **Images are served at full WordPress export resolution** (up to 2880px) — far larger than needed
3. **No responsive images** — mobile devices download the same 2560px image as desktop
4. **GIF format** is inefficient for 11MB — should be MP4 or animated WebP

## Strategy

### Phase 1: Restore and Protect GIFs
- Restore `27_terrastories.gif` from git (DONE — 31 frames recovered)
- Mark GIFs as off-limits for Pillow compression in `scripts/compress-media.py`
- The `160_*` GIF is actually a single frame — convert to JPEG

### Phase 2: Convert Animated GIF to MP4 + WebP Fallback
- Use `ffmpeg` to convert `27_terrastories.gif` (11MB) to:
  - `27_terrastories.webp` (animated WebP, ~1-2MB)
  - `27_terrastories.mp4` (H.264, ~500KB-1MB)
- Use `<video>` tag with poster frame and `<img>` fallback in the template
- Expected savings: **~9-10 MB**

### Phase 3: Resize Images to Reasonable Dimensions
- Create three size tiers:
  - **Thumbnail**: 400px wide (for cards, grids)
  - **Content**: 800px wide (for page body content)
  - **Hero**: 1200px wide (for hero banners, full-width images)
- No image should exceed 1200px wide
- Use Pillow `thumbnail()` with `LANCZOS` resampling for quality
- Keep originals in a `_ originals` backup folder (not in public/)
- Expected savings: **~40-50% further reduction**

### Phase 4: Responsive `<picture>` Elements
- For content images, generate multiple sizes at build time using Astro's built-in `<Image>` component
- Astro 6 + sharp can auto-generate responsive srcsets
- Use `widths` prop: `widths={[400, 800, 1200]}`
- Browser downloads only what it needs based on viewport

### Phase 5: Convert Remaining PNGs to WebP Where Possible
- Use `cwebp` or sharp to create WebP versions
- Use `<picture>` with `<source type="image/webp">` fallback to JPEG
- Expected additional savings: **25-35%** over JPEG

### Phase 6: Build-Time Optimization with Astro
- Configure `image.service` in `astro.config.mjs` for automatic optimization
- Use `astro:assets` `<Image>` component for all content images
- Lazy-load below-fold images with `loading="lazy"`
- Add `fetchpriority="high"` for hero/LCP images

## Implementation Order

1. Fix compress script to skip animated GIFs
2. Convert `160_*` single-frame GIF to JPEG
3. Resize all images to max 1200px using safe script
4. Convert animated GIF to MP4 + WebP
5. Integrate Astro `<Image>` component for responsive srcsets
6. Add lazy loading attributes

## Expected Final Size

| Stage | Size | Reduction |
|-------|------|-----------|
| Original | 116 MB | — |
| After initial compression | 75 MB | 35% |
| After resizing to max 1200px | ~35 MB | 70% |
| After GIF→MP4 conversion | ~26 MB | 78% |
| After WebP conversion | ~20 MB | 83% |
| With responsive srcsets | ~15 MB effective* | 87% |

*Effective = average bytes downloaded per page visit, not total on disk

## Safety Rules

1. **NEVER** process animated GIFs with Pillow — it destroys frames
2. **ALWAYS** back up originals before modifying
3. **VERIFY** every image after processing (dimensions, file size, visual spot-check)
4. **TEST** builds after each phase before committing
5. Use `ffmpeg` for video/GIF conversion, `Pillow` for raster, `cwebp` for WebP
