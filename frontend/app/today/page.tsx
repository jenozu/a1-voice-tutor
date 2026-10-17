"use client";

import Link from "next/link";
import { useState } from "react";
import AppNav from "@/components/AppNav";
import SpeakButton from "@/components/SpeakButton";

export default function TodayPage() {
  const [revealed, setRevealed] = useState(false);

  return (
    <main className="arova-shell">
      <Link href="/" className="text-sm font-bold text-neutral-500">← Home</Link>
      <section className="mt-5 rounded-[2rem] bg-[var(--arova-pink)] p-6">
        <p className="arova-kicker">Word of the day</p>
        <p className="mt-7 text-5xl font-black">сегодня</p>
        <p className="mt-2 text-sm font-bold text-neutral-600">segodnya</p>
        <p className="mt-5 text-2xl font-bold">today</p>
        <div className="mt-5 flex flex-wrap gap-2">
          <SpeakButton text="сегодня" label="Normal" />
          <SpeakButton text="сегодня" label="Slow" rate={0.78} className="arova-button-soft" />
          <SpeakButton text="Сегодня я работаю." label="Sentence" className="arova-button-soft" />
        </div>
      </section>

      <section className="arova-card mt-5 p-5">
        <p className="arova-kicker text-neutral-500">Use it</p>
        <p className="mt-3 text-2xl font-black">Сегодня я работаю.</p>
        <p className="mt-2 text-neutral-600">Today I am working.</p>
      </section>

      <section className="arova-card mt-5 p-5">
        <p className="arova-kicker text-neutral-500">Quick recall</p>
        <h2 className="mt-2 text-xl font-black">What does сегодня mean?</h2>
        {!revealed ? (
          <button type="button" onClick={() => setRevealed(true)} className="arova-button mt-5">Reveal answer</button>
        ) : (
          <div className="mt-5 rounded-2xl bg-[var(--arova-mint)] p-4">
            <p className="text-xl font-black">today</p>
            <p className="mt-1 text-sm text-neutral-600">Now say сегодня aloud before moving on.</p>
          </div>
        )}
      </section>

      <section className="mt-5 rounded-[2rem] bg-[var(--arova-yellow)] p-5">
        <p className="arova-kicker">Linguistics connection</p>
        <h2 className="mt-2 text-xl font-black">Words of time often anchor short Russian sentences.</h2>
        <p className="mt-2 text-sm leading-6 text-neutral-700">
          Arova will keep resurfacing high-utility time words like сегодня, завтра and вчера because they combine easily with many verbs and situations.
        </p>
      </section>

      <AppNav />
    </main>
  );
}
