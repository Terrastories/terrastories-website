import styled from "styled-components";

export const BannerHeader = styled.h1`
	color: ${props => props.color};
	font-size: ${props => props.size};
`;

BannerHeader.defaultProps = {
	color: "white",
	size: "45pt"
};

export const BannerWrapper = styled.div`
	margin-bottom: ${props => props.gapBottom};
`;

BannerWrapper.defaultProps = {
	gapBottom: "20px"
};

export const Text = styled.p`
	padding: 0;
	margin: 0;
	font-size: ${props => props.fontSize};
	color: ${props => props.color};
`;

Text.defaultProps = {
	color: "white",
	fontSize: "1.3rem"
};

export const Banner = styled.div`
	width: 100%;
	min-height: ${props => props.height};
	align-items: center;
	justify-content: center;
	display: flex;
	flex-direction: column;
	background-color: ${props => props.bgColor};
`;

Banner.defaultProps = {
	bgColor: "#09697e",
	height: "50vh"
};

export const BannerContent = styled.div`
	text-align: center;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 5em;
	position: absolute;
	width: 100%;
	opacity: 1;
	margin-bottom: ${props => props.gapBottom};
	color: ${props => props.color};
	margin-top: ${props => props.gapTop};
`;

BannerContent.defaultProps = {
	color: "white",
	gapTop: "2em",
	gapBottom: "1em"
};
