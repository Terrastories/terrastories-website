---
author: rkemper
author_name: rkemper
categories:
- Dev Stories
date: 2018-06-13 03:51:24+00:00
excerpt: 'I just came back from an exhilarating weekend at Ruby for Good 2018 to
  work with a team to develop an open-source, offline-compatible geostorytelling application.
  I want to share my experiences, but first, some history. Almost twenty years ago,
  ACT partnered with the Trio (or sometimes Tyrío, Tarëno) indigenous communities
  in southern Suriname and northern Brazil to …'
featured_image: /media/images/339_terrastories-team-e1598673500192.jpg
featured_image_id: 339
link: /act-partakes-in-ruby-for-good-2018-to-develop-offline-geostorytelling-app-terrastories-for-remote-communities
modified: 2020-08-29 03:59:15+00:00
og_image: /media/images/339_terrastories-team-e1598673500192.jpg
seo_description: Terrastories is a geostorytelling application built to enable indigenous
  and other local communities to locate and map their oral storytelling traditions.
seo_title: ACT partakes in Ruby for Good 2018 to develop offline geostorytelling app
  Terrastories for remote communities - Terrastories
slug: act-partakes-in-ruby-for-good-2018-to-develop-offline-geostorytelling-app-terrastories-for-remote-communities
status: publish
title: ACT partakes in Ruby for Good 2018 to develop offline geostorytelling app Terrastories
  for remote communities
type: post
---

# ACT partakes in Ruby for Good 2018 to develop offline geostorytelling app Terrastories for remote communities

I just came back from an exhilarating weekend at [**Ruby for Good 2018**](http://rubyforgood.org/) to work with a team to develop an open-source, offline-compatible geostorytelling application. I want to share my experiences, but first, some history.

Almost twenty years ago, ACT partnered with the Trio (or sometimes Tyrío, Tarëno) indigenous communities in southern Suriname and northern Brazil to produce large-scale maps of their ancestral lands, entirely from an indigenous perspective. These maps showed an enormous amount of information and indigenous knowledge including sacred sites, historically significant places, local names for geographical features, and natural resources used by the communities.
![](/media/images/336_kwamala.jpg)

At the time, these maps were pioneering in the fields of participatory and indigenous mapping, but the geographers realized they were missing a crucial part of the Trio knowledge about their ancestral lands: the oral histories about the places on the map. To remedy this absence, and to accompany the maps, ACT sponsored a publication by Karin Boven, *Beyond Samuwaka*, about the most important Trio sacred place.

Several years ago, during mapping fieldwork with the Matawai Maroons, we realized a similar need to [**document the oral histories that the community share about their territory**](https://news.mongabay.com/2017/11/storytelling-empowers-indigenous-people-to-conserve-their-environments/). For the Matawai, storytelling is an important cultural tradition, and is at risk of being lost due to the passing of the community the elders, and the youth no longer being around to listen to their stories as in times past.
![](/media/images/337_oomsepie.jpg)

However, seventeen years later since the publication of the Trio maps, mapping technology has improved by leaps and bounds. Using interactive web mapping technology like [**story maps**](https://storymaps.arcgis.com/en/gallery/#s=0&q=amazon%20conservation%20team), it is now possible to add additional layers of information to the map, and to use maps to tell stories in innovative ways. We decided to embark on a project to partner with the community to document and record their oral history traditions (more information about this project coming in the future). But we still faced a challenge: while mapping technology has enabled the data on the maps to come to life in novel ways, a lot of this tech is reliant on internet connectivity, while our partner communities live in extremely remote locations.

So, we decided to build our own offline-compatible geostorytelling application, designed specifically for remote communities. Besides being able to run offline, we wanted it to be open-source so that any community anywhere in the world could use it to map their own place-based storytelling traditions. We also wanted it to be able to play audio and video recordings of storytelling. And we wanted it to be easy to install and use. Piece of cake, right?
![](/media/images/338_rubyforgood.jpg)

Not so – we very quickly realized that we, as a field organization, lacked the technical expertise to develop something that can really do all of that. Thankfully, we found friends in the tech world willing to help out. The company [**Mapbox**](https://mapbox.com/) saw the potential social impact of the project, and was willing to help us render our mapping data offline using their Studio platform. And, they introduced us to a wonderful community called [**Ruby for Good**](https://rubyforgood.org/).

Ruby for Good is an annual event where programmers in the Ruby language get together for a long weekend to build projects that help communities. Inspired by the slogan “dedicated to making the world gooder,” the organizing committee selects a handful of projects each year and programmers attending the event choose a project that speaks to them. Amazingly, Ruby for Good selected our geostorytelling proposal, and from June 7 through June 10, a team set to work on making our dreams come to life. We decided to call it *Terrastories*, because the app will be used to map stories about land, or territory.
![](/media/images/339_terrastories-team-e1598673500192.jpg)

The talented Terrastories team, composed of people with various backgrounds in front-end design, UX/UI (user experience / user interface), Ruby for Rails, and server administration set to work, and quickly the pieces started to assemble and fall into place. Thanks to the diligent prep work by the two team leads, we already had a workflow to easily take Mapbox Studio content offline. Shortly thereafter, the team worked on a beautiful style guide and branding for the application, a login system for viewing restricted content and editing, the ability to add points and stories to the map and to upload and view videos, and a user interface design that brings it all together. And it all runs offline! I almost couldn’t believe what I was seeing. In the span of three short days, the team was able to present the following:
> “We knew the [@Mapbox](https://twitter.com/Mapbox?ref_src=twsrc%5Etfw) API was going to be awesome, but also that we didn’t know how to use it…” team Terrastories [#RubyforGood2018](https://twitter.com/hashtag/RubyforGood2018?src=hash&ref_src=twsrc%5Etfw) [@RubyforGood](https://twitter.com/RubyforGood?ref_src=twsrc%5Etfw) [pic.twitter.com/t2OyYTulw7](https://t.co/t2OyYTulw7)
> — Erin Quinn (@EqMapbox) [June 10, 2018](https://twitter.com/EqMapbox/status/1005865896731082752?ref_src=twsrc%5Etfw)

Using Terrastories, the Matawai and other communities will be able to explore recordings of their oral history storytelling by interacting with the map and clicking on points where stories are located, or by using a sidebar card feature. Users will also be able to log in and access restricted stories (such as stories that should only be heard by specific community members, or restricted to outsiders) that are assigned to specific credentials, if necessary. Community members will also be able to add stories to the application, and edit them. The application will require only shapefiles, a map styled in Mapbox Studio, and limited setup before users can begin mapping their own place-based storytelling traditions, preserving and presenting them as an interactive learning tool for generations to come.

Terrastories is still a work in progress, and will continue to be worked on in the coming months. When it’s done, we will build the first portal for the Matawai Maroons, and bring it directly to the communities in the Surinamese rainforest for their review and feedback, which can be incorporated into the application design. Terrastories is built to be open-source, and we are excited to share this application with anybody who wants to use it, or expand it.

Our thanks go out to the Terrastories team at Ruby for Good, as well as the event organizers and our friends at Mapbox, for believing in this project, and for their amazing dedication. This would not have been possible without you, and we can’t wait to show this application to the communities!
