# Terrastories Design Comparison Report

Generated from the current Astro codebase and the saved WordPress/Astra reference HTML in `/tmp/terrastories-ref/`.

## Executive Summary

The Astro rebuild preserves much of the page content and image inventory, but it does not yet match the original WordPress visual system. The current site uses a new Tailwind palette, Inter typography, rounded cards, forest/river/clay accents, and modern constrained layouts. The original site is an Astra/Beaver Builder/Elementor composition using Open Sans body text, Oswald headings, teal section headings, a warm orange accent, a 5px orange header rule, square orange buttons, full-width hero title bands, and a simple teal footer with a centered icon/nav menu.

The highest-impact gaps are:

1. **Global typography mismatch**: current `src/styles/global.css` uses Inter and `--color-ink: #1b1f23`; original uses Open Sans, 15px, `#3a3a3a`, and Oswald headings at weight 400.
2. **Brand color mismatch**: current `forest`, `river`, and `clay` are close but not exact. Original links/buttons use `#d97b29`, hover `#dea826`, heading/selection/footer teal `#09697e`, and advanced footer green `#33aa8b`.
3. **Header mismatch**: current header is a modern Tailwind navbar with small logo, thin stone border, no dropdowns, and slide-in mobile drawer. Original has 300x42 logo, full-width header, 35px left padding, 0 right padding, 5px orange bottom border, dropdown submenus, orange active nav text, and a full-height orange CTA block flush to the right.
4. **Page title/hero mismatch**: original pages hide the normal page header and use full-width Beaver Builder photo/background rows with centered uppercase Oswald `h1` titles. Current `PageLayout.astro` renders a standard article header with title/excerpt and `max-w-4xl`.
5. **Footer mismatch**: original has a separate “FOLLOW US” Elementor strip, then a teal footer overlay with centered square Terrastories icon and one nested footer nav. Current footer is a four-column dark forest footer with explanatory copy and copyright line.
6. **Component styling mismatch**: original buttons are square orange Astra buttons with `padding: 10px 50px 10px 40px`; current buttons/cards/logos are rounded, bordered, and shadowed.

## Original Design Tokens To Apply

Use these as the target tokens in `src/styles/global.css`.

```css
--color-brand-orange: #d97b29;
--color-brand-orange-hover: #dea826;
--color-brand-teal: #09697e;
--color-brand-green: #33aa8b;
--color-body: #3a3a3a;
--font-sans: "Open Sans", sans-serif;
--font-heading: "Oswald", sans-serif;
```

Recommended global rules:

```css
html { font-size: 93.75%; }
body {
  font-family: var(--font-sans);
  font-size: 15px;
  font-weight: 400;
  color: var(--color-body);
  background: #fff;
}
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  font-weight: 400;
  color: var(--color-brand-teal);
  letter-spacing: 0;
}
h1 { font-size: 40px; }
h2 { font-size: 30px; }
h3 { font-size: 25px; }
h4 { font-size: 20px; }
h5 { font-size: 18px; }
h6 { font-size: 15px; }
a { color: var(--color-brand-orange); }
a:hover, a:focus { color: var(--color-brand-orange-hover); }
::selection { background: var(--color-brand-teal); color: #fff; }
```

Also load the fonts in `BaseLayout.astro` or CSS:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400&family=Oswald:wght@400&display=swap" rel="stylesheet">
```

## Global Layout Differences

### Current Astro

- `src/layouts/PageLayout.astro` uses `article.mx-auto.max-w-4xl.px-6.py-12`.
- `src/pages/index.astro` uses a modern section layout with `max-w-5xl`/`max-w-7xl`.
- `global.css` sets `background: var(--color-paper)` (`#fbfaf6`).

### Original WordPress

- Astra content container is usually `max-width: 940px` for regular content.
- Header container is full width with `padding-left: 35px`, `padding-right: 0`.
- Page-builder rows alternate between full-width hero rows and fixed-width content rows.
- Normal `.entry-header` is hidden on pages by custom CSS: `.page .entry-header { display: none; }`.
- Body background reads white, not warm paper.

