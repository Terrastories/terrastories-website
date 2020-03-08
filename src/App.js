import React from "react";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import Landing from "./Landing";
import Gallery from "./Gallery";
import About from "./About";
import GetInvolved from "./GetInvolved";
import Download from "./Download";
import PageLayout from "./PageLayout";

function App() {
	return (
		<div className="app">
			<PageLayout>
				<BrowserRouter>
					<Switch>
						<Route exact path="/" component={Landing} />
						<Route exact path="/about" component={About} />
						<Route exact path="/get-involved" component={GetInvolved} />
						<Route exact path="/gallery" component={Gallery} />
						<Route exact path="/download" component={Download} />
					</Switch>
				</BrowserRouter>
			</PageLayout>
		</div>
	);
}

export default App;
