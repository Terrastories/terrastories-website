import React from "react";
import LogoCombo from "./svgComponents/logocombo";
import { Column, Row } from "./styled-components/layout";

const Navbar = () => {
	return (
		<div className="nav">
			<Column
				className="navbar-brand"
				alignItems="flex-start"
				justifyContent="center"
			>
				<a href="/">
					<LogoCombo />
				</a>
			</Column>
			<Column alignItems="flex-end">
				<Row justifyContent="space-evenly">
					<ul>
						<li className="nav-item home">
							<a href="/">HOME</a>
						</li>
						<li className="nav-item">
							<a href="/get-involved">GET INVOLVED</a>
						</li>
						<li className="nav-item">
							<a href="/gallery">GALLERY</a>
						</li>
						<li className="nav-item">
							<a href="/about">ABOUT</a>
						</li>
						<li className="nav-item cta">
							<a href="/download">DOWNLOAD</a>
						</li>
					</ul>
				</Row>
			</Column>
		</div>
	);
};

export default Navbar;
