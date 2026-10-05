import Link from "next/link";

export default function Page() {
  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/" className="text-sm text-neutral-500">← Arova</Link>
      <h1 className="mt-5 text-3xl font-bold">Progress</h1>
      <p className="mt-2 leading-7 text-neutral-600">See what you can actually recognize, produce and use.</p>
      <div className="mt-6 grid gap-3">
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Course progress</h2><p className="mt-1 text-sm text-neutral-600">Your path through Russian A1.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Mastery</h2><p className="mt-1 text-sm text-neutral-600">Recognition and production tracked separately.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Practice time</h2><p className="mt-1 text-sm text-neutral-600">Speaking and listening time.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Goals</h2><p className="mt-1 text-sm text-neutral-600">Weekly study target, streak and XP.</p></section>
      </div>
    </main>
  );
}
