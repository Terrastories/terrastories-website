---
author: rkemper
author_name: rkemper
categories:
- Dev Stories
- User Stories
date: 2018-11-14 21:20:00+00:00
excerpt: The classroom was abuzz. Groups of students sat together around mobile phones,
  exploring a digital map of their traditional homeland, watching videos of their
  elders telling stories of community history and traditions. Watching them, I could
  tell that the Terrastories project was onto something.
featured_image: /media/images/288_0_rfT_psmWY-PspSb9.jpg
featured_image_id: 288
link: /mapping-oral-history-in-the-rainforests-of-suriname
modified: 2020-08-27 21:48:13+00:00
og_image: /media/images/288_0_rfT_psmWY-PspSb9.jpg
seo_description: Terrastories is a geostorytelling application built to enable indigenous
  and other local communities to locate and map their oral storytelling traditions.
seo_title: Mapping oral history in the rainforests of Suriname - Terrastories
slug: mapping-oral-history-in-the-rainforests-of-suriname
status: publish
title: Mapping oral history in the rainforests of Suriname
type: post
---

## Field testing Terrastories to help communities protect place-based cultural knowledge

*By Kalimar Maia, Terrastories Steward. Originally published on the Mapbox blog[here](<https://blog.mapbox.com/mapping-oral-history-in-the-rainforests-of-suriname-2f94ef1d765b>).*

> For us, it is so important to be able to document and preserve our stories. It gives me a feeling of pride to be a Matawai, because it enables me to know my roots. And I am so grateful to ACT and Mapbox for helping us. — Tina Henkie, basja (a traditional authority figure), Pusugrunu

The classroom was abuzz. Groups of students sat together around mobile phones, exploring a digital map of their traditional homeland, watching videos of their elders telling stories of community history and traditions. Watching them, I could tell that the Terrastories project was onto something.

I was in Pusungrunu, one of the ten Matawai villages in central Suriname that have been working with [Amazon Conservation Team (ACT)](<https://www.amazonteam.org/terrastories/>) to [map the rainforest surrounding the Saramacca River](<https://www.amazonteam.org/land-and-history-among-the-matawai-of-suriname/>) since 2015. I traveled 22 hours from Washington D.C. to Suriname and another 5 hours by dirt road to be here to help test the first version of [Terrastories](<https://www.amazonteam.org/terrastories/>), a geostorytelling application that enables local communities to create and use interactive digital maps that locate their stories, traditions, and their places of significant meaning or value within their territories.

![](/media/images/Capture-2-1024x473.png)_From Washington, DC to Pusugrunu, Suriname._

The Matawai are Maroons, descendants of Africans who escaped slavery in the 17th and 18th centuries. Matawai history, culture, and land management traditions are taught through the stories told by elders. However, this knowledge is at risk as community members leave to look for work and as resource extraction, including gold mining, encroaches on the rainforest.

![](/media/images/Capture-3-1024x607.png)_Scenes from the village._

Together, ACT and the Matawai decided to use the territory mapping as an opportunity to record and preserve Matawai oral history. By weaving video interviews with elders into an interactive map, the project will help future generations stay connected to their territory, culture, and history while preserving the landscape context necessary for this place-based knowledge.

> When plotted on a map, the stories create a multi-dimensional representation of the Matawai experience, past and present. — Rudo Kemper, Amazon Conservation Team

From the beginning, the goal of Terrastories was to create a community-based content management system (CMS) for the Matawai themselves, not for global audiences. It needed to work completely offline, within the community. The interface had to be user-friendly and intuitive, and use words from the Matawai language, so that community members could add places, photos, videos and written narratives themselves. And it had to offer the ability for selected Matawai administrators to set varying levels of access — a vital feature for preserving local control and protecting sensitive sites from exploitation and abuse, such as the recent [destruction of sacred Xingu drawings by vandals](<https://noticias.r7.com/tecnologia-e-ciencia/ato-de-vandalismo-destroi-gravuras-historicas-sobre-mito-indigena-em-caverna-do-xingu-28092018>) in the Kamukuwaká in Brazil. The clarity of vision was there — the question was how to build it. ACT was already using Mapbox Studio to create custom styled maps, so the team reached out to us to see if we could help.

Building this highly customized application would require a skilled team and a significant amount of development time. As luck would have it, ACT’s request coincided with project selection for [Ruby For Good](<https://rubyforgood.org/>) 2018, an annual coding retreat for volunteers to build technology for non-profits that Mapbox sponsored this year. As one of the founders and organizers of Ruby For Good, and as a Mapbox Sales Engineer, I was excited to see how our communities could come together to build something uniquely tailored to the needs of the Matawai and other similar communities. Ten people and three days later we had the beginning of a Terrastories application that could run an interactive map experience on desktop and mobile, completely offline.

Over the next four months, Ruby for Good volunteers and I continued work on the app to have it ready in time for ACT’s October field visit, so it could be tested with students and teachers at the Matawai’s school. After investing over 450 hours, we wanted to have someone on the ground for the initial testing to help with debugging and to observe the app in action. With Mapbox’s support, I traveled to the remote part of Suriname that I’d been looking at on my screen all these months.

The night before our presentation to the school, there was some final debugging to do. We had to wait for the village generator to start up because it only runs from 6 pm — 11 pm. We didn’t have a monitor so we had to hook up the projector and display it on the wall. I’m really glad I was there to work directly on the (offline!) computer we set up for the demo, otherwise the months of work completed by the team would not have been available for the students to see.

![](/media/images/0_oFegjSovPcSRnCI7.jpg)_Final debugging, once the generator was turned on._

All of this was well worth the effort when we presented Terrastories at the community school.

The students in the Pusungrunu school spent about an hour exploring the app, listening and watching stories told by the elders. It was valuable to user test this early version directly with the Matawai. While in the field we found bugs and limitations — such as video streaming crashing, or the network card on the computer only being able to handle three simultaneous users — and we identified UI/UX changes that will enhance the editor/admin experience. While there is still a lot of work to do on Terrastories, judging from the students’ interaction we feel like it was a real success.

![](/media/images/0_iDBIN3pVhz6lyvRM-1.jpg)
![](/media/images/0_XFgPtLQQvDJ-u6Gn.jpg)
![](/media/images/0_rfT_psmWY-PspSb9-1-1024x677.jpg)
![](/media/images/0_fTNAwjMbM7HTyqVl-1.jpg)

_Students in the Pusungrunu school exploring Terrastories for the first time._

> This is really an invaluable tool. Our school is in dire need of resources to make the lessons more engaging and meaningful for the children, and [with Terrastories] we have a tool to be able to teach history, geography, language and culture all in one. — Paul Redmond, School Principal, Public School of Pusugrunu

Terrastories isn’t only a tool for the Matawai. Once the app is ready for a more robust deployment, ACT will share it with additional partner communities — including the Wauja in Brazil and the Kogui in Colombia. And ACT, Mapbox, and the Ruby for Good volunteers are building Terrastories as an open source tool so that organizations and communities around the world will be able to use it.

If you are interested in volunteering your skills on Terrastories, please check out our [GitHub page](<https://github.com/rubyforgood/terrastories>) to get involved. If you are an organization interested in undertaking check out other community team projects get in touch with our [Community Team](<https://www.mapbox.com/community/?utm_campaign=terrastories-blog&utm_medium=blog&utm_source=community-page>).
