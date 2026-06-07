"use client";

import { useState } from "react";
import { useRef,useEffect } from "react";

export default function SettingsMenu({
  onToggle,
  isFullscreen,
  supportMails,
  newsData
}: {
  onToggle: () => void;
  isFullscreen: boolean;
  supportMails: string[];
  newsData: { title: string }[];
}) {
  const [open, setOpen] = useState(false);
  const [notesIndex, setNotesIndex] = useState(0);
  const [notesOpen, setNotesOpen] = useState(false);
  const [submenu, setSubmenu] = useState<string | null>(null);
  const [activeIndex, setActiveIndex] = useState(0);
  const menuRef = useRef<HTMLDivElement>(null);
  const [currentNews, setCurrentNews] = useState(0);
  const menuItems = [
  "Go to Normal",
  "News",
  "Results",
  "Internal Marks",
  "CGPA",
  "Syllabus",
  "Map",
  "Notes",
  "Schedule",
  "Contact US"
  
  
  ];
  const scheduleFiles = [
  {
    title: "Schedule For Jan-May(2026)",
    file: "Schedule.pdf"
  },
  {
    title: "CSE practical slot",
    file: "CSE & CSE(AI&ML)-2025-26 even sem practical slot.pdf"
  }
];
 
      const notesLinks = [
  {
    title: "Notes 1",
    link: "https://www.poriyaan.in/#google_vignette"
  },
  {
    title: "Notes 2",
    link: "https://www.brainkart.com/menu/anna-university/"
  },
  {
    title: "Notes 3",
    link: "https://padeepz.net/download-anna-university-book-notes-important-questions-and-question-papers-for-2021-regulation/"
  },
  {
    title: "Notes 4",
    link: "https://stucor.in/annauniv-syllabus/anna-university-r2021-ug-pg-syllabus/"
  },
  {
    title: "Notes 5",
    link: "https://www.learnskart.in/syllabus/"
  }
];
  const handleMenuClick = (item: string, index: number) => {
  setActiveIndex(index);

  if (item === "Go to Normal") {
    onToggle();
    setOpen(false);
  }

  if (item === "Results") window.open("https://coe.annauniv.edu/home");
  if (item === "Internal Marks") window.open("https://coe.annauniv.edu/home");
  if (item === "CGPA") window.open("https://m.annauniversitycgpacalc.com/");
  if (item === "Syllabus") window.open("https://cac.annauniv.edu/aidetails/ai_ug_cands_2021ft.html");
  if (item === "Map") window.open("https://www.google.com/maps/place/Anna+University+Regional+Campus,Madurai/@9.9024237,78.0402989,3a,90y,227.95h,80.22t/data=!3m10!1e1!3m8!1s_2oR5vDDXYsrqDLR0nc3JA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D9.777310435753336%26panoid%3D_2oR5vDDXYsrqDLR0nc3JA%26yaw%3D227.9457540431491!7i16384!8i8192!9m2!1b1!2i26!4m11!1m2!2m1!1sanna+university!3m7!1s0x3b00c5c6d2daaaad:0xb7bd44af1de632a6!8m2!3d9.9020481!4d78.03987!10e5!15sCg9hbm5hIHVuaXZlcnNpdHmSARJnb3Zlcm5tZW50X2NvbGxlZ2XgAQA!16s%2Fm%2F0gx1fyp?entry=ttu&g_ep=EgoyMDI2MDUwMi4wIKXMDSoASAFQAw%3D%3D");

  if (item === "Contact US") setSubmenu("support");
  if (item === "News") setSubmenu("news");
  if (item === "Notes") setNotesOpen(prev => !prev);
  if (item === "Schedule") setSubmenu("schedule");
};
useEffect(() => {
  const handleKey = (e: KeyboardEvent) => {
    if (!open) return;

    if (!notesOpen) {
      if (e.key === "ArrowDown") {
        setActiveIndex(prev => (prev + 1) % menuItems.length);
      }

      if (e.key === "ArrowUp") {
        setActiveIndex(prev =>
          prev === 0 ? menuItems.length - 1 : prev - 1
        );
      }

      if (e.key === "Enter") {
        handleMenuClick(menuItems[activeIndex], activeIndex);
      }
    }

    if (notesOpen) {
      setActiveIndex(menuItems.indexOf("Notes"));
    }
  };

 const handleClickOutside = (e: PointerEvent) => {
  const target = e.target as Node;

  if (!menuRef.current) return;

  if (!menuRef.current.contains(target)) {
    setOpen(false);
    setSubmenu(null);
    setNotesOpen(false);
  }
};

  window.addEventListener("keydown", handleKey);
  document.addEventListener("pointerdown", handleClickOutside);

  return () => {
    window.removeEventListener("keydown", handleKey);
    document.removeEventListener("pointerdown", handleClickOutside);
  };
}, [open, activeIndex, notesOpen, notesIndex]);
useEffect(() => {
  if (submenu !== "news") return;

  const interval = setInterval(() => {
    setCurrentNews((prev) =>
      prev === newsData.length - 1 ? 0 : prev + 1
    );
  }, 3000);

  return () => clearInterval(interval);
}, [submenu, newsData.length]);

  

  return (
    <div ref={menuRef}  className="fixed top-5 right-5 z-[9999]">

      {/* ⚙️ BUTTON */}
      <button
  onClick={() => setOpen(!open)}
  className="
    relative w-8 h-8 rounded-full 
    bg-black/10 backdrop-blur-xl
    border border-black/20
    text-black
    hover:scale-110 transition
  "
>
  ⚙️
</button>

      {/* MENU */}
      {open && (
        <div>
        
  <div className="
    relative right-0 mt-3 w-60
    isolate
    rounded-2xl
    bg-white/10 backdrop-blur-2xl
    border border-white/20
    shadow-[0_10px_40px_rgba(0,0,0,0.6)]
    p-2 space-y-1
  ">

   
    {/* 🔥 GOLD SELECTOR */}
<div
  className="absolute left-0 right-1 h-10 rounded-lg pointer-events-none transition-all duration-300"
  style={{
    top: `${
      notesOpen
        ? menuItems.indexOf("Notes") * 44 + 8
        : activeIndex * 44 + 8
    }px`,
    background: "linear-gradient(90deg, gold, rgba(255,215,0,0.3))",
    boxShadow: "0 0 12px gold"
  }}
/>

    {menuItems.map((item, i) => (
  <div key={i}>
    <button
      onClick={() => handleMenuClick(item, i)}
      className={`
  w-full h-10 flex items-center px-3
  text-black text-sm relative z-[5]
  transition-all duration-200
  hover:bg-white/10
  hover:shadow-[0_0_12px_rgba(255,255,255,0.3)]
  ${activeIndex === i ? "text-white drop-shadow-[0_0_6px_gold]" : ""}
`}
onMouseEnter={() => {
  if (!notesOpen) setActiveIndex(i);
}}
    >
      {item}
    </button>

    {/* NOTES DROPDOWN */}
    {item === "Notes" && notesOpen && (
  <div className="ml-3 mt-1 space-y-1 relative">
    
    {/* 🔥 VIOLET SELECTOR */}
    <div
      className="absolute left-0 right-0 h-8 rounded-lg pointer-events-none transition-all duration-300"
      style={{
        top: `${notesIndex * 32}px`,
        background: "linear-gradient(90deg,rgb(255, 0, 187) , rgba(255, 0, 187, 0.49))",
        boxShadow: "0 0 12px violet"
      }}
    />


    {notesLinks.map((note, idx) => (
  <button
    key={idx}
    onClick={() => window.open(note.link, "_blank")}
    onMouseEnter={() => setNotesIndex(idx)}
    className={`
      block w-full text-left px-2 py-1 text-black text-sm relative z-10
      transition-all duration-200
      ${
        notesIndex === idx
          ? "text-white drop-shadow-[0_0_6px_violet]"
          : ""
      }
    `}
  >
    ✨ {note.title}
  </button>
))}
  </div>
)}
  </div>
))}
  </div>
  
  {submenu && (
  <div className="
    absolute right-64 top-20 w-90 z-[1000]
    rounded-2xl
    bg-white/10 backdrop-blur-2xl
    border border-white/20
    shadow-[0_10px_40px_rgba(0,0,0,0.6)]
    p-3
  ">

    {/* 🔙 BACK */}
    <button
      onClick={() => setSubmenu(null)}
      className="text-sm text-white mb-2 hover:underline"
    >
      ← Back
    </button>

    {/* SUPPORT */}
    {submenu === "support" && (
      <div className="space-y-2">
        {supportMails.map((mail, i) => (
          <div key={i} className="text-black text-sm bg-white/10 p-2  rounded">
            🔖 {mail}
          </div>
        ))}
      </div>
    )}

    {/* NEWS */}
   {/* NEWS */}
{submenu === "news" && (
  <div
    className="
      relative h-44 overflow-hidden
      rounded-2xl
      bg-black/20
      border border-white/10
      p-3
      backdrop-blur-xl
    "
  >
    {/* TOP LIVE HEADER */}
    <div className="flex items-center gap-2 mb-3">
      <div className="w-2 h-2 rounded-full bg-red-500 animate-pulse" />

      <span className="text-white text-xs tracking-widest font-semibold">
        NEWS UPDATES
      </span>
    </div>

    {/* NEWS CONTAINER */}
    <div className="relative h-28 overflow-hidden">
      {newsData.map((n, i) => (
        <div
          key={i}
          className={`
            absolute left-0 w-full
            transition-all duration-700 ease-in-out
            ${
              i === currentNews
                ? "translate-y-0 opacity-100 scale-100"
                : i < currentNews
                ? "-translate-y-20 opacity-0 scale-95"
                : "translate-y-20 opacity-0 scale-95"
            }
          `}
        >
          <div
            className="
              p-4 rounded-2xl
              bg-gradient-to-r
              from-pink-500/20
              to-violet-500/20
              border border-pink-400/20
              shadow-[0_0_20px_rgba(255,0,150,0.4)]
              backdrop-blur-xl
            "
          >
            {/* NEW TAG */}
            <div className="flex items-center justify-between mb-2">
              <span
                className="
                  text-[10px]
                  px-2 py-1
                  rounded-full
                  bg-pink-500/30
                  text-pink-200
                  animate-pulse
                "
              >
                NEW UPDATE
              </span>

              <span className="text-white/40 text-[10px]">
                JUST NOW
              </span>
            </div>

            {/* NEWS TEXT */}
            <div
              className="
                text-yellow-400 text-sm
                font-medium
                leading-relaxed
                drop-shadow-[0_0_8px_rgba(255,255,255,0.4)]
              "
            >
              🔖 {n.title}
            </div>
          </div>
        </div>
      ))}
    </div>

    {/* BOTTOM GLOW */}
    <div
      className="
        absolute bottom-0 left-1/2 -translate-x-1/2
        w-32 h-6
        bg-pink-500/30
        blur-2xl
        rounded-full
        pointer-events-none
      "
    />
  </div>
)}
    {/*Schedule*/}

    {submenu === "schedule" && (
  <div className="space-y-3">
    {scheduleFiles.map((pdf, i) => (
      <div
        key={i}
        className="
          flex items-center justify-between
          bg-white/10
          p-3 rounded-xl
          backdrop-blur-lg
        "
      >
        <div className="text-black text-sm">
          🧶 {pdf.title}
        </div>

        <a
          href={pdf.file}
          download
          className="
            px-3 py-1 rounded-lg
            bg-gradient-to-r from-pink-500 to-violet-500
            text-white text-xs
            hover:scale-105
            transition
          "
        >
          Download
        </a>
      </div>
    ))}
  </div>
)}

  </div>
)}
</div>
)}

    </div>
  );
}


/* 🔥 REUSABLE ITEM */
function MenuItem({
  label,
  link,
  onClick,
}: {
  label: string;
  link?: string;
  onClick?: () => void;
}) {
  return (
    <button
      onClick={() => {
        if (link) window.open(link, "_blank");
        if (onClick) onClick();
      }}
      className="
        w-full text-left px-3 py-2
        rounded-lg
        hover:bg-gray-100
        text-sm text-black
      "
    >
      {label}
    </button>
  );
}