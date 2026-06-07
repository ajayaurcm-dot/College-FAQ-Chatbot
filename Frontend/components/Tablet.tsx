"use client";

import { useEffect, useRef, useState } from "react";

const videos = [
  "/videos/video1.mp4",
  
  "/videos/video3.mp4",
  "/videos/video4.mp4",
  "/videos/video6.mp4",
  "/videos/video7.mp4",
  "/videos/video8.mp4",
  "/videos/video9.mp4",

];

export default function Tablet({ volume }: any) {
  const videoRef = useRef<HTMLVideoElement>(null);

  const [currentVideo, setCurrentVideo] = useState(videos[0]);
  const [isFading, setIsFading] = useState(false);

  // 🔀 Random video
  useEffect(() => {
    const getRandomVideo = () => {
      let next;
      do {
        next = videos[Math.floor(Math.random() * videos.length)];
      } while (next === currentVideo);
      return next;
    };

    const interval = setInterval(() => {
      setIsFading(true);

      setTimeout(() => {
        setCurrentVideo(getRandomVideo());
        setIsFading(false);
      }, 500);
    }, 10000);

    return () => clearInterval(interval);
  }, [currentVideo]);

  // 🔊 APPLY VOLUME
  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.volume = volume;
      videoRef.current.muted = volume === 0;
    }
  }, [volume]);

  return (
    <div className="absolute bottom-[0%] left-[0%] w-29 h-51 
     overflow-hidden  bg-black">

      <video
        ref={videoRef}
        key={currentVideo}
        autoPlay
        loop
        playsInline
        onLoadedMetadata={() => {
         if (videoRef.current) {
            videoRef.current.volume = volume;
            videoRef.current.muted = volume === 0;
        }
  }}
        className={`w-full h-full object-cover transition-opacity duration-500 ${
          isFading ? "opacity-0" : "opacity-100"
        }`}
      >
        <source src={currentVideo} type="video/mp4" />
      </video>

      

    </div>
  );
}