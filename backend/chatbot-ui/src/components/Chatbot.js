import React, { useState } from 'react';

const Chatbot = ({ setVideoState }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

const handleSendMessage = () => {
  if (input.trim() === '') return;

  setMessages((prev) => [...prev, { text: input, isUser: true }]);

  setVideoState('typing');

  setTimeout(() => {
    setVideoState('reading');  // smoother transition
  }, 4000);

  setTimeout(() => {
    setMessages((prev) => [
      ...prev,
      { text: "Here's the response based on your question", isUser: false }
    ]);

    setVideoState('idle');
  }, 4000);

  setInput('');
};

  return (
    <div className="chatbot-container">
      <div className="chat-header">
         College Assistant
      </div>

      <div className="messages">
        {messages.map((msg, i) => (
          <div key={i} className={msg.isUser ? 'user-message' : 'bot-message'}>
            {msg.text}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          id="user-input"
          type="text"
          value={input}
          onChange={(e) => {
            setInput(e.target.value);
            setVideoState('typing'); // 🔥 typing state
          }}
          placeholder="Type your question..."
        />

        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;