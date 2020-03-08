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
					<FaGithub color="white" size="40px" />
				</Column>
				<Column gapRight="50px">
					<AiFillTwitterCircle color="white" size="45px" />
				</Column>
			</FollowContent>
		</FollowBar>
	);
};

export default FollowUs;
