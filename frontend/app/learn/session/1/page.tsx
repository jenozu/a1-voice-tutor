"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { apiUrl } from "@/lib/api";

type Item = {
  id: string;
  cyrillic: string;
  romanization: string;
  english: string;
};

type Session = {
  title: string;
  focus: string;
  items: Item[];
};

type Phase = "recognition" | "production" | "complete";

export default function SessionOnePage() {
  const [session, setSession] = useState<Session | null>(null);
  const [phase, setPhase] = useState<Phase>("recognition");
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [recognitionCorrect, setRecognitionCorrect] = useState(0);
  const [productionCorrect, setProductionCorrect] = useState(0);
  const [result, setResult] = useState<{ advance: boolean } | null>(null);

  useEffect(() => {
    fetch(apiUrl("/api/courses/ru-a1/stage-1/sessions/1"))
      .then((response) => response.json())
      .then(setSession);
  }, []);

  const item = useMemo(() => session?.items[index], [session, index]);

  async function answer(correct: boolean) {
    if (!session) return;
    if (phase === "recognition" && correct) setRecognitionCorrect((value) => value + 1);
    if (phase === "production" && correct) setProductionCorrect((value) => value + 1);

    if (index < session.items.length - 1) {
      setIndex((value) => value + 1);
      setRevealed(false);
      return;
    }

    if (phase === "recognition") {
      setPhase("production");
      setIndex(0);
      setRevealed(false);
      return;
    }

    const finalProduction = productionCorrect + (correct ? 1 : 0);
    const recognitionPercent = Math.round((recognitionCorrect / session.items.length) * 100);
    const productionPercent = Math.round((finalProduction / session.items.length) * 100);

    const response = await fetch(apiUrl("/api/courses/ru-a1/stage-1/mastery"), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        recognition_percent: recognitionPercent,
        production_percent: productionPercent,
      }),
    });
    const mastery = await response.json();
    setResult(mastery);
    setPhase("complete");
  }

  if (!session) {
    return <main className="mx-auto max-w-xl px-5 py-8">Loading session…</main>;
  }

  const recognitionPercent = Math.round((recognitionCorrect / session.items.length) * 100);
  const productionPercent = Math.round((productionCorrect / session.items.length) * 100);

  if (phase === "complete") {
    return (
      <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
        <Link href="/learn" className="text-sm text-neutral-500">← Learn</Link>
        <h1 className="mt-6 text-3xl font-bold">Session complete</h1>
        <div className="mt-6 grid grid-cols-2 gap-3">
          <div className="rounded-2xl border border-neutral-200 bg-white p-4">
            <p className="text-sm text-neutral-500">Recognition</p>
            <p className="mt-1 text-2xl font-bold">{recognitionPercent}%</p>
          </div>
          <div className="rounded-2xl border border-neutral-200 bg-white p-4">
            <p className="text-sm text-neutral-500">Production</p>
            <p className="mt-1 text-2xl font-bold">{productionPercent}%</p>
          </div>
        </div>
        <section className="mt-4 rounded-2xl border border-neutral-200 bg-white p-5">
          <h2 className="font-semibold">{result?.advance ? "Mastery gate passed" : "Keep reviewing"}</h2>
          <p className="mt-2 text-sm leading-6 text-neutral-600">
            Arova requires at least 80% recognition and 70% production. Weak items will eventually
            feed directly into FSRS review.
          </p>
        </section>
      </main>
    );
  }

  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/learn" className="text-sm text-neutral-500">← Learn</Link>
      <p className="mt-6 text-xs font-semibold uppercase tracking-[0.15em] text-neutral-500">
        {phase === "recognition" ? "Recognition" : "Production"} · {index + 1}/10
      </p>
      <h1 className="mt-2 text-2xl font-bold">{session.title}</h1>

      <section className="mt-6 rounded-3xl border border-neutral-200 bg-white p-7 text-center shadow-sm">
        {phase === "recognition" ? (
          <>
            <p className="text-4xl font-semibold">{item?.cyrillic}</p>
            <p className="mt-3 text-sm text-neutral-500">{item?.romanization}</p>
            {revealed && <p className="mt-6 text-xl">{item?.english}</p>}
          </>
        ) : (
          <>
            <p className="text-2xl font-semibold">{item?.english}</p>
            {revealed && (
              <>
                <p className="mt-6 text-4xl font-semibold">{item?.cyrillic}</p>
                <p className="mt-2 text-sm text-neutral-500">{item?.romanization}</p>
              </>
            )}
          </>
        )}

        {!revealed ? (
          <button
            onClick={() => setRevealed(true)}
            className="mt-8 rounded-xl bg-neutral-900 px-5 py-3 text-sm font-semibold text-white"
          >
            Reveal answer
          </button>
        ) : (
          <div className="mt-8 grid grid-cols-2 gap-3">
            <button onClick={() => answer(false)} className="rounded-xl border border-neutral-300 px-4 py-3">
              Again
            </button>
            <button onClick={() => answer(true)} className="rounded-xl bg-neutral-900 px-4 py-3 font-semibold text-white">
              Got it
            </button>
          </div>
        )}
      </section>

      <section className="mt-5 rounded-2xl border border-neutral-200 bg-white p-4">
        <p className="text-xs font-semibold uppercase tracking-[0.15em] text-neutral-500">
          Linguistics · Learn why
        </p>
        <h2 className="mt-2 font-semibold">Russian can omit “to be” in the present tense</h2>
        <p className="mt-2 text-sm leading-6 text-neutral-600">
          English usually needs “am / is / are.” Russian commonly leaves the present-tense form of
          “to be” unstated: “Я студент” literally reads closer to “I student,” but means “I am a
          student.” This is one reason short Russian sentences can feel structurally different.
        </p>
        <Link href="/explore/linguistics" className="mt-3 inline-block text-sm underline">
          Go deeper
        </Link>
      </section>

      <section className="mt-3 rounded-2xl border border-neutral-200 bg-white p-4">
        <p className="text-xs font-semibold uppercase tracking-[0.15em] text-neutral-500">Culture</p>
        <h2 className="mt-2 font-semibold">Ты vs. Вы</h2>
        <p className="mt-2 text-sm leading-6 text-neutral-600">
          Ты is informal singular “you.” Вы is plural “you” and is also used as a polite/formal
          singular form. Arova introduces both immediately because choosing between them matters in
          real conversation.
        </p>
      </section>
    </main>
  );
}
