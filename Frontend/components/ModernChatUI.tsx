"use client";
import MessageRenderer from "@/components/MessageRenderer";
import Image from "next/image";

import { useState, useRef, useEffect } from "react";
import sendMessage from "@/lib/api"; // ✅ YOUR BACKEND

type Message = {
  role: "user" | "bot";
  text: string;
};

export default function ModernChatUI({
  messages,
  setMessages,
}: {
  messages: Message[];
  setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
}) {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  // ✅ SEND MESSAGE (CONNECTED TO BACKEND)
  const send = async () => {
    if (!input.trim()) return;

    const updated = [...messages, { role: "user", text: input }];
    setMessages(updated);
    setInput("");
    setLoading(true);

    try {
      const reply = await sendMessage(input);

      setMessages([
        ...updated,
        { role: "bot", text: reply },
      ]);
    } catch {
      setMessages([
        ...updated,
        { role: "bot", text: "Error getting response." },
      ]);
    }

    setLoading(false);
  };

  // ✅ ENTER KEY WORKING
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") send();
  };

  // ✅ AUTO SCROLL
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="w-full h-full flex items-center justify-center bg-white">

      {/* MAIN CARD */}
      <div className="
        w-[70%] h-[95%]
        rounded-[40px]
        bg-gradient-to-br from-purple-500 to-pink-400
        border-2 border-white
        shadow-[0px_0px_30px_rgba(0,0,0,.6)]
        flex flex-col
        overflow-hidden
        backdrop-blur-xl
        
      ">

{/* HEADER */}
<div className="
  absolute top-0 left-0 w-full
  flex items-center justify-between
  px-8 py-4
  bg-black backdrop-blur-md
  rounded-t-[40px]
  z-20
">

  {/* LEFT TITLE */}
   {/* LEFT SIDE (LOGO + TEXT IMAGE) */}
  <div className="flex items-center gap-3 ml-2">

    {/* 🎓 ANNA UNIVERSITY LOGO */}
    <Image
      src="/anna-logo1.png"
      alt="Anna University"
      width={55}
      height={55}
      className="object-contain"
    />

    {/* ✨ SMART ASSIST IMAGE TEXT */}
    <Image
      src="/smartassist-text1.png"
      alt="Smart Assist"
      width={300}
      height={40}
      className="object-contain translate-x-[210px]"
    />

  </div>

  {/* RIGHT STATUS */}
  <div className="flex items-center gap-2 mr-5">
    
    {/* 🔥 GLOW DOT */}
    <div className="
  w-1 h-1 rounded-full
  
  bg-green-400
  animate-pulse
  shadow-[0_0_15px_rgba(0,255,150,1),0_0_30px_rgba(0,255,150,0.8)]
" />

    <span className="text-green-400 text-sm">
      Online
    </span>
  </div>
</div>
      

        {/* CHAT AREA */}

        {/* CHAT AREA */}
<div className="flex-1 overflow-hidden rounded-[40px]">
  
  <div
    className="
      h-full overflow-y-auto
      px-6 pt-24 pb-28 space-y-3
      custom-scrol
    "
    style={{ scrollPaddingBottom: "120px" }}
  >

          {messages.map((msg, i) => (
            <div
              key={i}
              className={`flex ${msg.role === "user" ? "justify-end" : "justify-start pl-6"}`}
            >
              <div
  className={`
    max-w-[70%]
    px-5 py-3
    rounded-3xl
    drop-shadow-[0_15px_10px_rgba(0,0,0,0.5)]
    text-xl
    font-[Playfair_Display]
    leading-relaxed
    tracking-wide
                  ${
                    msg.role === "user"
                      ? "bg-yellow-400 text-white"
                      : "bg-white text-black"
                  }
                `}
              >
                <MessageRenderer text={msg.text} />
              </div>
            </div>
          ))}

          {loading && (
  <div className="flex justify-start pl-6">
    <div className="
      px-5 py-3
      rounded-3xl
      bg-white/90
      backdrop-blur-md
      shadow-[0_10px_30px_rgba(0,0,0,0.4)]
      flex items-center gap-2 
    ">
      
      {/* DOT 1 */}
      <span className="typing-dot"></span>

      {/* DOT 2 */}
      <span className="typing-dot delay-150"></span>

      {/* DOT 3 */}
      <span className="typing-dot delay-300"></span>

    </div>
  </div>
)}

          <div ref={chatEndRef} />
        </div>
        </div>

        {/* INPUT */}
        <div className="
  absolute bottom-3 left-1/2 -translate-x-1/2
  w-[90%] z-30
">

          <div className="
  flex items-center gap-3

  bg-white/10
  backdrop-blur-2xl

  rounded-full px-5 py-3

  border border-white/30
  shadow-[0_10px_30px_rgba(0,0,0,0.4)]
">

            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Type a message..."
              className="
                flex-1 bg-transparent
                outline-none
                text-white text-xl
                font-[Playfair_Display]
                placeholder:text-white/60
              "
            />

            <button
              onClick={send}
              className="
                w-9 h-9 flex items-center justify-center
                rounded-full
                bg-gradient-to-r from-purple-500 to-pink-400
                shadow-[0_5px_20px_rgba(255,0,200,0.6)]
                text-white
                shadow-lg
                hover:scale-145 transition
              "
            >
              ➤
            </button>

          </div>
        </div>

      </div>
    </div>
  );
}