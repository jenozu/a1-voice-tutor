import Link from "next/link";

export default function Page() {
  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/" className="text-sm text-neutral-500">← Arova</Link>
      <h1 className="mt-5 text-3xl font-bold">Learn</h1>
      <p className="mt-2 leading-7 text-neutral-600">Your structured Russian A1 course. Pareto-selected language is taught through complete lessons, not isolated word lists.</p>
      <div className="mt-6 grid gap-3">
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Continue Lesson 1</h2><p className="mt-1 text-sm text-neutral-600">Russian Sounds, Cyrillic & First Conversation.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Course map</h2><p className="mt-1 text-sm text-neutral-600">24 A1 lessons will live here as the course is authored.</p></section>
      </div>
    </main>
  );
}
