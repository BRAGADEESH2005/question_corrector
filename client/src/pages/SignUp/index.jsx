import React, { useState } from "react";
import "./styles.css";
import { FaGoogle } from "react-icons/fa";
import { FaFacebook } from "react-icons/fa";
import {useNavigate} from "react-router-dom";
// import { Link } from "react-router-dom";

const SignUp = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform validation here
    if (name.trim() === "" || email.trim() === "" || password.trim() === "" || confirmPassword.trim() === "") {
      alert("Please fill in all fields.");
      return;
    }
	if(password!==confirmPassword){
		alert("Passwords do not match");
		return;
	}
    // If all fields are filled, continue
    // You can redirect or perform any other action here
    // For now, just logging the form data
	// TODO:Backend Integration
    console.log("Form submitted:", { name, email, password, confirmPassword });
	navigate("/profileDetails");
	
  };

  return (
    <div className="signup">
      <form className="signup-container" onSubmit={handleSubmit}>
        <h3 className="signup-title">Sign Up</h3>
        <input
          className="signup-input"
          type="text"
          id="name"
          placeholder="Name*"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
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
