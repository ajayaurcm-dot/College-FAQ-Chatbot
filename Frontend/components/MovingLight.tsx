"use client";

import { motion } from "framer-motion";

export default function MovingLight() {
  return (
    <motion.div
      className="absolute w-40 h-40 bg-green-400 blur-3xl rounded-full opacity-40 pointer-events-none"
      animate={{
        x: [0, 50, -30, 0],
        y: [0, -20, 30, 0],
      }}
      transition={{
        duration: 6,
        repeat: Infinity,
        ease: "easeInOut",
      }}
    />
  );
}