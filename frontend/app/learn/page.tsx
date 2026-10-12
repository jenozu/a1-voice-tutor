"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import AppNav from "@/components/AppNav";
import { apiUrl } from "@/lib/api";

type ProfileResponse = {
  configured: boolean;
  profile: null | {
    minutes_per_day: number;
    study_days: string[];
    pace: string;
    plan: { estimated_weeks: number; weekly_minutes: number; recommended_minutes_per_day_for_target: number; };
  };
};

export default function LearnPage() {
  const [data, setData] = useState<ProfileResponse | null>(null);
  const [failed, setFailed] = useState(false);

  useEffect(() => {
    fetch(apiUrl("/api/profile"))
      .then((response) => { if (!response.ok) throw new Error(); return response.json(); })
      .then(setData)
      .catch(() => setFailed(true));
  }, []);

  return (
    <main className="arova-shell">
      <Link href="/" className="text-sm font-bold text-neutral-500">← Arova</Link>
      <div className="mt-5">
        <p className="arova-kicker text-neutral-500">Russian A1</p>
        <h1 className="mt-1 text-4xl font-black tracking-[-0.04em]">Learn</h1>
        <p className="mt-2 max-w-xl leading-7 text-neutral-600">A structured course, but every lesson still feels alive: useful language, sound, grammar, linguistics, culture and speaking.</p>
      </div>

      {!data && !failed && <p className="mt-6 text-sm text-neutral-500">Loading your plan…</p>}

      {(failed || data?.configured === false) && (
        <section className="mt-6 rounded-[2rem] bg-[var(--arova-pink)] p-6">
          <p className="arova-kicker">First step</p>
          <h2 className="mt-2 text-2xl font-black">Build your study plan</h2>
          <p className="mt-2 text-sm leading-6 text-neutral-700">Choose your days, pace and target so Arova can make the course feel realistic.</p>
          <Link href="/onboarding" className="arova-button mt-5">Start setup</Link>
        </section>
      )}

      {data?.configured && data.profile && (
        <>
          <section className="mt-6 grid grid-cols-3 gap-2">
            {[
              ["Weekly", `${data.profile.plan.weekly_minutes} min`],
              ["Study days", String(data.profile.study_days.length)],
              ["Est. course", `${data.profile.plan.estimated_weeks} wk`],
            ].map(([label,value]) => (
              <div key={label} className="rounded-2xl bg-white p-4 shadow-sm">
                <p className="text-xs font-bold text-neutral-500">{label}</p>
                <p className="mt-1 text-lg font-black">{value}</p>
              </div>
            ))}
          </section>

          <section className="mt-5 overflow-hidden rounded-[2rem] bg-[var(--arova-pink)] p-6">
            <div className="flex justify-between gap-4">
              <p className="arova-kicker">Lesson 1 · Session 1</p>
              <span className="rounded-full bg-white/70 px-3 py-1 text-xs font-bold">10 min</span>
            </div>
            <h2 className="mt-4 text-3xl font-black tracking-tight">Russian Sounds, Cyrillic & First Conversation</h2>
            <p className="mt-3 text-sm leading-6 text-neutral-700">Your first 10 high-value items plus active recall, pronunciation, linguistics and culture.</p>

            <div className="mt-5 h-3 overflow-hidden rounded-full bg-white/60">
              <div className="h-full w-[35%] rounded-full bg-black" />
            </div>
            <div className="mt-2 flex justify-between text-xs font-bold"><span>Progress</span><span>35%</span></div>

            <div className="mt-5 flex flex-wrap gap-2 text-xs font-bold">
              {["Vocabulary", "Listening", "Linguistics", "Speaking"].map((tag) => (
                <span key={tag} className="rounded-full bg-white/65 px-3 py-2">{tag}</span>
              ))}
            </div>

            <Link href="/learn/session/1" className="arova-button mt-6">Continue lesson</Link>
          </section>

          <section className="mt-6">
            <div className="flex items-end justify-between">
              <div>
                <p className="arova-kicker text-neutral-500">Course path</p>
                <h2 className="mt-1 text-2xl font-black">What comes next</h2>
              </div>
              <Link href="/onboarding" className="text-sm font-bold underline">Adjust plan</Link>
            </div>
            <div className="mt-3 grid gap-3">
              {[
                ["01", "Sounds & First Conversation", "In progress", "bg-[var(--arova-pink)]"],
                ["02", "People & Basic Conversation", "Next", "bg-[var(--arova-lilac)]"],
                ["03", "Ask for Information", "Locked", "bg-white"],
              ].map(([n,title,status,bg]) => (
                <div key={n} className={`flex items-center gap-4 rounded-3xl border border-[var(--arova-line)] p-4 ${bg}`}>
                  <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-black text-sm font-black text-white">{n}</span>
                  <div className="min-w-0 flex-1">
                    <p className="font-black">{title}</p>
                    <p className="mt-1 text-xs font-bold text-neutral-500">{status}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>
        </>
      )}
      <AppNav />
    </main>
  );
}
