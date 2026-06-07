"use client"
import ChatUI from "@/components/ChatUI"
import Particles from "@/components/Particles";
import Image from "next/image"
import Tablet from "@/components/Tablet"
import { useState, useRef, useEffect } from "react";
import SpeakerControl from "@/components/SpeakerControl";
import PremiumClock from "@/components/PremiumClock"
import ModernChatUI from "@/components/ModernChatUI"
import SettingsMenu from "@/components/SettingsMenu";
export default function Home() {
   const [volume, setVolume] = useState(0.5); // 0 to 1
   const [fullscreen, setFullscreen] = useState(false);
   const [menuOpen, setMenuOpen] = useState(false);
   const menuRef = useRef<HTMLDivElement>(null);
   const [messages, setMessages] = useState([]);
   const toggleFullscreen = () => {
   setFullscreen(prev => !prev);
    };
   const supportMails = [
    "Student Section: 0452-2555 544",
     "Email: helpdesk@autmdu.in",
     "Email: dean@autmdu.ac.in",
     "Placements: tpo_aurcm@autmdu.in",
     "Posh Cell: aurcmposhcell@autmdu.in",
     "GrievanceCell: aurcmgrievancecell@autmdu.in"
   ];

   const newsData = [
    { title: "Practical Exams are Started" },
    { title: "New lab inaugurated" },
    { title: "Placement drive announced" },
    { title: "Exam Dates are announced" }
    ];



   useEffect(() => {
  function handleClickOutside(e: MouseEvent) {
    if (menuRef.current && !menuRef.current.contains(e.target as Node)) {
      setMenuOpen(false);
    }
  }

  if (menuOpen) {
    document.addEventListener("click", handleClickOutside);
  }

  return () => {
    document.removeEventListener("click", handleClickOutside);
  };
}, [menuOpen]);
   
  return (
    <main className="relative h-screen w-full [perspective:1200px]"> 
    
    
     <Image 
         src="/abi1.png"
         alt="background"
         sizes="100vw"
         fill
         className="object-cover opacity-100 pointer-events-none select-none"
         />
         <div className="absolute bg-white rounded-full shadow-[0_0_6px_rgba(255,255,255,0.6)] z-[9999]"><Particles /></div>
         

     

      {/********************************************** PHONE **********************************************/}
      <div className="absolute  bg-gray-900 rounded-lg overflow-hidden  shadow-xl
      
           bottom-29 left-78

           w-29 h-51

           [transform:rotateX(28deg)_rotateY(48deg)__rotateZ(-21deg)] 

           shadow-[0_0_80px_rgba(0,255,150,0.25)]
      
      " 
      >       {/* 🎥 Tablet */}
      <Tablet volume={volume} />

     

                      
             <div className="absolute inset-0 overflow-hidden">

              <div className="absolute top-0 left-[-50%] w-[50%] h-full
                bg-gradient-to-r from-transparent via-white/40 to-transparent
                blur-xl
                skew-x-[20deg]
                animate-light-sweep
                pointer-events-none" />

           </div>

      
      
  
         
     </div> 








         {/*********************************************** LIGHT **************************************/}

      {/* Yellow LIGHT */}
      <div className="absolute bottom-15 left-14 w-20 h-30 bg-yellow-500 opacity-50 rounded-full blur-3xl animate-glow-pulse " />

      {/* White LIGHT */}
      <div className="absolute bottom-106 left-61 w-25 h-25 rounded-full blur-2xl opacity-50 animate-rgb-light glow" />




      {/* ================= NORMAL MONITOR ================= */}
      {!fullscreen && (
        <div className="absolute top-18 left-128 w-[51%] h-[66%] rounded-3xl border border-gray-450 relative overflow-hidden z-20
  [transform:rotateX(0deg)_rotateY(-15deg)_rotateZ(0deg)]">

          <Image 
            src="/balo.png"
            alt="monitor"
            fill
            className="object-cover z-0"
          />

          <ChatUI messages={messages} setMessages={setMessages} />

        </div>
      )}

     {/* ================= FULLSCREEN CHAT ================= */}


      {/* 🔥 INVISIBLE HOTSPOT */}
      <div
        className="fixed bottom-8 right-68 rounded w-16 h-16 z-[100]  cursor-pointer"
        onClick={(e) => {
          e.stopPropagation();
          setMenuOpen(!menuOpen);
        }}
      />

      {/* 🔥 FLOATING MENU */}
{menuOpen && (
  <div
    ref={menuRef}
    className="
      fixed bottom-4 right-28 z-[110]
      w-38 rounded-xl
      bg-white/10 backdrop-blur-xl
      border border-white/20
      shadow-[0_10px_40px_rgba(0,0,0,0.6)]
      p-2
    "
  >
    <button
      onClick={() => {
        setFullscreen(true);
        setMenuOpen(false);
      }}
      className="
        w-full text-left px-3 py-2
        rounded-lg
        hover:bg-white/20
        text-white text-sm
        transition
      "
    >
      Full Screen Mode
    </button>
  </div>
)}
      {/* 🌟 MONITOR BOTTOM GLOW (OUTSIDE) */}
         <div
         className="
         absolute 
         top-[75%] left-[68%] -translate-x-1/2
         w-[50%] h-10
         blur-3xl 
         rounded-full 
         opacity-99
         pointer-events-none
         z-10
         bg-blue-200
         glow
        "
/>
{/* 🎯 LIGHT CONTAINER (SAME WIDTH AS MONITOR) */}
<div
  className="
  absolute
  top-[75%] left-[65%] -translate-x-1/2
  w-[50%] h-16
  rounded-full 
  overflow-hidden
  pointer-events-none
  z-10
  
  
  [transform:rotateX(0deg)_rotateY(-15deg)_rotateZ(0deg)] 
  opacity-60
  "
  style={{
    WebkitMaskImage: `
      linear-gradient(to right, transparent, black 15%, black 85%, transparent),
      linear-gradient(to top, transparent, black 30%, black 70%, transparent)
    `,
    WebkitMaskComposite: "destination-in",
    maskImage: `
      linear-gradient(to right, transparent, black 15%, black 85%, transparent),
      linear-gradient(to top, transparent, black 30%, black 70%, transparent)
    `,
    maskComposite: "intersect",
  }}
>
  {/* ✨ MOVING LIGHT */}
  <div
    className="
    absolute
    left-[-40%]
    w-[40%] h-full
    blur-2xl
    animate-monitor-light
    "
    style={{
      background:
        "linear-gradient(to right, transparent, rgba(0,255,255,0.8), transparent)",
    }}
  />
</div>

       

      {/********************************** RIGHT LAMP **************************************/}
      <div className="absolute top-88 right-2 w-24 h-24 bg-white rounded-full blur-3xl opacity-150 glow" />


       
      {/********************************** PremiumClock **************************************/}

<div className="
absolute bottom-16 right-9
[transform:rotateX(0deg)_rotateY(-62deg)] 
z-30
"
>
  
  

  <PremiumClock />
  

</div>
 {/* 🔊 Speaker */}
      <SpeakerControl volume={volume} 
                      setVolume={setVolume} />




                    {fullscreen && (
  <div className="fixed inset-0 z-[999]">

    {/* 🔥 BACKGROUND */}
    <div className="absolute inset-0">
      <Image
        src="/ramnadu.png"   // 👈 change here
        alt="bg"
        fill
        className="object-cover"
      />
    </div>

   

    {/* 🔥 CHAT */}
    <div className="absolute inset-0 z-10">
      
      {fullscreen && (
  <div className="fixed inset-0 z-[999]">

    {/* CLEAN WHITE BACKGROUND */}
    <div className="absolute inset-0 bg-white" />

    {/* NEW MODERN CHAT UI */}
    <div className="absolute inset-0 z-10">
      <ModernChatUI
        messages={messages} 
        setMessages={setMessages} 
      />
    </div>

    {/* SETTINGS BUTTON */}
 
    </div>

)}
    </div>

    {/* 🔥 SETTINGS BUTTON (TOP RIGHT) */}
    
      {/* ✅ ADD HERE */}
    <SettingsMenu 
  onToggle={toggleFullscreen} 
  isFullscreen={fullscreen}
  supportMails={supportMails}
  newsData={newsData}
/>

      
    </div>

  
)}



    </main>
  );
}
