// Shared navigation data used by Header and Footer

export interface NavChild {
  label: string;
  href: string;
}

export interface NavItem {
  label: string;
  href: string;
  children?: NavChild[];
  icon?: "github";
}

export const navItems: NavItem[] = [
  {
    label: "How It Works",
    href: "/how-it-works",
    children: [
      { label: "Videos", href: "/how-it-works#videos" },
      { label: "Methodology", href: "/how-it-works#mapping-oral-histories" },
      {
        label: "Practical Guide",
        href: "/how-it-works#earth-defenders-toolkit",
      },
      { label: "Demo", href: "/demo" },
      { label: "Try Terrastories", href: "/try-terrastories" },
    ],
  },
  { label: "Documentation", href: "https://docs.terrastories.app" },
  {
    label: "Blog",
    href: "/blog",
    children: [
      { label: "User Stories", href: "/category/user-stories" },
      { label: "Dev Stories", href: "/category/dev-stories" },
    ],
  },
  { label: "Contribute", href: "/contribute" },
  { label: "Contact Us", href: "/contact-us" },
  {
    label: "Sponsor Us",
    href: "/sponsor-us",
    children: [{ label: "Funding Needs", href: "/sponsor-us#funding-needs" }],
  },
  {
    label: "GitHub",
    href: "https://github.com/Terrastories/terrastories",
    icon: "github",
  },
];

export const exploreHref = "https://explore.terrastories.app";

export const sponsors = [
  {
    name: "Awana Digital",
    href: "https://awana.digital",
    src: "/media/images/748_AwanaDigital-Logomark-HiRes.png",
  },
];

export const partners = [
  {
    name: "Earth Defenders Toolkit",
    href: "https://earthdefenderstoolkit.com",
    src: "/media/images/432_EDT-asset-dark-logo.png",
  },
  {
    name: "Amazon Conservation Team",
    href: "https://amazonteam.org",
    src: "/media/images/81_ACT-HQ_SQ_ENG_ASH.png",
  },
  {
    name: "Ruby for Good",
    href: "https://rubyforgood.org",
    src: "/media/images/83_rubyforgood.png",
  },
  {
    name: "Mapbox",
    href: "https://mapbox.com",
    src: "/media/images/82_mapbox-logo-blue-square.png",
  },
  {
    name: "ATALM",
    href: "https://atalm.org/",
    src: "/media/images/565_ATALM-logo_og.png",
  },
  {
    name: "Tech Matters",
    href: "https://techmatters.org",
    src: "/media/images/409_tech_matters_JPG_viewimage.jpg",
  },
  {
    name: "Ohneganos",
    href: "https://www.ohneganos.com/",
    src: "/media/images/433_ohneganos.png",
  },
  {
    name: "Indigenous Mapping Workshop",
    href: "https://indigenousmaps.com",
    src: "/media/images/435_IndigenousMaps.jpg",
  },
];

export const isExternal = (href: string) => href.startsWith("http");
