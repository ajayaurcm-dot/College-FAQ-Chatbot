"use client";

import { useState, useEffect, useRef } from "react";

type Props = {
  volume: number;
  setVolume: (v: number) => void;
};

export default function SpeakerControl({ volume, setVolume }: Props) {
  const [showControls, setShowControls] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // 🔥 Close when clicking outside
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (
        containerRef.current &&
        !containerRef.current.contains(e.target as Node)
      ) {
        setShowControls(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () =>
      document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div ref={containerRef} className="fixed inset-0 z-30 pointer-events-none">

      {/* 🔊 INVISIBLE SPEAKER HITBOX (ADJUST POSITION HERE) */}
      <div
        onClick={() => setShowControls((prev) => !prev)}
        className="absolute bottom-[16%] left-[37%] w-24 h-24  cursor-pointer pointer-events-auto"
      />

      {/* 🎚️ VOLUME TOGGLE PANEL */}
      {showControls && (
        <div
          className="absolute bottom-[1%] left-[41%] -translate-x-1/2 
          bg-black/70 backdrop-blur-md 
          px-5 py-4 rounded-2xl 
          border border-white/10 
          shadow-[0_10px_40px_rgba(0,0,0,0.8)]
          animate-fadeIn
          pointer-events-auto"
        >
          {/* Label */}
          <div className="text-xs text-gray-300 mb-3 text-center tracking-wide">
            Volume
          </div>

          {/* Slider */}
          <input
            type="range"
            min="0"
            max="100"
            value={volume * 100}
            onChange={(e) => setVolume(Number(e.target.value) / 100)}
            className="w-36 accent-green-400 cursor-pointer"
          />
        </div>
      )}
    </div>
  );
}