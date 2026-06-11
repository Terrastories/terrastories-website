# PRD: Visual Alignment with Original Terrastories Design

**Goal**: Align the Astro rebuild's visual system with the original WordPress/Astra site at terrastories.app, while keeping improvements from the rebuild.

**Reference**: Original site CSS tokens and HTML structure from `/tmp/terrastories-ref/`.

---

## Out of Scope (Keep As-Is)

- Hamburger menu component, animation, and side slider (only update background color + add missing nav items)
- Partners and sponsors section (already looks good)
- Stewards and alumni PeopleGrid (already looks good)
- Content/copy changes (already migrated)
- Canonical/OG tags pointing to terrastories.app (intentional)

---

## Phase 1: Global Design Tokens & Typography

**Files**: `src/styles/global.css`, `src/layouts/BaseLayout.astro`

The biggest visual gap — our site looks like a different brand because fonts and colors are wrong.

- Replace Inter with **Open Sans** (body) via Google Fonts
- Replace heading font with **Oswald** (weight 400) via Google Fonts
- Change body text color to `#3a3a3a`
- Change background from warm paper (`#fbfaf6`) to white (`#fff`)
- Change link color to `#d97b29` (orange), hover to `#dea826` (gold)
- Change `::selection` to teal bg / white text
- Update Tailwind `@theme` tokens:
  - Rename or replace `clay` with `#d97b29` (brand orange)
  - Rename or replace `forest` with `#09697e` (brand teal)
  - Remove or repurpose `moss`, `river`, `ink`, `cream`, `paper`, `bark` if no longer needed
- Add base CSS rules for heading sizes matching original Astra values
- Load Google Fonts in `BaseLayout.astro` head

**Verification**: After building, headings should render in Oswald, body in Open Sans, links orange, background white.

---

## Phase 2: Header

**File**: `src/components/Header.astro`

- Add **5px orange bottom border** (`#d97b29`)
- Increase logo size to closer to original 300px wide (currently `h-8`)
- Add missing **Documentation** nav item
- Add **dropdown submenus**:
  - How It Works → Videos, Methodology, Practical Guide, Try Terrastories
  - Developer Community → Dev Stories, Contribute
  - Sponsor Us → Funding Needs
- Change nav link hover/active color to `#d97b29` (currently forest)
- Change **Explore Terrastories CTA** to square (not rounded), orange bg, gold hover
- Update hamburger menu **background color** to match new theme (teal or white)
- Add missing nav items to mobile menu (Documentation, submenus)
- Remove underline from active nav state (original uses orange text only)

**Verification**: Header should have orange bottom rule, larger logo, dropdown menus, orange active states, square CTA.

---

## Phase 3: Footer

**File**: `src/components/Footer.astro`

Original has a distinct two-part structure we should match:

- Add **"FOLLOW US"** section above footer with heading and social icons (Twitter/X, GitHub, Mailing List)
- Change footer background from dark forest to **teal** (`#09697e`)
- Replace 4-column layout with **centered single-column**:
  - Terrastories square icon/logo centered
  - Footer nav matching original hierarchy (same as header nav)
- Remove descriptive paragraph columns (original has none)

**Verification**: Footer should be teal with centered icon + nav, FOLLOW US strip above.

---

## Phase 4: Page Title Bands

**File**: `src/layouts/PageLayout.astro`

Original pages use full-width centered uppercase title bands instead of standard article headers.

- Replace article header with full-width centered title band:
  - `uppercase` text
  - Oswald font, weight 400
  - Teal color (`#09697e`)
  - Centered
- Remove `font-bold`, `text-ink`, `md:text-5xl`
- Change content wrapper from `max-w-4xl` to `max-w-[940px]` (matching Astra container)
- Remove `prose-img:rounded` (original images are square)
- Change `prose-a:text-river` to `prose-a:text-[#d97b29]` (orange links)
- Optionally remove excerpt display for pages (original hides `.page .entry-header`)

**Verification**: All pages (How It Works, Demo, Contact, Sponsor, etc.) should show centered uppercase teal titles.

---

## Phase 5: Buttons Sitewide

**Files**: Multiple — `index.astro`, `PostCard.astro`, `Header.astro`, `demo.md`

- Replace rounded buttons with **square** orange buttons
- Color: `bg-[#d97b29]`, hover `bg-[#dea826]`, white text
- Padding: approximately `px-[40px] py-[10px]`
- Apply to: CTA buttons on homepage, "Read more" on post cards, Explore Terrastories, Demo page button

**Verification**: All buttons should be square orange with gold hover.

---

## Phase 6: Homepage Sections

**File**: `src/pages/index.astro`

Refine the homepage sections to match original heading styles:

- **Hero section**: Center h1 uppercase, Oswald, teal. Center h4 subtitle. (Keep current layout structure, just restyle the typography)
- **"LATEST STORIES" heading**: Centered, uppercase, Oswald, teal (currently left-aligned)
- **PostCards**: Update title to Oswald/teal, date to orange, "Read more" to square orange button (via Phase 5 button changes)
- **"HELP US GROW" section**: Centered uppercase heading, match original styling. Keep two CTA buttons but make them square orange.
- Remove `bg-forest` from Help Us Grow section (original uses a lighter background or none)

**Verification**: Homepage headings centered uppercase, cards updated, CTAs square orange.

---

## Phase 7: Post Cards

**File**: `src/components/PostCard.astro`

- Remove rounded borders (`rounded`, `border`, `border-stone-200`)
- Use Oswald font for title, teal color
- Make date orange (`#d97b29`)
- Change "Read more" from text link to **centered square orange button**
- Optionally switch from bordered card to shadow-only wrapper

**Verification**: Post cards should look closer to original UABB blog cards with orange read-more buttons.

---

## Phase 8: Content Images

**File**: `src/layouts/PageLayout.astro`, page-level adjustments

- Remove `prose-img:rounded` from PageLayout
- Ensure content images render square (no rounded corners)
- Verify figcaption uses italic styling

**Verification**: All content images square, no rounded corners.

---

## Phase 9: Ancillary Page Tweaks

**Files**: Various content pages

- **How It Works**: Add section anchor IDs (`#videos`, `#methodology`, `#edt`) so header/footer submenu links work
- **Sponsor Us**: Ensure `id="funding"` anchor exists on Funding Needs heading
- **Demo**: Add centered orange CTA button linking to `https://our.terrastories.app`
- **Contact**: Remove uppercase body copy (already partially done), ensure orange links

**Verification**: All submenu links from header/footer navigate to correct page sections.

---

## Implementation Notes

- Phase 1 (tokens) should be done first as everything else depends on it
- Phases 2-4 can be done in parallel after Phase 1
- Phase 5 (buttons) should come before Phase 6 (homepage) since buttons are used there
- Phase 9 is cleanup and can be done last
- After each phase: build, verify, commit
- Use `npx astro build` to verify; serve with `python3 -m http.server 4322` in dist/
