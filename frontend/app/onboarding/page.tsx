"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { apiUrl } from "@/lib/api";

const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

export default function OnboardingPage() {
  const router = useRouter();
  const [targetDate, setTargetDate] = useState("");
  const [studyDays, setStudyDays] = useState<string[]>(["Mon", "Wed", "Fri", "Sun"]);
  const [minutes, setMinutes] = useState(25);
  const [pace, setPace] = useState("standard");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  function toggleDay(day: string) {
    setStudyDays((current) =>
      current.includes(day) ? current.filter((value) => value !== day) : [...current, day]
    );
  }

  async function submit(event: FormEvent) {
    event.preventDefault();
    setSaving(true);
    setError("");
    try {
      const response = await fetch(apiUrl("/api/profile"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          language: "Russian",
          target_level: "A1",
          target_date: targetDate || null,
          study_days: studyDays,
          minutes_per_day: minutes,
          pace,
        }),
      });
      if (!response.ok) throw new Error("Could not save your study plan.");
      router.push("/learn");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/" className="text-sm text-neutral-500">← Arova</Link>
      <p className="mt-6 text-xs font-semibold uppercase tracking-[0.15em] text-neutral-500">
        Setup
      </p>
      <h1 className="mt-2 text-3xl font-bold">Build your Russian A1 plan</h1>
      <p className="mt-2 leading-7 text-neutral-600">
        Arova will use your available time to pace the 24-lesson course. Mastery still controls
        when you advance.
      </p>

      <form onSubmit={submit} className="mt-7 space-y-6">
        <label className="block">
          <span className="text-sm font-semibold">Target date (optional)</span>
          <input
            type="date"
            value={targetDate}
            onChange={(event) => setTargetDate(event.target.value)}
            className="mt-2 w-full rounded-xl border border-neutral-300 bg-white px-3 py-3"
          />
        </label>

        <fieldset>
          <legend className="text-sm font-semibold">Study days</legend>
          <div className="mt-2 grid grid-cols-4 gap-2">
            {days.map((day) => (
              <button
                type="button"
                key={day}
                onClick={() => toggleDay(day)}
                className={`rounded-xl border px-3 py-2 text-sm ${
                  studyDays.includes(day)
                    ? "border-neutral-900 bg-neutral-900 text-white"
                    : "border-neutral-300 bg-white"
                }`}
              >
                {day}
              </button>
            ))}
          </div>
        </fieldset>

        <label className="block">
          <span className="text-sm font-semibold">Minutes per study day</span>
          <input
            type="number"
            min={5}
            max={240}
            step={5}
            value={minutes}
            onChange={(event) => setMinutes(Number(event.target.value))}
            className="mt-2 w-full rounded-xl border border-neutral-300 bg-white px-3 py-3"
          />
        </label>

        <label className="block">
          <span className="text-sm font-semibold">Pace</span>
          <select
            value={pace}
            onChange={(event) => setPace(event.target.value)}
            className="mt-2 w-full rounded-xl border border-neutral-300 bg-white px-3 py-3"
          >
            <option value="relaxed">Relaxed</option>
            <option value="standard">Standard</option>
            <option value="intensive">Intensive</option>
            <option value="custom">Custom</option>
          </select>
        </label>

        {error && <p className="text-sm font-medium text-red-700">{error}</p>}

        <button
          type="submit"
          disabled={saving || studyDays.length === 0}
          className="w-full rounded-xl bg-neutral-900 px-4 py-3 font-semibold text-white disabled:opacity-50"
        >
          {saving ? "Creating plan..." : "Create my plan"}
        </button>
      </form>
    </main>
  );
}
