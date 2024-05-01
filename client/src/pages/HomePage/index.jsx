import React from "react";
import { Link } from "react-router-dom";
import "./styles.css"; // Import your custom styles

const HomePage = () => {
    return (
        <div className="homepage-container">
            <div className="homepage-content">
                <h1>Welcome to QuestionCorrector</h1>
                <p>Empowering students to upload answers and teachers to provide corrections</p>
                <Link to='/signup' className="get-started-btn">Get Started</Link>
            </div>
        </div>
    );
};

export default HomePage;
