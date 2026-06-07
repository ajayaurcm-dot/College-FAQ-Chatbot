"use client";

import { useEffect, useRef, useState } from "react";
import sendMessage from "@/lib/api";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

type Message = {
  role: "user" | "bot";
  text: string;
};

type Props = {
  messages: Message[];
  setMessages: (msgs: Message[]) => void;
};

export default function ChatUI({ messages, setMessages }: Props) {
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  const handleSend = async (text: string) => {
    if (!text.trim()) return;

    const updated = [...messages, { role: "user", text }];
    setMessages(updated);
    setLoading(true);

    try {
      const reply = await sendMessage(text);

      setMessages([
        ...updated,
        { role: "bot", text: reply }
      ]);
    } catch {
      setMessages([
        ...updated,
        { role: "bot", text: "Error getting response." }
      ]);
    }

    setLoading(false);
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="relative h-full w-full overflow-hidden">

      {/* CHAT AREA */}
      <div className="
        absolute inset-0
        overflow-y-auto
        px-6 pt-6 pb-32
        space-y-4
        custom-scroll
       
      "
       style={{ scrollbarWidth: "thin" }}>
        {messages.map((msg, i) => (
          <MessageBubble key={i} role={msg.role} text={msg.text} />
        ))}

        {loading && (
          <MessageBubble role="bot" text="Typing..." />
        )}

        <div ref={chatEndRef} />
      </div>

      {/* 🔥 GLASS FADE MASK (IMPORTANT) */}
      <div className="
        pointer-events-none
        absolute bottom-12 left-39 w-90 h-8
        z-20 rounded-[33px] 
        bg-gradient-to-t 
        
        transparent 45%
        backdrop-blur-xl
      " />

      {/* INPUT (TOP LAYER) */}
      <div className="
        absolute bottom-3 left-1/2 -translate-x-1/2
        w-[92%] max-w-3xl
        z-30
      ">
        <ChatInput onSend={handleSend} />
      </div>

    </div>
  );
}