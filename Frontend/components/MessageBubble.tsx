"use client";
import MessageRenderer from "./MessageRenderer";

type Props = {
  role: "user" | "bot";
  text: string;
  time?: string;
};

export default function MessageBubble({ role, text, time }: Props) {
  const isUser = role === "user";

  return (
    <div className={`w-full flex ${isUser ? "justify-end pr-5 pt-6" : "justify-start pl-5"} mb-6`}>
      <div
        className={`
          glass-bubble
          ${isUser ? "user-bubble" : "bot-bubble"}
          max-w-[70%]
        `}
      >
        <div
  className="
  relative z-10
    text-[15px]
    font-medium
    leading-relaxed
    whitespace-pre-wrap
    text-black
    brightness-100
    drop-shadow-[0_1px_2px_rgba(255,255,255,0.4)]
  "
>
          <MessageRenderer text={text} />
        </div>

        {time && (
          <div className="text-[11px] mt-2 text-right opacity-60">
            {time}
          </div>
        )}

        {/* IMPORTANT: bottom reflection */}
        <div className="bottom-reflection"></div>
      </div>
    </div>
  );
}