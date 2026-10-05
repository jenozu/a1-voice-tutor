"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { apiUrl } from "@/lib/api";

type ProfileResponse = {
  configured: boolean;
  profile: null | {
    minutes_per_day: number;
    study_days: string[];
    pace: string;
    plan: {
      estimated_weeks: number;
      weekly_minutes: number;
      recommended_minutes_per_day_for_target: number;
    };
  };
};

export default function LearnPage() {
  const [data, setData] = useState<ProfileResponse | null>(null);
  const [failed, setFailed] = useState(false);

  useEffect(() => {
    fetch(apiUrl("/api/profile"))
      .then((response) => {
        if (!response.ok) throw new Error();
        return response.json();
      })
      .then(setData)
      .catch(() => setFailed(true));
  }, []);

  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/" className="text-sm text-neutral-500">← Arova</Link>
      <h1 className="mt-5 text-3xl font-bold">Learn</h1>
      <p className="mt-2 leading-7 text-neutral-600">
        Your structured Russian A1 course combines Pareto language with grammar, linguistics,
        culture, listening and speaking.
      </p>

      {!data && !failed && <p className="mt-6 text-sm text-neutral-500">Loading your plan…</p>}

      {(failed || data?.configured === false) && (
        <section className="mt-6 rounded-2xl border border-neutral-200 bg-white p-5 shadow-sm">
          <h2 className="font-semibold">Set up your study plan first</h2>
          <p className="mt-2 text-sm leading-6 text-neutral-600">
            Choose your study days, pace and target so Arova can schedule the course.
          </p>
          <Link
            href="/onboarding"
            className="mt-4 inline-flex rounded-xl bg-neutral-900 px-4 py-2.5 text-sm font-semibold text-white"
          >
            Start setup
          </Link>
        </section>
      )}

      {data?.configured && data.profile && (
        <>
          <section className="mt-6 grid grid-cols-3 gap-2">
            <div className="rounded-xl border border-neutral-200 bg-white p-3">
              <p className="text-xs text-neutral-500">Weekly</p>
              <p className="mt-1 font-semibold">{data.profile.plan.weekly_minutes} min</p>
            </div>
            <div className="rounded-xl border border-neutral-200 bg-white p-3">
              <p className="text-xs text-neutral-500">Study days</p>
              <p className="mt-1 font-semibold">{data.profile.study_days.length}</p>
            </div>
            <div className="rounded-xl border border-neutral-200 bg-white p-3">
              <p className="text-xs text-neutral-500">Est. course</p>
              <p className="mt-1 font-semibold">{data.profile.plan.estimated_weeks} wk</p>
            </div>
          </section>

          <section className="mt-4 rounded-2xl border border-neutral-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-semibold uppercase tracking-[0.15em] text-neutral-500">
              Lesson 1 · Pareto Session 1
            </p>
            <h2 className="mt-2 text-xl font-semibold">
              Russian Sounds, Cyrillic & First Conversation
            </h2>
            <p className="mt-2 text-sm leading-6 text-neutral-600">
              Your first 10 high-value items, active recall, a linguistics concept and a mastery
              check.
            </p>
            <Link
              href="/learn/session/1"
              className="mt-4 inline-flex rounded-xl bg-neutral-900 px-4 py-2.5 text-sm font-semibold text-white"
            >
              Start session
            </Link>
          </section>

          <Link href="/onboarding" className="mt-4 inline-block text-sm text-neutral-500 underline">
            Adjust study plan
          </Link>
        </>
      )}
    </main>
  );
}
