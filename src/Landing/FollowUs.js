import React from "react";
import styled from "styled-components";
import { FaGithub } from "react-icons/fa";
import { AiFillTwitterCircle } from "react-icons/ai";
import { Row, Column } from "../styled-components/layout";
import { BannerHeader } from "../styled-components/banners";

const FollowBar = styled(Row)`
	background-color: #33aa8b;
	height: 75px;
	justify-content: flex-start;
	padding-left: 50px;
	margin-top: 10px;
`;

const IconLink = styled.a`
	color: white;
	padding: 5px;
	:hover {
		background-color: #09697e;
	}
	:focus {
		background-color: #09697e;
		outline: none;
	}
`;

const FollowContent = styled.div`
	display: flex;
	align-items: center;
	padding-top: 5px;
	padding-bottom: 5px;
`;

const FollowUs = () => {
	return (
		<FollowBar width="100%">
			<FollowContent>
				<Column gapRight="50px">
					<BannerHeader color="white" size="30pt">
						FOLLOW US
					</BannerHeader>
				</Column>
				<Column gapRight="50px">
					<IconLink href="https://github.com/Terrastories">
						<FaGithub color="white" size="40px" />
					</IconLink>
				</Column>
				<Column gapRight="50px">
					<IconLink href="https://twitter.com/TerrastoriesApp">
						<AiFillTwitterCircle color="white" size="45px" />
					</IconLink>
				</Column>
			</FollowContent>
		</FollowBar>
	);
};

export default FollowUs;
