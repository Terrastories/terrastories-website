---
categories:
- Dev Stories
date: 2020-12-31 05:26:20+00:00
excerpt: In the spirit of sharing positive stories to end a bleak year, I would like
  to tell you about some of the major highlights for Terrastories in 2020 that we
  achieved in spite of the pandemic.
featured_image: /media/images/451_IMW2020-Terrastories-Map.jpg
featured_image_id: 451
link: /open-source-volunteerism-and-oral-histories-mapping-during-a-pandemic-terrastories-2020-in-review
og_image: /media/images/451_IMW2020-Terrastories-Map.jpg
seo_description: Terrastories is a geostorytelling application built to enable indigenous
  and other local communities to locate and map their oral storytelling traditions.
seo_title: 'Open-source volunteerism and oral histories mapping, during a pandemic:
  Terrastories 2020 in review 🌏💬 - Terrastories'
slug: open-source-volunteerism-and-oral-histories-mapping-during-a-pandemic-terrastories-2020-in-review
status: publish
title: 'Open-source volunteerism and oral histories mapping, during a pandemic: Terrastories
  2020 in review 🌏💬'
type: post
---

* * *

Needless to say, it’s been a crazy year, and literally nothing went according to plan.

As the world shut down at the beginning of 2020, our daily lives were completely disrupted, and plans to travel or host events rapidly unraveled. For many volunteer projects that generally rely on people getting together in person, this meant trying to figure out how do things over Zoom.

