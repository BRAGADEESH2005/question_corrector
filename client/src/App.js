import { Routes, Route, BrowserRouter } from "react-router-dom";
import { mainRoutes } from "./routes";
import Layout from "./Layout";

function App() {
	return (
		<>
			<BrowserRouter>
				<Layout>
				<Routes>
					{mainRoutes.map((route, index) => {
						return (
							<Route
								key={index}
								path={route.path}
								Component={route.component}
								exact={route.exact}
							/>
						);
					})}
					{/* TODO:404Page */}
					<Route path="*" element={<div>404Page</div>} />
				</Routes>
				</Layout>
			</BrowserRouter>
		</>
	);
}

export default App;
