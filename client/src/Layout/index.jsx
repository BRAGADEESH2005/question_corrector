import React from "react";

import Navbar from "../Component/Navbar";
import SidePanel from "../Component/SidePanel";
import "./styles.css";

const Layout = ({ children }) => {
	return (
		<div>
			<Navbar />
			<div className="container">
				<SidePanel />
				{children}
			</div>
		</div>
	);
};

export default Layout;
