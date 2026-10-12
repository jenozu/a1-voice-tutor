"use client";

type Props = {
  text: string;
  label?: string;
  className?: string;
};

export default function SpeakButton({ text, label = "Listen", className = "arova-button" }: Props) {
  function speak() {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "ru-RU";
    window.speechSynthesis.speak(utterance);
  }

  return (
    <button type="button" onClick={speak} className={className}>
      {label}
    </button>
  );
}
