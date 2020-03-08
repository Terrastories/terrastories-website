import styled from "styled-components";

export const ButtonSolid = styled.button`
	display: block;
	margin-right: auto;
	margin-left: auto;
	padding: 0.5em;
	background-color: #d97b29;
	border: #d97b29 3px solid;
	-webkit-transition: background-color 400ms ease;
	transition: background-color 400ms ease;
	font-family: Open Sans, sans-serif;
	font-size: 20px;
	line-height: 24px;
	font-weight: 400;
	text-align: center;
	color: white;
	margin: 2em;
	font-family: "Oswald";
	max-width: 250px;

	:hover {
		background-color: #dea826;
		border-color: #dea826;
		color: white;
	}
`;

export const ButtonOutline = styled.button`
	display: block;
	margin-right: auto;
	margin-left: auto;
	padding: 0.5em;
	background-color: transparent;
	-webkit-transition: background-color 400ms ease;
	transition: background-color 400ms ease;
	font-family: Open Sans, sans-serif;
	font-size: 20px;
	line-height: 24px;
	font-weight: 400;
	text-align: center;
	border: white 3px solid;
	color: white;
	margin: 2em;
	font-family: "Oswald";
	max-width: 250px;
	:hover {
		background: white;
		color: #09697e;
	}
`;
