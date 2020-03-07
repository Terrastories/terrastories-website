import React from "react";
import bgImage from "./assets/welcome-bg.jpg";
import styled from "styled-components";
import Blogs from "./Blogs";

const Header = styled.h1`
	color: #09697e;
`;

const Text = styled.p`
	padding: 0;
	margin: 0;
	font-size: 1.3rem;
	color: white;
`;
const Landing = () => {
	return (
		<>
			<header className="jumbo">
				<img src={bgImage} />
				<div className="jumbo-text">
					<h1>TERRASTORIES:</h1>
					<h1>CONNECTING GENERATIONS</h1>
					<Text>A geostorytelling application designed for</Text>
					<Text> communities to safeguard oral histories</Text>
					<button className="cta-button">DOWNLOAD</button>
				</div>
			</header>
			<div className="landing main">
				<Header className="heading">WHAT WE DO</Header>
				<p>
					Terrastories is a geostorytelling application built to enable
					indigenous and other local communities to locate and map their own
					oral storytelling traditions about places of significant meaning or
					value to them. Community members can add places and stories through a
					user-friendly interface, and make decisions about designating certain
					stories as private or restricted. Built with the Mapbox platform,
					Terrastories works both online and offline, so that remote communities
					can access the application entirely without needing internet
					connectivity.
				</p>

				<p>
					The main Terrastories interface consists of an interactive map and a
					sidebar with media content. Users can explore the map and click on
					activated points to see the stories associated with those points.
					Alternatively, users can interact with the sidebar and click on
					stories to see where in the landscape these narratives took place.
				</p>

				<p>
					Through an administrative back end, users can also add, edit, and
					remove stories, or set them as restricted so that they are watchable
					only with a special login. Users can design and customize the content
					of the interactive map entirely, and the interface itself is
					customizable with a color scheme and design reflecting the style of
					the community.
				</p>
			</div>
			<Blogs />
		</>
	);
};

export default Landing;
