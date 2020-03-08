import React from "react";
import { Column, Row } from "../styled-components/layout";
import styled from "styled-components";
import Holder from "holderjs";

Holder.addTheme("dark", {
	//bg: "#33AA8B"
	bg: "gainsboro"
});

const BlogTitle = styled.h1`
	font-size: 40px;
`;

const BlogTextWrapper = styled.div`
	overflow: hidden;
	text-overflow: ellipsis;
`;

const BlogText = styled.p`
	font-size: 11pt;
`;

const BlogThumbnail = styled.div``;

const Blogs = () => {
	return (
		<>
			<Row gapTop="2em" justifyContent="center" className="blogs" width="100%">
				<Column
					textAlign="center"
					alignItems="space-between"
					gapLeft="3em"
					gapRight="3em"
				>
					<BlogThumbnail>
						<img alt="placeholder" src="holder.js/300x200?theme=dark" />
					</BlogThumbnail>
					<BlogTitle>BLOG POST TITLE</BlogTitle>
					<BlogTextWrapper>
						<BlogText>
							Terrastories is a geostorytelling application built to enable
							indigenous and other local communities to locate and map their own
							oral storytelling traditions about places of significant
							meaning...
						</BlogText>
					</BlogTextWrapper>
				</Column>
				<Column
					textAlign="center"
					alignItems="space-between"
					gapLeft="3em"
					gapRight="3em"
				>
					<BlogThumbnail>
						<img alt="placeholder" src="holder.js/300x200?theme=dark" />
					</BlogThumbnail>
					<BlogTitle>BLOG POST TITLE</BlogTitle>
					<BlogTextWrapper>
						<BlogText>
							Terrastories is a geostorytelling application built to enable
							indigenous and other local communities to locate and map their own
							oral storytelling traditions about places of significant
							meaning...
						</BlogText>
					</BlogTextWrapper>
				</Column>
				<Column
					textAlign="center"
					alignItems="space-between"
					gapLeft="3em"
					gapRight="3em"
				>
					<BlogThumbnail>
						<img alt="placeholder" src="holder.js/300x200?theme=dark" />
					</BlogThumbnail>
					<BlogTitle>BLOG POST TITLE</BlogTitle>
					<BlogTextWrapper>
						<BlogText>
							Terrastories is a geostorytelling application built to enable
							indigenous and other local communities to locate and map their own
							oral storytelling traditions about places of significant
							meaning...
						</BlogText>
					</BlogTextWrapper>
				</Column>
			</Row>
		</>
	);
};

export default Blogs;
