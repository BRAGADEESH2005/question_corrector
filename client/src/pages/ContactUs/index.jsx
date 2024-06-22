import React, { useState } from 'react';
import './styles.css';

const ContactUs = () => {
  const [feedback, setFeedback] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send feedback or query logic here
    console.log('Feedback or query submitted:', feedback);
    // You can integrate feedback submission functionality here using libraries or send a POST request to a backend service
    // Remember to reset the feedback state after submission if needed
    setFeedback('');
  };

  return (
    <div className="contact-us-container">
      <h2>Contact Us</h2>
      <form onSubmit={handleSubmit} className="contact-form">
        <textarea
          placeholder="Your feedback or query..."
          value={feedback}
          onChange={(e) => setFeedback(e.target.value)}
          className="feedback-input"
          required
        />
        <button type="submit" className="submit-button">Submit</button>
      </form>
    </div>
  );
};

export default ContactUs;
