import React from "react";
import styled from "styled-components";
import Navbar from "./Navbar";
import Footer from "./Footer";

const Page = styled.div`
	overflow-x: hidden;
	overflow-y: hidden;
`;

const PageContent = styled.div`
	min-height: 500px;
`;

const PageLayout = props => {
	return (
		<>
			<Page>
				<Navbar />
				<PageContent>{props.children}</PageContent>
				<Footer />
			</Page>
		</>
	);
};

export default PageLayout;
