import React from "react";
import { Link } from "react-router-dom";
import "./styles.css";
import { MdDashboard } from "react-icons/md";
import { MdQuestionAnswer } from "react-icons/md";
import { IoMdCloudUpload } from "react-icons/io";
import { FaHandsHelping } from "react-icons/fa";
import { IoMdMail } from "react-icons/io";
import { FaUsers } from "react-icons/fa";
import { FaBookOpen } from "react-icons/fa";
const SidePanel = () => {
	return (
		<div className="side-panel">
			<div className="top-panel">
				<Link className="side-anchor" to={"/dashboard"}>
					<MdDashboard className="icon" /> Dashboard
				</Link>
				<Link className="side-anchor" to="/questionPaper">
					<MdQuestionAnswer className="icon" /> Question Paper
				</Link>
				<Link className="side-anchor" to={"/answerUpload"}>
					<IoMdCloudUpload className="icon" /> Upload Answer
				</Link>
				<Link className="side-anchor">
					<FaBookOpen className="icon" />
					Guidelines
				</Link>
			</div>
			<div className="bottom-panel">
				<Link className="side-anchor">
					<FaHandsHelping className="icon" />
					Help Center
				</Link>
				<Link className="side-anchor">
					<IoMdMail className="icon" />
					Contact Us
				</Link>
				<Link className="side-anchor">
					<FaUsers className="icon" />
					About Us
				</Link>
			</div>
		</div>
	);
};

export default SidePanel;
