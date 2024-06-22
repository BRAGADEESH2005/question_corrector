import React, { useState } from "react";
import { Document, Page } from "react-pdf";
import "./styles.css";
const PdfViewer = ({ pdfUrl }) => {
	const [numPages, setNumPages] = useState(null);
	const [pageNumber, setPageNumber] = useState(1);

	const onDocumentLoadSuccess = ({ numPages }) => {
		setNumPages(numPages);
	};

	return (
		<div className="view-pdf">
		<h1>Question Paper</h1>
		<div className="pdf-container">
			
			<div className="pdf-holder">
				<div className="pdf-scrollable">
					<Document
						file={pdfUrl}
						className="pdf-actual"
						onLoadSuccess={onDocumentLoadSuccess}
					>
						{Array.apply(null, Array(numPages))
							.map((x, i) => i + 1)
							.map((page) => {
								return (
									<Page
										key={page}
										pageNumber={page}
										renderTextLayer={false}
										renderAnnotationLayer={false}
										// className={"pdf-page"}
									/>
								);
							})}
					</Document>
				</div>
			</div>
		</div>
		</div>
	);
};

export default PdfViewer;
