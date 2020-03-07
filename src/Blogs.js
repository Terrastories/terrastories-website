import React from "react";
import { Column, Row } from "./styled-components/layout";
import styled from "styled-components";
import Holder from "holderjs";

Holder.addTheme("dark", {
	//bg: "#33AA8B"
	bg: "gainsboro"
});

const BlogTitle = styled.h1``;

const BlogText = styled.p``;

const BlogThumbnail = styled.div``;

const Blogs = () => {
	return (
		<>
			<Row
				gapTop="5em"
				gapBottom="5em"
				justifyContent="center"
				className="blogs"
				width="100%"
			>
				<Column
					textAlign="center"
					alignItems="space-between"
					gapLeft="3em"
					gapRight="3em"
				>
					<BlogThumbnail>
						<img src="holder.js/300x200?theme=dark" />
					</BlogThumbnail>
					<BlogTitle>Blog Title</BlogTitle>
					<BlogText>This is text</BlogText>
				</Column>
				<Column
					textAlign="center"
					alignItems="space-between"
					gapLeft="3em"
					gapRight="3em"
				>
					<BlogThumbnail>
						<img src="holder.js/300x200?theme=dark" />
					</BlogThumbnail>
					<BlogTitle>Blog Title</BlogTitle>
					<BlogText>This is text</BlogText>
				</Column>
				<Column
					textAlign="center"
					alignItems="space-between"
					gapLeft="3em"
					gapRight="3em"
				>
					<BlogThumbnail>
						<img src="holder.js/300x200?theme=dark" />
					</BlogThumbnail>
					<BlogTitle>Blog Title</BlogTitle>
					<BlogText>This is text</BlogText>
				</Column>
			</Row>
		</>
	);
};

export default Blogs;
