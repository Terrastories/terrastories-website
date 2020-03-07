import React from "react";
import LogoMark from "./logomark";
import LogoCombo from "./logocombo";

const Navbar = () => {
	return (
		<div className="nav">
			<a href="/">
				<LogoCombo />
			</a>
			<ul>
				<li className="nav-item home">
					<a href="/">Home</a>
				</li>
				<li className="nav-item">
					<a href="/get-involved">Get Involved</a>
				</li>
				<li className="nav-item">
					<a href="/gallery">Gallery</a>
				</li>
				<li className="nav-item">
					<a href="/about">About</a>
				</li>
				<li className="nav-item cta">
					<a href="/download">Download</a>
				</li>
			</ul>
		</div>
	);
};

export default Navbar;
