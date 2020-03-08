import React from "react";
import { Row, Column } from "../styled-components/layout";
import BannerImage from "../MediaFiles/ren-ran-232079-unsplash.png";
import {
	Banner,
	BannerContent,
	BannerHeader,
	Text,
	BannerWrapper
} from "../styled-components/banners";
import { ButtonSolid, ButtonOutline } from "../styled-components/buttons";
import styled from "styled-components";

const BackgroundImg = styled.img`
	width: 1500px;
	object-fit: cover;
	filter: brightness(60%);
`;

const Donate = () => {
	return (
		<>
			<Banner bgColor="#09697e" style={{ maxHeight: "25vh" }}>
				<BackgroundImg src={BannerImage} />
				<BannerContent styled={{ paddingBottom: "50px", paddingTop: "50px" }}>
					<BannerWrapper>
						<BannerHeader size="45pt">HELP US GROW</BannerHeader>
					</BannerWrapper>
					<Text color="white">
						We are a non-profit organization that depends on the
					</Text>
					<Text color="white">support and time of other humans that care.</Text>
					<Row>
						<Column>
							<ButtonSolid>BECOME A DONOR</ButtonSolid>
						</Column>
						<Column>
							<ButtonOutline>BE A CONTRIBUTOR</ButtonOutline>
						</Column>
					</Row>
				</BannerContent>
			</Banner>
		</>
	);
};

export default Donate;
