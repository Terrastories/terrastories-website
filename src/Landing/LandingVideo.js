import React from "react";
import "video-react/dist/video-react.css";
import { Player } from "video-react";

const LandingVideo = () => {
	return (
		<Player width={4} fluid="false">
			<source src="" />
		</Player>
	);
};

export default LandingVideo;
