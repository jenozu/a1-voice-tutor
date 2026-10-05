import Link from "next/link";

export default function Page() {
  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/" className="text-sm text-neutral-500">← Arova</Link>
      <h1 className="mt-5 text-3xl font-bold">Review</h1>
      <p className="mt-2 leading-7 text-neutral-600">Arova will use FSRS plus performance data to bring back material at the right time.</p>
      <div className="mt-6 grid gap-3">
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Due reviews</h2><p className="mt-1 text-sm text-neutral-600">New and weak items scheduled by FSRS.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Weak vocabulary</h2><p className="mt-1 text-sm text-neutral-600">Items with low recognition or production.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Weak skills</h2><p className="mt-1 text-sm text-neutral-600">Grammar, listening and speaking errors will eventually feed this area.</p></section>
      </div>
    </main>
  );
}
