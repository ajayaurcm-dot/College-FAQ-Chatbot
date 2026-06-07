import React from "react";

const urlRegex = /(https?:\/\/[^\s]+)/g;

export default function MessageRenderer({ text }: { text: string }) {
  // 🔥 STEP 1: FIX NUMBERED LIST
  const formattedText = text
    .replace(/(\d+\.\s)/g, "\n$1") // add line break before 1. 2. 3.
    .trim();

  const lines = formattedText.split("\n");

  return (
    <>
      {lines.map((line, i) => {
  urlRegex.lastIndex = 0; // 🔥 IMPORTANT

  const parts: React.ReactNode[] = [];
  let lastIndex = 0;
  let match;

  while ((match = urlRegex.exec(line)) !== null) {
    const rawUrl = match[0];
    const cleanUrl = rawUrl.replace(/[.,!?;:]+$/, "");

    if (match.index > lastIndex) {
      parts.push(
        <span key={`text-${lastIndex}`}>
          {line.slice(lastIndex, match.index)}
        </span>
      );
    }

    let domain = "";
    try {
      domain = new URL(cleanUrl).hostname.replace("www.", "");
    } catch {
      domain = cleanUrl;
    }

    parts.push(
      <a
        key={`${cleanUrl}-${match.index}`} // ✅ FIXED
        href={cleanUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="link-card"
      >
        <div className="link-icon">↗</div>
        <div className="link-body">
          <div className="link-title">Open Portal</div>
          <div className="link-url">{domain}</div>
        </div>
        <div className="link-arrow">›</div>
      </a>
    );

    lastIndex = match.index + rawUrl.length;
  }

  if (lastIndex < line.length) {
    parts.push(
      <span key={`text-${lastIndex}`}>
        {line.slice(lastIndex)}
      </span>
    );
  }

  return (
    <div key={i} className="mb-1">
      {parts}
    </div>
  );
})}
    </>
  );
}