const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-screen max-w-xl flex-col gap-6 px-5 py-10">
      <div className="space-y-2">
        <p className="text-sm font-semibold uppercase tracking-[0.18em] text-neutral-500">
          Russian A1
        </p>
        <h1 className="text-4xl font-bold tracking-tight">A1 Voice Tutor</h1>
        <p className="text-base leading-7 text-neutral-700">
          Mobile-first lessons built around high-value Russian, active recall,
          listening, speaking, and spaced review.
        </p>
      </div>

      <section className="rounded-2xl border border-neutral-200 bg-white p-5 shadow-sm">
        <h2 className="text-lg font-semibold">MVP foundation</h2>
        <ul className="mt-3 space-y-2 text-sm leading-6 text-neutral-700">
          <li>Next.js + TypeScript frontend</li>
          <li>FastAPI + SQLite backend</li>
          <li>faster-whisper speech-to-text</li>
          <li>Browser Russian text-to-speech</li>
          <li>FSRS review scheduling</li>
        </ul>
        <p className="mt-4 text-xs text-neutral-500">API: {apiBase}</p>
      </section>
    </main>
  );
}
