import React from "react";
import bgImage from "./assets/welcome-bg.jpg";

const Landing = () => {
	return (
		<>
			<header className="jumbo">
				<img src={bgImage} />
				<div className="jumbo-text">
					<p>
						<strong>Terrastories: </strong>
					</p>
					<p>
						A geostorytelling application designed for communities to safeguard
						oral histories
					</p>
				</div>
			</header>
			<div className="main">
				<p>
					Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur
					finibus lacus sapien, non pellentesque enim dignissim semper.
					Curabitur viverra aliquet volutpat. Aliquam vehicula urna felis, a
					tempor odio ullamcorper commodo. Cras eu est vestibulum, egestas metus
					vel, laoreet metus. Ut lacinia lacinia diam, id mattis elit vehicula
					in. Nullam a sapien eget tellus ornare sodales. Praesent egestas lacus
					quis condimentum tempor. Sed egestas ut tellus in condimentum. Nullam
					libero mauris, scelerisque vitae consectetur at, commodo eu tellus.
					Maecenas aliquet placerat enim, id suscipit nibh lobortis quis. Nam ac
					arcu nec quam vestibulum sagittis. Aenean lacinia tempor leo, id
					porttitor dolor interdum at.
				</p>
			</div>
		</>
	);
};

export default Landing;
