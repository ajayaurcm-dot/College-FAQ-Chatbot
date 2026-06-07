"use client";
import { useEffect, useState } from "react";

export default function PremiumClock() {
  const [time, setTime] = useState(new Date());
  const [showColon, setShowColon] = useState(true);

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
      setShowColon((prev) => !prev); // blinking effect
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const hours = time.getHours();
  const minutes = time.getMinutes();

  const displayHours = hours % 12 || 12;
  const displayMinutes = minutes.toString().padStart(2, "0");
  const ampm = hours >= 12 ? "PM" : "AM";

  return (
    <div
      className="relative w-[134px] h-[64px] rounded-xl 
      bg-[#0a0a0a]/90 backdrop-blur-md
      border border-white/10 
      shadow-[0_20px_80px_rgba(0,0,0,0.95)]
      overflow-hidden flex items-center justify-center"
    >

      {/* 🔥 AMBIENT LIGHT REFLECTION (MOVING FEEL) */}
      <div className="absolute inset-0 opacity-10 pointer-events-none">
        <div className="absolute w-[200%] h-full 
       " />
      </div>

      

      

      {/* 🔥 EDGE HIGHLIGHT */}
      <div className="absolute inset-0 rounded-xl 
      ring-1 ring-white/10 " />
      <div className="absolute top-0 left-[-5%] w-[25%] h-full
                bg-gradient-to-r from-transparent via-white/40 to-transparent
                blur-xl
                skew-x-[20deg]
                animate-light-sweep
                pointer-events-none" />

      {/* TIME */}
      <div className="flex items-end gap-2 z-10">

        <span style={{fontFamily:"digital7"}} className="text-[38px] leading-none tracking-wider 
         text-white
        drop-shadow-[0_0_8px_rgba(255,255,255,0.3)] shine opacity-80
        ">
          {displayHours}
          <span className={`mx-1 ${showColon ? "opacity-100" : "opacity-0"} transition`}>
            :
          </span>
          {displayMinutes}
        </span>

        <span className="text-[14px] text-gray-300 mb-2 tracking-wide">
          {ampm}
        </span>

      </div>
    </div>
  );
}