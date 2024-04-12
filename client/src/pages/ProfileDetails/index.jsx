import React, { useState } from "react";
import {useParams,useNavigate} from "react-router-dom";
import "../SignUp/styles.css";

const ProfileDetails = () => {
	const [firstName, setFirstName] = useState("");
	const [lastName, setLastName] = useState("");
	const [age, setAge] = useState("");
	const [board, setBoard] = useState("");
	const [classLevel, setClassLevel] = useState("");
	const [phoneNumber, setPhoneNumber] = useState("");

	const boardOptions = ["CBSE", "ICSE", "State Board"];
	const classOptions = ["10th", "11th", "12th"];
	const {category} = useParams();
	const navigate = useNavigate();

	const handleSubmit = (event) => {
		event.preventDefault();
		// Here you can handle the form submission, for now let's just log the form data
		if (board === "" || classLevel === "") {
			alert("Please select board and class");
			return;
		}
		console.log({
			firstName,
			lastName,
			age,
			board,
			classLevel,
			phoneNumber,
		});
		navigate("/dashboard");
	};

	return (
		<div className="signup">
			<form className="signup-container" onSubmit={handleSubmit}>
				<h3 className="signup-title">{category}-Profile Details</h3>
				<input
					className="signup-input"
					type="text"
					placeholder="First Name"
					value={firstName}
					onChange={(e) => setFirstName(e.target.value)}
					required
				/>
				<input
					className="signup-input"
					type="text"
					placeholder="Last Name"
					value={lastName}
					onChange={(e) => setLastName(e.target.value)}
					required
				/>
				<input
					className="signup-input"
					type="number"
					placeholder="Age"
					value={age}
					onChange={(e) => setAge(e.target.value)}
					required
				/>
				<input
					className="signup-input"
					type="tel"
					placeholder="Phone Number"
					value={phoneNumber}
					onChange={(e) => setPhoneNumber(e.target.value)}
					required
				/>
				<select
					className="signup-input"
					value={board}
					onChange={(e) => setBoard(e.target.value)}
				>
					<option className="signup-input" value="">
						Select Board
					</option>
					{boardOptions.map((option) => (
						<option className="signup-input" key={option} value={option}>
							{option}
						</option>
					))}
				</select>
				<select
					className="signup-input"
					value={classLevel}
					onChange={(e) => setClassLevel(e.target.value)}
				>
					<option className="signup-input" value="">
						Select Class
					</option>
					{classOptions.map((option) => (
						<option className="signup-input" key={option} value={option}>
							{option}
						</option>
					))}
				</select>

				<button className="btn" type="submit">
					Submit
				</button>
			</form>
		</div>
	);
};

export default ProfileDetails;