### Recommended Changes

- Change global background from paper to white.
- Use a reusable page hero component before content on all major pages:
  - full width
  - centered title
  - uppercase for page hero titles
  - Oswald, weight 400
  - teal text
  - background image/photo row if assets can be identified, otherwise plain full-width row with matching spacing
- Change `PageLayout.astro` content width to closer Astra values: `max-w-[940px]`.
- Remove default excerpt block for pages when trying to match WordPress, because original page headers are hidden and excerpts are not rendered.

## Header

### Original

Source: all reference pages, header around the `#masthead` markup.

- Logo: `Logocombo-300x42.png`, rendered `width="300" height="42"`.
- Header container: full width, left padding 35px desktop, 20px mobile, right padding 0.
- Header bottom border: `5px solid #d97b29`.
- Nav text: Open Sans, 15px, `#3a3a3a`; hover/current `#d97b29`.
- Desktop breakpoint: 922px.
- Dropdowns:
  - How It Works -> Videos, Methodology, Practical Guide, Try Terrastories
  - Developer Community -> Dev Stories, Contribute
  - Sponsor Us -> Funding Needs
  - dropdown top border `2px solid #09697e`
- Top-level menu also includes Documentation between How It Works and Demo.
- Explore Terrastories is an Astra custom menu button at the far right, orange, square, full header height feel, with `line-height: 3.5`, `margin-right: -15px`.
- Mobile toggle is an orange filled Astra button, not a side drawer design.

### Current Astro

File: `src/components/Header.astro`

- Logo is `/media/images/nav-logo.png` with `h-8`, much smaller than 300x42.
- Header has `border-b border-stone-200 bg-paper`, not 5px orange.
- Uses `max-w-7xl px-6 py-4`; original is full width with explicit Astra padding.
- Missing top-level Documentation.
- Missing dropdown submenus.
- Active state uses forest text plus underline; original uses orange text, no underline.
- CTA is rounded orange (`bg-clay`) and hover forest; original is square orange and hover gold.
- Mobile menu is a custom slide-in panel; original Astra mobile menu expands under the header.

### Recommended Changes

- Replace header classes with a full-width layout:
  - `bg-white border-b-[5px] border-[#d97b29]`
  - inner container `max-w-none pl-[35px] pr-0 py-0 min-h-[70px]`
- Render logo at `w-[300px] h-auto` or `max-w-[300px]`, with mobile max width guarded.
- Add Documentation top-level nav item.
- Model nav as nested data and render dropdowns on desktop.
- Change active/hover to `text-[#d97b29]`; remove underline active decoration.
- Change Explore CTA to square:
  - `bg-[#d97b29] hover:bg-[#dea826] text-white rounded-none px-[40px] py-[10px] leading-[3.5]`
  - align flush right if matching the original exactly.
- For mobile, either adapt the current drawer visually to Astra colors or replace it with an inline expanding menu under the header; include submenu items with indentation.

## Footer

### Original

Source: footer in all reference pages.

- Pre-footer social section from Elementor:
  - heading `FOLLOW US`
  - circular social icons: Twitter/X, GitHub, Mailchimp/mailing list
- Footer proper:
  - `.ast-footer-overlay` background `#09697e`
  - top border `1px solid #7a7a7a`
  - padding top/bottom `2em`
  - centered square Terrastories icon `Terrastories-icon-sq-150x150.png`
  - one nested footer nav menu containing the same main nav and submenu hierarchy
  - links have compact horizontal padding `.5em`
- No four-column explanatory footer and no visible copyright line in the captured markup.

### Current Astro

File: `src/components/Footer.astro`

- Dark forest background `bg-forest`, not teal `#09697e`.
- Four-column layout with headings and paragraph.
- No Terrastories square icon.
- No “FOLLOW US” strip or social icons.
- Footer link hierarchy differs from original and is split into columns.

