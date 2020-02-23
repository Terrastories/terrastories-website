import React from "react";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import Landing from "./Landing";
import Team from "./Team";
import About from "./About";
import Navbar from "./Navbar";

function App() {
	return (
		<div className="app">
			<Navbar />
			<BrowserRouter>
				<Switch>
					<Route exact path="/" component={Landing} />
					<Route exact path="/team" component={Team} />
					<Route exact path="/about" component={About} />
				</Switch>
			</BrowserRouter>
		</div>
	);
}

export default App;
