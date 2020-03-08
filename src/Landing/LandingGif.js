import React from "react";
import styled from "styled-components";
import terrastoriesGif from "../MediaFiles/terrastories.gif";

const GifWrapper = styled.div`
	display: flex;
	justify-content: center;
	padding: 10px;
	margin-top: 25px;
`;

const Gif = styled.img`
	max-width: 800px;
	object-fit: contain;
`;

const LandingGif = () => {
	return (
		<>
			<GifWrapper>
				<Gif src={terrastoriesGif} alt="project screenshots" />
			</GifWrapper>
		</>
	);
};

export default LandingGif;
