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
				<li>
					<a href="/team">Team</a>
				</li>
				<li>
					<a href="/about">About</a>
				</li>
			</ul>
		</div>
	);
};

export default Navbar;