### Recommended Changes

- Replace `bg-forest` with `bg-[#09697e]`.
- Add a separate pre-footer `FOLLOW US` section before `<footer>` with centered heading and three circular icons/links:
  - `https://twitter.com/TerrastoriesApp`
  - `https://github.com/Terrastories`
  - `/mailing-list/`
- Rework footer layout to a centered single-column widget area:
  - icon image `/media/images/40_Terrastories-icon-sq.png` or the available closest square icon asset
  - nested nav list matching the original hierarchy
- Remove or de-emphasize the copyright row if strict matching is required.

## Buttons

### Original

- Button color: `#d97b29`; hover/focus `#dea826`.
- Text: white.
- Border radius: `0`.
- Padding: `10px 50px 10px 40px`.
- Font inherits Open Sans 15px, weight 400.
- Line-height: 1 for normal Astra buttons.

### Current Astro

- Uses `rounded`, `rounded-lg`, `font-semibold`, `bg-clay`, hover forest/clay variants.
- Buttons in homepage CTA use rounded-lg and mixed filled/outlined styles.

### Recommended Changes

- Create a shared `.btn-original` or Tailwind utility pattern:
  - `rounded-none bg-[#d97b29] px-[40px] pr-[50px] py-[10px] font-normal leading-none text-white hover:bg-[#dea826]`
- Replace homepage, demo, card “Read more”, and header CTA button styling with this pattern.
- Avoid rounded buttons when matching WordPress.

## Homepage

### Original Structure

Source: `/tmp/terrastories-ref/home.html`.

1. Full-width photo/background hero row:
   - centered heading `TERRASTORIES: CONNECTING GENERATIONS`
   - subheading `A free and open-source application...`
   - headings via Beaver Builder UABB, centered and uppercase
2. Fixed-width intro text row.
3. Full-width GIF/image module: `terrastories.gif`.
4. Text about free/open-source, then two SDG images.
5. `LATEST STORIES` centered uppercase heading.
6. Three-column UABB blog post grid:
   - thumbnail on top
   - title
   - date as small heading/meta
   - excerpt
   - centered orange “Read more” Astra button
7. Full-width photo/background CTA row:
   - `HELP US GROW`
   - subheading
   - dual buttons: Sponsor us, Be a developer
8. Sponsors/partners fixed-width section:
   - heading “Terrastories is currently being sponsored by”
   - large Awana logo
   - heading “Special thanks to our partners”
   - partner logos laid out in rows of four
   - “Become a partner” button/link near the end

### Current Astro

File: `src/pages/index.astro`

- Hero content is just rendered Markdown inside `prose`, not a page-builder hero band.
- Intro and hero are combined into one `bg-paper px-6 py-14` section.
- Video uses a rounded `<video>` with shadow; original uses an image/GIF module with no rounded card styling.
- `Latest Stories` section heading is left-aligned title case with a “View all” link; original is centered uppercase with no view-all link in the captured section.
- Post cards are rounded bordered cards and use modern Tailwind colors.
- CTA uses solid forest background; original is a full-width photo/background row with centered heading and orange dual buttons.
- Partner logos are wrapped in bordered rounded logo cards; original logos are placed directly in columns without card chrome.

### Recommended Changes

- Split the homepage into explicit sections that mirror the original sequence.
- Add a homepage hero section:
  - full-width row
  - background photo if recoverable from Beaver Builder CSS; otherwise white/photo fallback
  - centered uppercase `h1`
  - centered `h4` subheading
- Set homepage hero `h1` to Oswald, weight 400, teal; use uppercase.
- Remove rounded/shadow styling from the demo media; render GIF/image square and centered.
- Change Latest Stories:
  - heading `LATEST STORIES`
  - centered, uppercase, Oswald
  - remove or visually hide “View all” if strict match is required
  - use original post-card treatment with top thumbnail, title, date, excerpt, orange button
