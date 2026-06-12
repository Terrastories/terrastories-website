---
author: rkemper
author_name: rkemper
categories:
- Dev Stories
date: 2019-11-05 20:06:00+00:00
excerpt: It’s been almost a year and a half since I became acquainted with a wonderful
  community of open-source Ruby developers. At the time, I was scurrying from one
  corporate office to another, trying to find the right party to build a geostorytelling
  application for my organization, the Amazon Conservation Team…
featured_image: /media/images/262_1_gaZxKq8EVtyvk0pWzjkJYA.jpeg
featured_image_id: 262
link: /a-very-happy-hacktoberfest-for-terrastories-and-the-ruby-community-%f0%9f%8e%83
modified: 2020-08-27 21:48:05+00:00
og_image: /media/images/262_1_gaZxKq8EVtyvk0pWzjkJYA.jpeg
seo_description: Terrastories is a geostorytelling application built to enable indigenous
  and other local communities to locate and map their oral storytelling traditions.
seo_title: 'A very happy #Hacktoberfest for Terrastories and the Ruby community 🎃
  - Terrastories'
slug: a-very-happy-hacktoberfest-for-terrastories-and-the-ruby-community
status: publish
title: 'A very happy #Hacktoberfest for Terrastories and the Ruby community 🎃'
type: post
---


