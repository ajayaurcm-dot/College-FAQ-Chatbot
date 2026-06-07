// src/App.js

import React from 'react';
import Chatbot from '../../chatbot-ui/src/components/Chatbot';
import Background from '../../chatbot-ui/src/components/Background';
import './App.css'; // Import the CSS styles

function App() {
  return (
    <div className="app-container">
      <Background />
      <Chatbot />
    </div>
  );
}

export default App;