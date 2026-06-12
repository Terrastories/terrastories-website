// Shared navigation data used by Header and Footer

export interface NavChild {
  label: string;
  href: string;
}

export interface NavItem {
  label: string;
  href: string;
  children?: NavChild[];
}

export const navItems: NavItem[] = [
  {
    label: 'How It Works',
    href: '/how-it-works',
    children: [
      { label: 'Videos', href: '/how-it-works#videos' },
      { label: 'Methodology', href: '/how-it-works#methodology' },
      { label: 'Practical Guide', href: '/how-it-works#edt' },
      { label: 'Try Terrastories', href: '/try-terrastories' },
    ],
  },
  { label: 'Documentation', href: 'https://docs.terrastories.app' },
  { label: 'Demo', href: '/demo' },
  { label: 'User Stories', href: '/category/user-stories' },
  {
    label: 'Developer Community',
    href: '/community',
    children: [
      { label: 'Dev Stories', href: '/category/dev-stories' },
      { label: 'Contribute', href: '/contribute' },
    ],
  },
  { label: 'Contact Us', href: '/contact-us' },
  {
    label: 'Sponsor Us',
    href: '/sponsor-us',
    children: [
      { label: 'Funding Needs', href: '/sponsor-us#funding' },
    ],
  },
  { label: 'GitHub', href: 'https://github.com/Terrastories/terrastories' },
];

export const exploreHref = 'https://explore.terrastories.app';

export const socialLinks = [
  { label: 'Twitter', href: 'https://twitter.com/TerrastoriesApp', icon: 'twitter' as const },
  { label: 'GitHub', href: 'https://github.com/Terrastories', icon: 'github' as const },
  { label: 'Mailing List', href: '/mailing-list', icon: 'mail' as const },
];

export const sponsors = [
  { name: 'Awana Digital', href: 'https://awana.digital', src: '/media/images/748_AwanaDigital-Logomark-HiRes.png' },
];

export const partners = [
  { name: 'Earth Defenders Toolkit', href: 'https://earthdefenderstoolkit.com', src: '/media/images/432_EDT-asset-dark-logo.png' },
  { name: 'Amazon Conservation Team', href: 'https://amazonteam.org', src: '/media/images/81_ACT-HQ_SQ_ENG_ASH.png' },
  { name: 'Ruby for Good', href: 'https://rubyforgood.org', src: '/media/images/83_rubyforgood.png' },
  { name: 'Mapbox', href: 'https://mapbox.com', src: '/media/images/82_mapbox-logo-blue-square.png' },
  { name: 'ATALM', href: 'https://atalm.org/', src: '/media/images/565_ATALM-logo_og.png' },
  { name: 'Tech Matters', href: 'https://techmatters.org', src: '/media/images/409_tech_matters_JPG_viewimage.jpg' },
  { name: 'Ohneganos', href: 'https://www.ohneganos.com/', src: '/media/images/433_ohneganos.png' },
  { name: 'Indigenous Mapping Workshop', href: 'https://indigenousmaps.com', src: '/media/images/435_IndigenousMaps.jpg' },
];

export const stewards = [
  { name: 'Rudo Kemper', image: '/media/images/640_rudo-square.jpg', url: 'https://github.com/rudokemper' },
  { name: 'Laura Mosher', image: '/media/images/126_lauramosher.jpg', url: 'https://github.com/lauramosher' },
  { name: 'Luandro Vieira', image: '/media/images/639_Screenshot-2023-02-18-235330.jpg', url: 'https://github.com/luandro' },
  { name: 'Albert Chae', image: '/media/images/644_T04PM108C-UHAS0KCMC-04f3dd0bb8de-512.jpg', url: 'https://github.com/albertchae' },
  { name: 'Roche Bhola', image: '/media/images/645_1492251_825539690793240_1507883986_o.jpg', url: 'https://github.com/rudokemper' },
];

export const alumni = [
  { name: 'Miranda Wang', image: '/media/images/121_mirandawang.jpg', url: 'https://github.com/mirandawang' },
  { name: 'Kalimar Maia', image: '/media/images/125_kalimarmaia.jpg', url: 'https://github.com/kalimar' },
  { name: 'Ian Norris', image: '/media/images/124_iannnorris.jpg', url: 'https://github.com/feminismisawesome' },
  { name: 'Mae Beale', image: '/media/images/127_maebeale.jpg', url: 'https://github.com/maebeale' },
];

export const isExternal = (href: string) => href.startsWith('http');
