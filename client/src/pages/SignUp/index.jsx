import React, { useState } from "react";
import "./styles.css";
import { FaGoogle } from "react-icons/fa";
import { FaFacebook } from "react-icons/fa";
import { useNavigate } from "react-router-dom";

const SignUp = () => {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [category, setCategory] = useState("");
	const navigate = useNavigate();

	const categoryOptions = ["Student", "Mentor", "Evaluator"];

	const handleSubmit = (e) => {
		e.preventDefault();
		// Perform validation here
		if (
			email.trim() === "" ||
			password.trim() === "" ||
			confirmPassword.trim() === "" ||
			category.trim() === ""
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
		// For now, just logging the form data and selected category
		// TODO: Backend Integration
		console.log("Form submitted:", { email, password, category });
		navigate(`/profileDetails/${category}`);
	};

	return (
		<div className="signup">
			<form className="signup-container" onSubmit={handleSubmit}>
				<h3 className="signup-title">Sign Up</h3>
        <hr className="row" />
				<div className="category-header">Choose Your Role</div>
				<div className="category-options">
					{categoryOptions.map((option) => (
						<label key={option} className="category-label">
							<input
								type="radio"
								value={option}
								checked={category === option}
								onChange={(e) => setCategory(e.target.value)}
								required
							/>
							{option}
						</label>
					))}
				</div>
          <hr className="row" />
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
		</div>
	);
};

export default SignUp;
