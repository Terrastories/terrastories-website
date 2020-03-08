import React from "react";
import { Row, Column } from "../styled-components/layout";
import {
	Banner,
	BannerContent,
	BannerHeader
} from "../styled-components/banners";
import { ButtonSolid } from "../styled-components/buttons";
import Holder from "holderjs";

Holder.addTheme("dark", {
	bg: "gainsboro"
});

const Acknowledgments = () => {
	return (
		<>
			<Banner
				bgColor="white"
				style={{ paddingBottom: "50px", paddingTop: "50px" }}
			>
				<BannerContent>
					<BannerHeader color="black">
						SPECIAL THANKS TO OUR PARTNERS
					</BannerHeader>
					<Row width="100%" justifyContent="center" gapTop="20px">
						<Column>
							<img
								alt="placeholder"
								className="clip-circle"
								src="holder.js/300x200?theme=dark"
							/>
						</Column>
						<Column>
							<img
								alt="placeholder"
								className="clip-circle"
								src="holder.js/300x200?theme=dark"
							/>
						</Column>
						<Column>
							<img
								alt="placeholder"
								className="clip-circle"
								src="holder.js/300x200?theme=dark"
							/>
						</Column>
					</Row>
					<ButtonSolid>BECOME A PARTNER</ButtonSolid>
				</BannerContent>
			</Banner>
		</>
	);
};

export default Acknowledgments;