- Change Help Us Grow:
  - use a full-width hero/CTA band, not `bg-forest`
  - title `HELP US GROW`, centered uppercase
  - subheading as `h4`, centered
  - both buttons orange/square or match UABB dual button styles if CSS is recovered
- Change partner logo section:
  - headings should preserve original text/case:
    - “Terrastories is currently being sponsored by”
    - “Special thanks to our partners”
  - remove rounded borders/background cards from `PartnerLogo.astro`
  - use fixed-width rows/columns, 4 columns desktop
  - allow Awana logo to be much wider than partner icon logos.

## PageLayout Pages: How It Works, Demo, Contact, Sponsor

### Shared Original Pattern

For `/how-it-works/`, `/demo/`, `/contact-us/`, and `/sponsor-us/`:

- WordPress has a normal `entry-title`, but custom CSS hides `.page .entry-header`.
- Visible page title is a full-width Beaver Builder row with centered uppercase text:
  - `HOW IT WORKS`
  - `DEMO`
  - `CONTACT US`
  - `SPONSOR US`
- Content below is in fixed-width Beaver Builder rows.
- Body copy is Open Sans 15px, `#3a3a3a`.
- Section headings are Oswald, teal, weight 400.
- Links are orange/gold.

### Current Astro

File: `src/layouts/PageLayout.astro`

- Renders an article header with title case `h1`, bold, `text-ink`, `md:text-5xl`.
- Renders excerpt under the title if present.
- Uses typography plugin defaults (`prose-stone`) that override sizes/weights away from Astra.
- Images are rounded via `prose-img:rounded`.
- Links use `prose-a:text-river`, not orange.

### Recommended Changes

- Replace article header with an original-style page title band:
  - `section.w-full`
  - `h1.text-center.uppercase.font-heading.font-normal.text-[#09697e]`
- Remove `font-bold`, `text-ink`, and `md:text-5xl` from page titles.
- Change content wrapper to `max-w-[940px]`.
- Override `.prose` to use Open Sans and original heading/link colors.
- Remove `prose-img:rounded`; original content images are square.
- Use `figcaption { font-style: italic; }`.

## How It Works Page

### Original

- Starts with `HOW IT WORKS` title band.
- Shows large GIF `terrastories-1920x1080-768x432-1.gif`.
- Text block follows.
- Videos section uses a UABB video gallery carousel with thumbnails, dark overlays, captions, and lightbox playback.
- Mapping oral histories section includes ACT guide image, small PDF icon/link row, and explanatory text.
- Earth Defenders Toolkit section includes a large screenshot.

### Current Astro

Content file: `src/content/pages/how-it-works.md`

- No page title band; relies on `PageLayout` article header.
- Video gallery is reduced to a bullet list of YouTube links.
- PDF icon row is simplified to one download link.
- Images become rounded through `PageLayout`.

### Recommended Changes

- Add original-style `HOW IT WORKS` hero/title band.
- Restore video gallery as a component rather than a bullet list:
  - 16:9 thumbnail carousel or responsive grid
  - caption overlay
  - play/lightbox behavior if desired
- Include the PDF icon link row if visual fidelity matters.
- Keep content width around 940px and remove image rounding.

## Demo Page

### Original

- Starts with `DEMO` title band.
- Text says the demo server is at `https://our.terrastories.app`.
- Explicit credentials appear in the original:
  - username `terrastories-demo`
  - password `MapsThatRoar123*`
- Centered orange Astra button: `Terrastories demo`.
- Two screenshots are displayed in a two-column nested row on desktop.

### Current Astro

Content file: `src/content/pages/demo.md`

- Text has been rewritten to say “Sign in with the demo credentials provided there”; credentials are not shown.
- No orange CTA button.
- Screenshots render as sequential Markdown images, likely stacked depending on prose layout.
- Page header is standard layout, not original title band.

### Recommended Changes

- Restore original visible text if content fidelity is in scope, including credentials.
- Add centered square orange `Terrastories demo` button linking to `https://our.terrastories.app`.
- Render screenshots in a two-column grid on desktop.
- Apply original page title band.

