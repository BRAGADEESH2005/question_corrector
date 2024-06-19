import React from "react";
import psglogo from "../../assets/psglogo.jfif";
import "./styles.css";
import { useState } from "react";

const QuestionPaper = () => {
	const [searchTerm, setSearchTerm] = useState("");
	const [filters, setFilters] = useState({
		board: "",
		difficulty: "",
	});
	const details = [
		{
			img: psglogo,
			subHeader: "Top Questions",
			content: "Start your day with the best questions",
		},
		{
			img: psglogo,
			subHeader: "Suggested Questions",
			content: "Questions suggested by mentors",
		},
		{
			img: psglogo,
			subHeader: "Liked Questions",
			content: "Questions you liked",
		},
		{
			img: psglogo,
			subHeader: "Answered Questions",
			content: "Questions you have answered",
		},
	];

	const questionPapers = [
		{
			qp_name: "QP1",
			qp_link: "http://localhost:3000/answerUpload",
			qp_board: "CBSE",
			qp_difficulty: "Easy",
			qp_acceptance: "25.5%",
			qp_subject: "Maths",
		},
		{
			qp_name: "QP2",
			qp_link: "http://localhost:3000/answerUpload",
			qp_board: "CBSE",
			qp_difficulty: "Easy",
			qp_acceptance: "25.5%",
			qp_subject: "Science",
		},
		{
			qp_name: "QP3",
			qp_link: "http://localhost:3000/answerUpload",
			qp_board: "CBSE",
			qp_difficulty: "Easy",
			qp_acceptance: "25.5%",
			qp_subject: "Maths",
		},
		{
			qp_name: "QP4",
			qp_link: "http://localhost:3000/answerUpload",
			qp_board: "CBSE",
			qp_difficulty: "Easy",
			qp_acceptance: "25.5%",
			qp_subject: "Science",
		},
		{
			qp_name: "QP5",
			qp_link: "http://localhost:3000/answerUpload",
			qp_board: "CBSE",
			qp_difficulty: "Easy",
			qp_acceptance: "25.5%",
			qp_subject: "Maths",
		},
		{
			qp_name: "QP6",
			qp_link: "http://localhost:3000/answerUpload",
			qp_board: "CBSE",
			qp_difficulty: "Easy",
			qp_acceptance: "25.5%",
			qp_subject: "Science",
		},
	];

	return (
		<div className="qp-page">
			<h2>Study Plan</h2>
			<div className="qp-top">
				<div className="study-plan">
					{details.map((detail, index) => (
						<div key={index} className="study-plan-card">
							<img className="plan-image" src={detail.img} alt="psglogo" />
							<div className="plan-content-holder">
								<h3 className="plan-content-title">{detail.subHeader}</h3>
								<p className="plan-content-para">{detail.content}</p>
							</div>
						</div>
					))}
				</div>
			</div>
			<div class="qp-bottom">
				<h2>Question Paper</h2>
				<div className="filter-section">
					<select
						className="filter-select"
						value={filters.board}
						onChange={(e) => setFilters({ ...filters, board: e.target.value })}
					>
						<option value="">Select Board</option>
						<option value="CBSE">CBSE</option>
						<option value="ICSE">ICSE</option>
						<option value="StateBoard">State Board</option>
						{/* Add options for different boards */}
					</select>
					<select
						className="filter-select"
						value={filters.difficulty}
						onChange={(e) =>
							setFilters({ ...filters, difficulty: e.target.value })
						}
					>
						<option value="">Select Difficulty</option>
						<option value="Easy">Easy</option>
						<option value="Medium">Medium</option>
						<option value="Hard">Hard</option>
						{/* Add options for different difficulties */}
					</select>
					<select
						className="filter-select"
						value={filters.difficulty}
						onChange={(e) =>
							setFilters({ ...filters, difficulty: e.target.value })
						}
					>
						<option value="">Subject</option>
						<option value="Maths">Maths</option>
						<option value="Science">Science</option>
						<option value="English">English</option>
						<option value="Social">Social</option>
					</select>
					<input
						type="text"
						placeholder="Search by name..."
						value={searchTerm}
						onChange={(e) => setSearchTerm(e.target.value)}
						className="filter-search"
					/>
				</div>
				<div class="table-responsive">
					<table class="qp-table">
						<thead>
							<tr>
								<th>Name</th>
								<th>Link</th>
								<th>Subject</th>
								<th>Board</th>
								<th>Difficulty</th>
								<th>Acceptance</th>
							</tr>
						</thead>
						<tbody>
							{questionPapers.map((questionPaper, index) => (
								<tr key={index} >
									<td>{questionPaper.qp_name}</td>
									<td>
										<a class="plan-link" href={questionPaper.qp_link}>
											QP_Link
										</a>
									</td>
									<td>{questionPaper.qp_subject}</td>
									<td>{questionPaper.qp_board}</td>
									<td>{questionPaper.qp_difficulty}</td>
									<td>{questionPaper.qp_acceptance}</td>
								</tr>
							))}
						</tbody>
					</table>
				</div>
			</div>
		</div>
	);
};

export default QuestionPaper;
