import React, { useState } from "react";
import "./styles.css";
import { FaGoogle } from "react-icons/fa";
import { FaFacebook } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
// import { Link } from "react-router-dom";

const SignUp = () => {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [openPopup, setOpenPopup] = useState(false);
	const [category, setCategory] = useState("");
	const navigate = useNavigate();

	const categoryOptions = ["Student", "Mentor", "Evaluator"];

	const handleSubmit = (e) => {
		e.preventDefault();
		// Perform validation here
		if (
			email.trim() === "" ||
			password.trim() === "" ||
			confirmPassword.trim() === ""
		) {
			alert("Please fill in all fields.");
			return;
		}
		if (password !== confirmPassword) {
			alert("Passwords do not match");
			return;
		}
		// If all fields are filled, continue
		// You can redirect or perform any other action here
		// For now, just logging the form data
		// TODO:Backend Integration
		console.log("Form submitted:", { email, password });
		setOpenPopup(true);
	};

	const handlePopUpSubmit = () => {
		if (category === "") {
			alert("Please select a category");
			return;
		}
		if (category === "Student") {
			navigate("/profileDetails/Student");
		} else if (category === "Mentor") {
			navigate("/profileDetails/Mentor");
		} else if(category === "Evaluator") {
			navigate("/profileDetails/Evaluator");
		}
		console.log("Category selected:", category);
	};

	return (
		<div className="signup">
			<form className="signup-container" onSubmit={handleSubmit}>
				<h3 className="signup-title">Sign Up</h3>
				<input
					className="signup-input"
					type="email"
					id="email"
					placeholder="Email*"
					value={email}
					onChange={(e) => setEmail(e.target.value)}
					required
				/>
				<input
					className="signup-input"
					type="password"
					id="password"
					placeholder="Password*"
					value={password}
					onChange={(e) => setPassword(e.target.value)}
					required
				/>
				<input
					className="signup-input"
					type="password"
					id="confirmPassword"
					placeholder="Confirm Password*"
					value={confirmPassword}
					onChange={(e) => setConfirmPassword(e.target.value)}
					required
				/>
				<button type="submit" className="btn">
					Continue
				</button>
				<p className="ordesign">Or</p>
				<button className="btn">
					<FaGoogle className="signup-icon" />
					Continue with Google
				</button>
				<button className="btn">
					<FaFacebook className="signup-icon" />
					Continue with Facebook
				</button>
			</form>
			{openPopup && (
				<div className="popup">
					<h2 className="signup-title">Choose Your Roll</h2>
					<select
						className="select-input"
						value={category}
						onChange={(e) => setCategory(e.target.value)}
					>
						<option className="select-input" value="">
							Select Class
						</option>
						{categoryOptions.map((option) => (
							<option className="select-input" key={option} value={option}>
								{option}
							</option>
						))}
					</select>
					<button className="btn" onClick={() => setOpenPopup(false)}>
						Close
					</button>
					<button onClick={handlePopUpSubmit} className="btn">Submit</button>
				</div>
			)}
		</div>
	);
};

export default SignUp;