For us at [Terrastories](<https://terrastories.app>), the situation was no different.

![](https://cdn-images-1.medium.com/max/1000/1*uA35Uc_2rLiTKb0nr5QTEg.png)

After the initial shock of the pandemic lapsed, our Terrastories stewards went to work devising how we can continue to build and encourage volunteer contributions to our scrappy FOSS (free and open-source) geostorytelling application, and how to provide our community users with support, all while sitting at home. Looking back on this surreal and whirlwind year, we managed to achieve quite a lot.

In the spirit of [sharing positive stories](<https://news.mongabay.com/2020/12/top-positive-environmental-stories-from-2020/>) to end a bleak year, we would like to tell you about **some of the major highlights for Terrastories in 2020** that we achieved in spite of the pandemic, and to **celebrate the people who played a part in helping build Terrastories** in the midst of an incredibly tough moment for the world and for all of us personally.

In what follows:

* Remote volunteering during a pandemic 👩‍💻
* Online support for Indigenous communities in getting started with Terrastories 💻
* New and existing partnerships and collaboration 🙌
* We launched our website (and a public roadmap) 🎉
* Thank you 🙏

![](https://cdn-images-1.medium.com/max/1500/1*le5-aMugxl8eA4LSBEGu4w.png)Terrastories in 2020: screenshot from the live demo prepared for the Indigenous Mapping Workshop in November 2020.

* * *

## Remote volunteering during a pandemic [👩‍💻](<https://emojipedia.org/woman-technologist/>)

Long before the pandemic began, our friends at [Ruby for Good](<http://rubyforgood.org/>) invited us back to their Spring coding event Ruby by the Bay. The event was supposed to be held at the NatureBridge campus six miles away from the Golden Gate Bridge in San Francisco, but ended up being a virtual meetup spread across two weekends in April.

Experimental in form by necessity, our Terrastories team decided to take a mob programming approach with all participants looking at the same code, instead of a more standard hackathon convention of splitting off and working on problems in a pair or individually. We frequently took pause to ensure that everyone, including the more junior level developers, understood how the code works.

![](/media/images/classic-logo.png)

![](https://cdn-images-1.medium.com/max/1000/1*zeAfWN_sa2J4puDOjs5Nyw.png)Team Terrastories at Ruby by the Bay remote 2020. Shout out to the entire team: Betsey Haibel, Bransyn Luther, Kendra Lockard, Sarah Laloggia, and team leads Mae Beale and Ian Norris.

While this resulted in us not getting as much work done as per the usual breakneck speed at Ruby for Good, the participants felt like they understood the Terrastories codebase much better and got more out of the experience. A few participants continued to work on Terrastories after the coding event ended: Sarah Laloggia, one of our team members who was relatively new to software engineering, continued to work on the curriculum builder project for months after Ruby by the Bay, bringing this new and highly demanded feature very close to completion as we close out the year.

In addition to Ruby for Good, a number of developers got in touch with us independently to work on Terrastories after finding out about the application through presentations at [csv,conf,5.0](<https://www.youtube.com/watch?v=j-mDnMjDnq4&feature=emb_title>) and elsewhere. Among them were Lucas Alcantara, Katherine Henry, and Oliver Hamuy, three students from Washington University in St. Louis.

![](https://cdn-images-1.medium.com/max/1000/1*UzibeSsunWn7pbwmGHC3-Q.png)Lucas Alcantara, Katherine Henry, and Oliver Hamuy (WUSTL)

Lucas, Katherine and Oliver were supposed to have a practical internship lined up for the spring or summer semester this year, which fell through the cracks due to the pandemic. The same happened to many of their peers, prompting an adjunct instructor at the university to set up a summer course called “Software Engineering Workshop” where they can get credit for contributing remotely to an open-source project. The students opted to contribute to Terrastories as their project, and throughout the summer [worked on resolving a number of issues and building new features for Terrastories](<https://terrastories.app/developing-terrastories-for-college-credit/>). Our thanks go out to Lucas, Katherine and Oliver for their amazing work.

> I liked how communicative the team was, and very supportive, and as Lucas said, very beginning friendly. You guys were super welcoming when we started out. When we were just researching the project, there were links to the #terrastories channel on the Ruby for Good Slack which was really nice, which we joined and when we reached out we got very quick responses. — Katherine Henry

![](https://cdn-images-1.medium.com/max/750/1*D-Oz_aHkRwkIlIUGtFpr6A.png)*A Sunday pair-a-stories session on  Zoom.*

To help volunteers like the WUSTL students and Sarah Laloggia meet their goals, Terrastories steward Ian Norris proposed hosting a regularly scheduled space over Zoom where folks could share what they’re working on, ask questions, and investigate a problem as a group. These Sunday sessions became known as *pair-a-stories,* and were very consistently attended over the summer. (Shout out to Ian for regular hosting!)

[Participating in the annual Hacktoberfest in October was very productive for us last year](<https://rudokemper.medium.com/a-very-happy-hacktoberfest-for-terrastories-and-the-ruby-community-9e472d9e85d3>), and this year we again scoped out several epics for the occasion, receiving 18 commits from a handful of first-time contributors.

All said and done, these were some of the major volunteer contributions to Terrastories this year:

* Easy setup for both online mode 🌐 and offline “fieldkit” mode 🌴
* Refactoring place markers into Mapbox GL JS 🗺️
* A new Theme feature for communities to set visual assets, color scheme, and map parameters via the administrative UI 🎨
* A new Curriculum Builder feature to enable communities to set up custom curriculums composed of selected stories that will play in a linear order. (Implementing a UX design created at Ruby by the Bay 2019) 🏫
* Setting up a minimum viable end to end testing framework, and validations in numerous areas 🧐
* Adding sponsor logos to the Terrastories welcome page ❤️
* Possibility to embed media content for online Terrastories instances 🔗
* UI improvements in certain areas like the administrative back end 👩‍🎨
* Workflow for setting up online demos on Heroku ⚛️
* Much improved documentation 📜
* Numerous bugs squashed 🔨🐛

It would be difficult to name every person who contributed to each of these accomplishments, but please know that we are incredibly grateful for your time and efforts ❤

* * *

## Online support for Indigenous communities in getting started with Terrastories 💻

The pandemic also prompted us to consider preparing virtual demos and training materials for our partners that are currently using Terrastories, and other Indigenous communities globally who are feeling the urgency of [taking action to preserve traditional knowledge](<https://www.culturalsurvival.org/news/indigenous-peoples-turning-traditional-knowledge-covid-19-response>).

![](https://cdn-images-1.medium.com/max/1000/1*eGqNX0Py8XGUZmylq23dWg.jpeg)

In June, the [GEO Indigenous Alliance](<https://www.earthobservations.org/indigenoussummit2020.php>) organized a hackathon called GEO Indigenous Hack4Covid with multiple challenges submitted by Indigenous leaders for participants to work on. One of the challenges was posed by James Rattling Leaf Sr. from the Rosebud Sioux Tribe in South Dakota, calling for an application that he termed Lapi Wowapiin in his native Lakota language, translating to “to write something for a purpose”.

The challenge called for an app that will support the transmission of knowledge between the Elders and the youth while advancing the use of the Lakota language via digital stories that have a connection with the landscape. [For this Hackathon, we submitted a demo build of Terrastories for the Lakota](<https://terrastories.app/geo-indigenous-hack4covid-terrastories-is-preserving-history-using-storytelling-and-geo-mapping/>) to **give the Rosebud Sioux Tribe and other communities a concrete idea of how the application can serve their needs.**

The Terrastories “Lakota Makha” build won second place in the hackathon, and we [were able to present on our work at this year’s GEO Indigenous Summit](<https://earthobservations.org/indigenoussummit2020.php>). Our thanks go out to James Rattling Leaf Sr. for his thoughtful challenge, and his continued support following the hackathon.

![](https://cdn-images-1.medium.com/max/1000/1*X9rfctspaIBFhjHdSXzs9w.png)

Last month, we had the privilege of hosting a 45 minute technical session about using Terrastories at the virtual [Indigenous Mapping Workshop](<https://www.indigenousmaps.com/>), for the benefit of the global Indigenous mapping community. This was the first time that we were able to provide a comprehensive and practical demo on how to use Terrastories, and we are grateful for the Indigenous Mapping Workshop team for the opportunity!

In preparation for the workshop, **we created three hands-on tutorials with accompanying videos, a 15 minute video walkthrough of how Terrastories works, and a live demo** , [all available on our website](<https://terrastories.app/tutorials/>).

A 15 minute walkthrough of how Terrastories works.

In 2021, we will continue to collaborate with the Indigenous Mapping Workshop to host more Terrastories training modules.

With the application in stable condition and new training materials made available, we are looking forward to remotely helping any community in the world in getting started mapping place-based stories with Terrastories!

* * *

## New and existing partnerships and collaboration 🙌

![](https://cdn-images-1.medium.com/max/1000/1*x5FlUnv40sUyMyafmvISxA.jpeg)

Terrastories was born out mapping oral histories fieldwork with [the Amazon Conservation Team](<http://amazonteam.org/>) (ACT), and ACT continues to be deeply involved in stewarding Terrastories.

Although the ACT team wasn’t able to travel to the field to get the latest versions of the application to partner communities such as the Matawai, Wauja and Tarëno residing in remote and offline conditions in the rainforest, the organization is looking to do so next year and also support other Indigenous communities in Colombia and Suriname in working with Terrastories.

This year, ACT [featured Terrastories in a storytelling map](<https://storymaps.arcgis.com/collections/198cd38e98014dbe9b926d3d20011f98?item=6>) about the oral history of the Matawai Maroons in Suriname, the first community to use the app.

![](https://cdn-images-1.medium.com/max/1000/1*ZYDt0MQW0vBu5G4rHupQxg.png)From the ACT Storytelling Map “Lands of Freedom: The oral history and cultural heritage of the Matawai Maroons in Suriname.”

![](https://cdn-images-1.medium.com/max/750/1*33Y3QdmX-7zvF4OZ4_fpvQ.jpeg)

In 2020, we embarked on a new partnership with the Silicon Valley’s nonprofit tech for good company [Tech Matters](<https://techmatters.org/>).

Tech Matters is building an integrative landscape management platform called Terraso, and what they kept hearing from local landscape leaders is that they need tools that are free, allow them to control their own data, provision maps and videos, and can work offline.

Our colleagues at Tech Matters found that Terrastories matches those needs pretty closely, and so they graciously funded us to improve the Terrastories administrative UI and to build out a new multi-instance architecture enabling multiple communities to host their maps and stories on one Terrastories server while still being able to protect and restrict their data. Our friend [Laura Mosher](<https://laura.mosher.tech/>) from the Ruby for Good community worked diligently in the final months of 2020 to get the work done, and we are very proud of what she accomplished during a short time.

![](https://cdn-images-1.medium.com/max/1000/1*rLJ5xRgm3hQjWaKhgg1ILA.jpeg)New administrative / back end UI with a dashboard view.

We are very grateful to Tech Matters for offering us the very first funding opportunity that Terrastories has received to date, to Laura for her amazing work, and to ACT for fiscally sponsoring.

![](https://cdn-images-1.medium.com/max/750/1*MeNQig4kl9Xt_-rXLz7P2g.png)

Another exciting partnership on the horizon for Terrastories is our participation in the [Earth Defenders Toolkit](<https://terrastories.app>), a new collection of open-source tools and training materials for communities on the frontlines of the struggle to defend critical ecosystems around the world.

Stewarded by the non-profit organization [Digital Democracy](<http://digital-democracy.org/>), the ultimate goal of the Earth Defenders Toolkit is to do better at ensuring that frontline communities [can use these tools directly without creating dependency on outside support](<https://rudokemper.medium.com/co-creating-an-earth-defenders-toolkit-with-the-indigenous-mapping-community-at-2020imw-16df7054ee4a>).

We are thrilled that Terrastories will take part and look forward to preparing content user manuals about using Terrastories for Indigenous and other communities directly in 2021.

![](https://cdn-images-1.medium.com/max/750/1*fUZgZAE5Ea7qrVxm_8rMig.png)

Lastly, at the tail end of 2020 we started to work more closely with [Ohneganos Ohnegahdę:gyo](<https://www.ohneganos.com/>), an Indigenous water research program in Canada who are using Terrastories to [map traditional Haudenosaunee place names, traditional ecological knowledge, and oral histories within the Six Nations Reserve and the Grand River](<https://terrastories.app/from-the-amazon-to-the-great-lakes-sharing-knowledge-and-mapping-oral-histories-with-first-nations-communities-in-canada/>).

Ohneganos are now the second organization to secure funding to work with Terrastories to do oral histories mapping, after ACT. We are looking forward to working closely with their team and the Haudenosaunee community at Six Nations Reserve next year.

* * *

## We launched our website (and a public roadmap) 🎉

![](https://cdn-images-1.medium.com/max/1000/1*fkX0nxkVVffo7Kfu0oHhGw.jpeg)Introducing terrastories.app!

Last but not least, a major milestone for us was**the launch of the Terrastories website**. It’s been a long term goal to have a central place bringing together user-friendly instructions on how to download and work with Terrastories, stories from partner communities using the app, a live demo, and other information about the application and our team.

![](https://cdn-images-1.medium.com/max/750/1*dXaKsXdvOrTDCSTC9mdYbQ.jpeg)

In addition to resources for using the application, we created a section for our **developer community** featuring information on how to contribute, stories from volunteers about working on Terrastories, and a shout out to everyone that has contributed to Terrastories.

For developers, we also considered that we should make it much easier for potential volunteers to figure out what’s going on with the project, especially in lieu of not being able to meet up in person for build-a-thons or code nights. We created a [Wiki](<https://github.com/Terrastories/terrastories/wiki>) on our Github page featuring resources for developers, technical documentation, a vision statement, and **our very first public**[**roadmap**](<https://github.com/Terrastories/terrastories/wiki/Terrastories-Roadmap>). We also adopted a consistent labeling convention for our [Github issues](<https://github.com/Terrastories/terrastories/labels>), “ready to start” definitions and templates for writing issues, and scoped out epics per the roadmap.

For anyone interested in Terrastories, we created a mailing list to periodically circulate posts like the one you’re reading! [Sign up here](<https://terrastories.app/mailing-list/>).

* * *

## Thank you 🙏

To everyone who contributed to Terrastories in 2020 — whether it was out of motivation to build something small but meaningful for marginalized communities to help them in their efforts to hold on to their traditional knowledge in light of overwhelming forces like COVID-19 or environmental destruction, or just to have something to do to stay sane while stuck at home, or both — and everyone who believed that the application could be useful to them or someone else, **thank you for believing in our mission**. We couldn’t have gotten this far without you, and we hope you will continue to stay part of our community.

To contribute to Terrastories as a volunteer, check out our [developer community page](<https://terrastories.app/community/>).
To stay up to date with all things Terrastories, [sign up](<https://terrastories.app/mailing-list/>) to our mailing list.
If you would like to get in touch about using Terrastories, or supporting our work in 2021 in another way, please [contact us](<https://terrastories.app/contact-us/>).

Best wishes for a happy new year from the Terrastories stewards team ✨
