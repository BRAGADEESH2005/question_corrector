import React, { useState } from "react";
import PdfViewer from "../../Component/PdfViewer"; // Adjust the path as per your project structure
import { pdfjs } from "react-pdf";
import pdf from "./abstract.pdf"; // Provide the path of your PDF here
import "./styles.css";

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
	"pdfjs-dist/build/pdf.worker.min.js",
	import.meta.url
).toString();

const AnswerUpload = () => {
	const [dragging, setDragging] = useState(false);
	const [files, setFiles] = useState([]);

	const handleDragOver = (e) => {
		e.preventDefault();
		e.stopPropagation();
		setDragging(true);
	};

	const handleDragEnter = (e) => {
		e.preventDefault();
		e.stopPropagation();
		setDragging(true);
	};

	const handleDragLeave = (e) => {
		e.preventDefault();
		e.stopPropagation();
		setDragging(false);
	};

	const handleDrop = (e) => {
		e.preventDefault();
		e.stopPropagation();
		setDragging(false);

		const droppedFiles = Array.from(e.dataTransfer.files);
		setFiles(droppedFiles);
	};

	const handleFileInputChange = (e) => {
		const selectedFiles = Array.from(e.target.files);
		setFiles(selectedFiles);
	};

	const handleUpload = () => {
		// Handle file upload here
		console.log("Files to upload:", files);
		// Reset the files state after upload
		setFiles([]);
	};

	return (
		<div className="upload-answer-holder">
			<div className="upload-pdf-container">
				<PdfViewer pdfUrl={pdf} />
			</div>
			<div
				className={`upload-container ${dragging ? "dragging" : ""}`}
				onDragOver={handleDragOver}
				onDragEnter={handleDragEnter}
				onDragLeave={handleDragLeave}
				onDrop={handleDrop}
			>
				<h1>Upload Answer</h1>
				<div className="drop-zone">
					{files.length === 0 ? (
						<>
							<p>Drag & drop your file here</p>
							<p>or</p>
						</>
					) : (
						<p>{files.length} file(s) selected</p>
					)}
					<input
						type="file"
						accept="application/pdf"
						onChange={handleFileInputChange}
						style={{ display: "none" }}
					/>
					<button  className="answer-upload-btn" onClick={() => document.querySelector('input[type="file"]').click()}>Choose File</button>
				</div>
				<button className="answer-upload-btn" onClick={handleUpload}>Upload</button>
			</div>
		</div>
	);
};

export default AnswerUpload;
