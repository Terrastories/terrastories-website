import React from "react";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import Landing from "./Landing";
import Gallery from "./Gallery";
import About from "./About";
import Navbar from "./Navbar";
import GetInvolved from "./GetInvolved";
import GetStarted from "./GetStarted";

function App() {
	return (
		<div className="app">
			<Navbar />
			<BrowserRouter>
				<Switch>
					<Route exact path="/" component={Landing} />
					<Route exact path="/about" component={About} />
					<Route exact path="/get-involved" component={GetInvolved} />
					<Route exact path="/gallery" component={Gallery} />
					<Route exact path="/download" component={GetStarted} />
				</Switch>
			</BrowserRouter>
		</div>
	);
}

export default App;