## Contact Page

### Original

- Starts with `CONTACT US` title band.
- Body is two paragraphs:
  - online server/partnership inquiries go to `support@awana.digital` and copy `terrastoriesorg@gmail.com`
  - self-hosting support points to docs support page
- No excerpt or card layout.

### Current Astro

Content file: `src/content/pages/contact-us.md`

- Content is converted into three bold lead-in paragraphs.
- `PageLayout` renders an excerpt below the title.
- Styling is modern prose with river links.

### Recommended Changes

- Use the original two-paragraph copy structure if matching content presentation.
- Remove excerpt display.
- Apply original page title band and orange links.

## Sponsor Page

### Original

- Starts with `SPONSOR US` title band.
- Fixed-width content row.
- Headings:
  - Donations
  - Sponsorship
  - Funding Needs
- In the original markup, these headings are often bold text inside `h2`, but the computed heading family/color still comes from Astra: Oswald, teal, weight 400.
- Funding Needs anchor is `#funding`.
- Standard unordered list styling.

### Current Astro

Content file: `src/content/pages/sponsor-us.md`

- Content largely matches, but:
  - “with ❤️” was normalized to “with love”
  - no visible `#funding` anchor unless Markdown heading slug generation happens to match
  - page header/excerpt differ
  - typography/colors differ

### Recommended Changes

- Apply original title band.
- Preserve `id="funding"` for compatibility with nav submenu.
- Use original heading/link/button styles globally.
- Confirm content wording if exact migration fidelity matters.

## Community Page

### Reference Caveat

The supplied `/tmp/terrastories-ref/community.html` is a WordPress 404 page for `developer-community`, not the original Developer Community page content. It still contains the global original header/footer, but it cannot be used as a reliable page-specific design reference.

### Current Astro

Files:

- `src/pages/community.astro`
- `src/components/PeopleGrid.astro`
- `src/content/pages/community.md`

The Astro page is a custom page with:

- standard article header
- Markdown intro
- steward/alumni portrait grids
- circular portraits with rings/shadows
- code contributors image with rounded corners and shadow

### Recommended Changes

- Apply the same global typography, links, and page title band as other pages.
- If a true original community page is recovered, compare against it before changing `PeopleGrid`.
- If matching the broader WordPress style now:
  - use Oswald teal headings
  - remove `font-bold text-ink`
  - reduce modern ring/shadow effects
  - remove rounded image corners where original images were square.

## Post Cards / Latest Stories

### Original

Source: homepage UABB blog posts grid.

- Three columns desktop.
- Thumbnail top.
- White content card area with UABB shadow wrapper.
- Title in Oswald heading style.
- Date as `h6` meta in orange.
- Excerpt.
- Centered orange square “Read more” button.

### Current Astro

File: `src/components/PostCard.astro`

- `overflow-hidden rounded border border-stone-200 bg-white`.
- Image forced to `aspect-video object-cover`.
- Date is plain `text-sm text-stone-600`.
- Title is `text-xl font-bold text-ink`.
- Read more is a text link, not a button.

### Recommended Changes

- Remove border radius.
- Replace border-card look with shadow-only or UABB-like wrapper.
- Use Oswald, weight 400, teal/dark heading color for titles.
- Make date orange (`#d97b29`) and small.
- Convert “Read more” to centered Astra-style orange button.

## Partner Logos

### Original

- Logos are bare image/photo modules inside columns.
- No border, rounded container, white card, or hover shadow.
- Sponsored Awana logo is large and horizontal.
- Partners are arranged in rows of four desktop columns.

### Current Astro

File: `src/components/PartnerLogo.astro`

- Every logo is wrapped in a rounded bordered white card with padding and hover shadow.
- Images are capped at `max-h-16`, making the Awana sponsor too small relative to the original.

### Recommended Changes

