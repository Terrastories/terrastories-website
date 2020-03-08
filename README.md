### Terrastories Static Site

# Setup

After initial clone/fork run `yarn install` to install dependencies

`yarn start` to run

# Structure

Styled Components that are re-usable across the static site should live in the styled-components directory. Isolated styled components can live in the same component file/directory as their parent.

SvgComponents (needs a better name) is where the JSX versions of the SVG icons live.
To convert an svg to jsx use [svg2jsx](https://svg2jsx.com/). React can also use svg's as part of a regular image tag but having them as components can make them more flexible.

MediaFiles is for stuff like images, videos, etc

# Notes

I've been using a placeholder library called 'holderjs' to generate image placeholders until we decide on which files we want to use.

To create a placeholder:

`<img src="src="holder.js/300x200?theme=dark" />`

where the source tag is `holder.js/<size>?theme=<theme name>` the theme is optional but it allows you to set a background color and text color for the placeholder.

To create a theme:

```
import Holder from "holderjs";

Holder.addTheme("<theme name>", {
	bg: "<css color or hex code>"
});
```

## Plans:

Front page
-- Vision & Mission; link to SDGs
-- User Stories (snippets that link to blog posts)
-- Partner organizations
-- Support and follow us (donate and social media links)

Download & Install
--info about how to install Terrastories for online or offline contexts

Gallery
--a gallery of projects using Terrastories; currently we just have the Heroku demo, but eventually we'll have Heritales, and we some of the public-facing ACT projects

Help build Terrastories
--information for volunteers / developers
--how to host a built-a-thon event for Terrastories

About Terrastories
-- short history
-- core team
-- advisory board
-- where Terrastories has been built so far
-- more on the partner organizations
