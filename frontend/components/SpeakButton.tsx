"use client";

import { useState } from "react";
import { apiUrl } from "@/lib/api";

type Props = {
  text: string;
  label?: string;
  className?: string;
  rate?: number;
};

function browserFallback(text: string, rate: number) {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "ru-RU";
  utterance.rate = Math.max(0.5, Math.min(rate, 1.5));
  window.speechSynthesis.speak(utterance);
}

export default function SpeakButton({
  text,
  label = "Listen",
  className = "arova-button",
  rate = 1,
}: Props) {
  const [loading, setLoading] = useState(false);

  async function speak() {
    if (loading) return;
    setLoading(true);
    try {
      const response = await fetch(apiUrl("/api/tts"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        browserFallback(text, rate);
        return;
      }

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const audio = new Audio(url);
      audio.playbackRate = rate;
      audio.addEventListener("ended", () => URL.revokeObjectURL(url), { once: true });
      audio.addEventListener("error", () => URL.revokeObjectURL(url), { once: true });
      await audio.play();
    } catch {
      browserFallback(text, rate);
    } finally {
      setLoading(false);
    }
  }

  return (
    <button type="button" onClick={speak} className={className} disabled={loading}>
      {loading ? "Loading…" : label}
    </button>
  );
}
