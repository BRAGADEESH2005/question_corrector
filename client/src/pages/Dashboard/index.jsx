import React from "react";
import "./styles.css";

const Dashboard = () => {
	return (
		<div className="dashboard-container">
			<div className="left-dashboard">
				<div className="user-intro">
					<p>Hello user.name</p>
					<p>Board:user.board</p>
					<p>Class:user.class</p>
					<button>Edit Profile</button>
				</div>
				<div className="mentor">
					<p>Mentor:user.mentor</p>
				</div>
				<div className="solved-papers">
					<h4>Recently Solved Papers</h4>
					<div>
						<li className="dashboard-papers">
							<p>QP1</p>
							<p>Score</p>
							<p>Subject</p>
						</li>
						<li className="dashboard-papers">
							<p>QP1</p>
							<p>Score</p>
							<p>Subject</p>
						</li>
						<li className="dashboard-papers">
							<p>QP1</p>
							<p>Score</p>
							<p>Subject</p>
						</li>
						<li className="dashboard-papers">
							<p>QP1</p>
							<p>Score</p>
							<p>Subject</p>
						</li>
					</div>
				</div>
			</div>

			<div className="right-dashboard">
				<div className="dashboard-analysis">
					<div className="analysis">
						<p>QP's Solved</p>
						<p>11</p>
					</div>
					<div className="analysis">
						<p>Average Score</p>
						<p>99</p>
					</div>
				</div>
				<div className="dashboard-performance">
					<ul>
						<li>Easy -- Score</li>
						<li>Medium -- Score</li>
						<li>Hard -- Score</li>
					</ul>
				</div>
				<div className="dashboard-contact">
					<h4>Contact Details</h4>
					<p>Email:user.email</p>
					<p>Phone:user.phone</p>
				</div>
			</div>
		</div>
	);
};

export default Dashboard;
