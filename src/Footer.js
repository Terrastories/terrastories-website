import React from "react";
import { Banner, BannerContent } from "./styled-components/banners";
import styled from "styled-components";
import { Column } from "./styled-components/layout";
import LogoMarkInverted from "./svgComponents/logomark-inverted";
import FooterBackground from "./svgComponents/footerbg";

const FooterNav = styled.ul`
	list-style: none;
	text-align: left;
`;

const FooterNavItem = styled.li`
	color: white;
	font-size: 13pt;
	font-family: "Open Sans";
	line-height: 25px;
`;

const Footer = () => {
	return (
		<>
			<Banner bgColor="#09697e" height="25vh">
				<FooterBackground />
				<BannerContent gapTop="5px">
					<Column alignItems="flex-start" gapRight="auto" gapLeft="100px">
						<FooterNav>
							<LogoMarkInverted />
							<FooterNavItem>Contact Us</FooterNavItem>
							<FooterNavItem>About</FooterNavItem>
							<FooterNavItem>Blog</FooterNavItem>
							<FooterNavItem>GitHub</FooterNavItem>
						</FooterNav>
					</Column>
				</BannerContent>
			</Banner>
		</>
	);
};

export default Footer;