- Remove `rounded-lg border bg-white p-4 hover:shadow-md`.
- Render anchors as plain centered blocks.
- Add optional sizing variants:
  - sponsor: wide, `max-w-[600px]`, no `max-h-16`
  - partner: natural image, constrained by column width, no card chrome

## PeopleGrid

### Current Difference

No valid original community page reference was available, so this component cannot be compared precisely. Its current ring, hover shadow, and circular portrait treatment are modern Tailwind design choices. If strict original matching is desired, reduce rings/shadows and use original image shapes once the source page is available.

## Priority Ranking

### Critical Styling Gaps

1. Replace Inter/Tailwind typography with Open Sans body and Oswald headings.
2. Replace current palette with exact WordPress tokens: orange `#d97b29`, hover gold `#dea826`, teal `#09697e`, body `#3a3a3a`.
3. Rebuild header to match Astra: 300px logo, 5px orange border, full nav including Documentation and dropdowns, orange active/hover states, square Explore CTA.
4. Rebuild footer to match original: `FOLLOW US` strip, social icons, teal footer overlay, centered square icon, nested footer nav.
5. Add original-style uppercase page title bands to all major pages and remove modern article headers/excerpts.

### High Priority

6. Convert buttons sitewide to square orange Astra buttons with gold hover.
7. Restyle homepage sections, especially `LATEST STORIES`, `HELP US GROW`, and sponsor/partner logos.
8. Restyle `PostCard.astro` to match UABB blog cards and button behavior.
9. Remove rounded corners/shadows from content images where original images were square.
10. Change prose link color from `river` to original orange.

### Medium Priority

11. Restore How It Works video carousel/lightbox instead of bullet links.
12. Restore Demo page CTA button and two-column screenshot layout.
13. Add `#funding`, `#videos`, `#methodology`, and `#edt` anchors explicitly so header/footer submenu links land correctly.
14. Rework partner logo sizing so sponsor and partner logos match original scale.

### Minor / Needs More Reference

15. Fine tune Beaver Builder row background images once their CSS/background assets are identified.
16. Fine tune mobile menu behavior to exactly match Astra expansion.
17. Compare Developer Community against a valid original page capture; current provided `community.html` is a 404 reference.

## File-by-File Change Map

- `src/styles/global.css`
  - Replace theme tokens, fonts, body color/background, link colors, selection color, heading rules, button utility rules, figcaption style.
- `src/layouts/BaseLayout.astro`
  - Load Open Sans and Oswald.
  - Ensure `Header` and `Footer` are not wrapped by extra modern layout constraints.
- `src/layouts/PageLayout.astro`
  - Replace article header with page-builder-like uppercase title band.
  - Use `max-w-[940px]`.
  - Remove excerpt rendering for original parity.
  - Remove `prose-img:rounded`; use original heading/link colors.
- `src/components/Header.astro`
  - Add Documentation.
  - Add nested nav/dropdowns.
  - Change logo size and header border/layout.
  - Restyle mobile toggle and CTA.
- `src/components/Footer.astro`
  - Replace four-column footer with original social strip plus teal icon/nav footer.
- `src/pages/index.astro`
  - Rebuild homepage section order and styling to mirror Beaver Builder rows.
  - Change Latest Stories heading/card layout.
  - Change Help Us Grow band/buttons.
  - Change sponsor/partner headings and logo layout.
- `src/components/PostCard.astro`
  - Remove rounded/bordered card styling.
  - Use Oswald title, orange date, centered orange Read more button.
- `src/components/PartnerLogo.astro`
  - Remove card chrome and support sponsor vs partner sizing.
- `src/components/PeopleGrid.astro`
  - Keep pending valid original community reference; optionally reduce modern effects.
- `src/content/pages/demo.md`
  - Restore credentials and CTA content if exact content parity is required.
- `src/content/pages/how-it-works.md`
  - Replace video bullet list with structured data/component use if restoring the original carousel.
- `src/content/pages/sponsor-us.md`
  - Ensure `Funding Needs` anchor is `funding`.

