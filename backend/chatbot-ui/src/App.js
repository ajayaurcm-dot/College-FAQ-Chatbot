import React, { useState } from 'react';
import Background from './components/Background';
import Chatbot from './components/Chatbot';
import './App.css';

function App() {
  const [videoState, setVideoState] = useState('idle');

  return (
    <div className="app-container">
      <Background videoState={videoState} />
      <Chatbot setVideoState={setVideoState} />
    </div>
  );
}

export default App;