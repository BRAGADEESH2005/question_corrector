import React, { useState } from "react";
import { Link } from "react-router-dom";
import psglogo from "../../assets/psglogo.jfif";
import { RxHamburgerMenu } from "react-icons/rx";
import { IoCloseOutline } from "react-icons/io5";
import "./styles.css";
import SidePanel from "../SidePanel";

const Navbar = () => {
	const [toggle, setToggle] = useState(false);
	const handleToggle = () => {
		setToggle(!toggle);
	};

	return (
		<nav>
			<div className="desktop-nav">
				<Link className="navbar-brand anchor" to="/">
					{/* TODO:change Logo */}
					<img src={psglogo} alt="psglogo" className="navbar-logo" />
					Question Corrector
				</Link>
				<div className="right-container">
					<Link className="premium-btn anchor" to="/">
						{/* TODO:Profile name */}
						Upgrade to Premium
						{/* Welcome Name!! */}
					</Link>
					{/* TODO:Profile Logo */}
					<img src={psglogo} alt="psglogo" className="profile-logo" />
				</div>

				{/* Mobile Navigation */}
				<div className="mobile-nav">
					{toggle ? (
						<IoCloseOutline className="hamburger" onClick={handleToggle} />
					) : (
						<RxHamburgerMenu className="hamburger" onClick={handleToggle} />
					)}
					{toggle && (
						<div className="mobile-nav-links">
							<Link className="mobile-link anchor" to="/">
								Dashboard
							</Link>
							<Link className="mobile-link anchor" to="/">
								Question Paper
							</Link>
							<Link className="mobile-link anchor" to="/about">
								Account Settings
							</Link>
							<Link className="mobile-link anchor" to="/contact">
								Contact Us
							</Link>
							<Link className="mobile-link anchor" to="/contact">
								Logout
							</Link>
						</div>
					)}
				</div>
			</div>
			<SidePanel />
		</nav>
	);
};

export default Navbar;
