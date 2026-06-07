import React from 'react';

const Background = ({ videoState }) => {
  return (
    <div className="video-background">

     <video
  autoPlay
  loop
  muted
  playsInline
  preload="auto"
  className={`background-video ${videoState === 'idle' ? 'active' : ''}`}
>
  <source src="/videos/idle.mp4" type="video/mp4" />
</video>

<video
  autoPlay
  loop
  muted
  playsInline
  preload="auto"
  className={`background-video ${videoState === 'typing' ? 'active' : ''}`}
>
  <source src="/videos/typing.mp4" type="video/mp4" />
</video>

<video
  autoPlay
  loop
  muted
  playsInline
  preload="auto"
  className={`background-video ${videoState === 'reading' ? 'active' : ''}`}
>
  <source src="/videos/reading.mp4" type="video/mp4" />
</video>
<div className="video-overlay"></div>

    </div>
  );
};

export default Background;