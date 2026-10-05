import Link from "next/link";

export default function Page() {
  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/" className="text-sm text-neutral-500">← Arova</Link>
      <h1 className="mt-5 text-3xl font-bold">Explore</h1>
      <p className="mt-2 leading-7 text-neutral-600">Go deeper without cluttering the main lesson flow.</p>
      <div className="mt-6 grid gap-3">
        <Link href="/explore/linguistics" className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Linguistics</h2><p className="mt-1 text-sm text-neutral-600">Why Russian works the way it does.</p></Link>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Culture</h2><p className="mt-1 text-sm text-neutral-600">Useful cultural context connected to real language use.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Etymology</h2><p className="mt-1 text-sm text-neutral-600">Word origins and families when they improve memory.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Grammar Reference</h2><p className="mt-1 text-sm text-neutral-600">A browsable reference linked back to lessons.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Word Bank</h2><p className="mt-1 text-sm text-neutral-600">Search learned and upcoming vocabulary.</p></section>
      </div>
    </main>
  );
}