By Rudo Kemper. November 5, 2019. Originally posted on [Medium](https://medium.com/@rudokemper/a-very-happy-hacktoberfest-for-terrastories-and-the-ruby-community-9e472d9e85d3).

It’s been almost a year and a half since I became acquainted with a wonderful community of open-source Ruby developers. At the time, I was scurrying from one corporate office to another, trying to find the right party to build a geostorytelling application for my organization, the [Amazon Conservation Team](https://amazonteam.org/).

We were working with an Amazonian community called the Matawai to [record and map their oral history storytelling traditions](https://www.youtube.com/watch?v=KJQKVb5NEHI), and had the idea of building a custom application that could combine interactive maps of the Matawai’s ancestral lands with videos of the elders telling stories about historically and culturally significant places. Inspired by other [local-first software initiatives](https://www.digital-democracy.org/blog/localfirst/), we wanted the application to work entirely without internet access in the Matawai villages, deep in the rainforests of Suriname.
![](/media/images/259_1_pvhqOklbS1s-iDeXKCselw.jpeg)

Matawai elders sharing oral histories about their landscape in the village of Misalibi. Photo credit: Mediavision.

Eventually, I found my way to the offices of the location platform company Mapbox, where I met their [community team](https://www.mapbox.com/community/) and by a stroke of luck, learned that they were sponsoring an event called [Ruby for Good](https://rubyforgood.org/). United by the appealingly simple ethic of MINASWAN, or Matz Is Nice And So We Are Nice (referring to the Japanese computer scientist, Yukihiro “Matz” Matsumoto, who created the Ruby language), at Ruby for Good volunteer developers come together to work on Ruby projects that do something good for the world.

At Ruby for Good projects range from applications serving to optimize diaper banks; providing resources on safe restroom access for transgender, intersex, and gender nonconforming individuals; helping provide emotional and legal support to survivors of domestic abuse; and serving analytics for abalone species population tracking. We pitched our geostorytelling application idea, the Ruby for Good organizing team liked it and accepted it for the list of projects for the summer 2018 event, and so, [Terrastories](/) was born!
![](/media/images/260_1_RKG3I3LuMdk4PSkq-pVWmQ.jpeg)

Ruby for Good 2018 team leads Miranda Wang and Jason Hinebaugh explaining the concept behind Terrastories to interested volunteers.

I have written [elsewhere](https://www.amazonteam.org/act-partakes-in-ruby-for-good-2018-to-develop-offline-geostorytelling-app-terrastories-for-remote-communities/) about that Ruby for Good experience, but what I want to emphasize here is something captured really well by Miranda Wang, one of the Terrastories stewards, in a recent [Storytime with Managers podcast interview](https://anchor.fm/cohere/episodes/Temporary-Teams-with-Miranda-Wang-e5hodq/a-aojmng) about her experience as a team lead for Terrastories in Ruby for Good 2018:
> When a group of strangers get together to collaborate on a project, it is possible to achieve an incredible amount of progress, and lay the foundation for building and cultivating a community.

Since starting to build Terrastories at that event, we’ve had over 500 contributions to the codebase by 50+ contributors [on our Github repo](https://github.com/terrastories/terrastories), and that is not counting the amazing work by designers, and others who have participated in the conversation on our #terrastories channel on the Ruby for Good Slack, which has over 80 members. Even more importantly, the Matawai community is in possession of a mini-computer containing the first build of Terrastories, populated with hundreds of recorded oral histories about their ancestral lands.
![](/media/images/261_1_oUQlRtC5bTCo-OFnvE8RuQ.jpeg)

Matawai kids interacting with Terrastories on a smartphone.

Some of that coding work has taken place at formally scheduled in-person events, like Ruby by the Bay 2019, but much of it has transpired entirely online. Led by the phenomenal leadership of stewards [Miranda Wang and Kalimar Maia](https://www.youtube.com/watch?v=f5YbOJ2UGcU), numerous Ruby volunteers have found their way to our community, making contributions and taking on a more active role, in some cases even joining our stewards team. Throughout the process, we’ve learned a lot about how to successfully manage an open-source project on Github, like the virtues behind having small and actionable tickets that are easy for a newcomer to plug away at, uncluttered labels that make your project easy to find, and auto commenting bots on pull requests.

Last month, we decided to try our luck at this year’s [Hacktoberfest](https://hacktoberfest.digitalocean.com/), an annual celebration of open-source software and coding challenge to contribute to open-source projects on Github in exchange for a t-shirt, organized by DigitalOcean and DEV. Throughout the month, volunteers pick tickets describing work that needs to be done on Github, and plug away at it.
![](/media/images/262_1_gaZxKq8EVtyvk0pWzjkJYA.jpeg)

We duly gardened our issues queue and added some Hacktoberfest labels, offered up a few prize items including some beautiful Terrastories pins sponsored by Mapbox, and hoped for the best. Amazingly, we received an overwhelming amount of interest from contributors across the world, including places like Brazil, Bulgaria, and Japan. All in all, a total of 24 people made 52 contributions to the Terrastories Github repo, resolving in the closing of 43% of the issues with a Hacktoberfest label! (And that percentage is current at the time of writing and bound to increase, because some submitted PRs still need to reviewed and merged.)

In a month’s time, the Terrastories development community was able to accomplish the following and more:

- The application now has tests, which will make it easier to deploy Terrastories and make the codebase more resistant to future bugs.
- A mini-map (aka overview map) to aid with geographical orientation was added to the top right of the map.
- Spanish and Japanese were added as language options for Terrastories, and the Portuguese translation has been improved.
- Photo and video content was added to the seed data, making it easier to demonstrate how Terrastories works [in our demo](http://terrastories.herokuapp.com/) and for future developers.
- Restricted stories now feature a small lock emoji to show logged in users which stories are restricted, and which ones are not.
- It is now possible to filter stories alphabetically (A-Z), or in the chronological order they were added.
- The map view now zooms and pans to filtered stories once they are selected using the filter dropdowns.
![](/media/images/263_1_QFYG4IAfSYbmraGiOJK5SQ.jpg)

Some of the new features like the sort dropdown, mini-map, and translation in the Japanese language!

These are all highly significant contributions towards making Terrastories a more stable and user-friendly application, and helps us along on our road map towards building Terrastories as a SaaS (Software as a Service), for serving and helping local communities across the world in preserving their storytelling traditions.

Once again, the global Ruby community truly demonstrated what MINASWAN is all about. On behalf of the Terrastories stewards team: our heartfelt thanks and huge shoutout to all of the volunteers, and to our friends at Mapbox and [Ovio](http://oviohub.com/) for getting the word out 🎃.