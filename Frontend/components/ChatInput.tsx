"use client";

import { useState } from "react";

type Props = {
  onSend: (message: string) => void;
};

export default function ChatInput({ onSend }: Props) {
  const [input, setInput] = useState("");

  const handleSubmit = () => {
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") handleSubmit();
  };

  return (
    <div className="w-full flex justify-center absolute bottom-6 left-0">
      
      <div className="glass-input relative flex items-center w-[60%] px-4 py-2">

        {/* INPUT */}
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask anything..."
          className="flex-1 bg-transparent outline-none text-black text-bold placeholder-gray-500 text-[17px]"
        />

        {/* SEND BUTTON */}
        <button
          onClick={handleSubmit}
          className="send-btn ml-3"
        >
          ➤
        </button>

        {/* bottom reflection */}
        <div className="input-reflection"></div>
      </div>

    </div>
  );
}