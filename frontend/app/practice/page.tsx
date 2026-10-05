import Link from "next/link";

export default function Page() {
  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/" className="text-sm text-neutral-500">← Arova</Link>
      <h1 className="mt-5 text-3xl font-bold">Practice</h1>
      <p className="mt-2 leading-7 text-neutral-600">Choose a skill without leaving the overall course progression.</p>
      <div className="mt-6 grid gap-3">
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Speaking</h2><p className="mt-1 text-sm text-neutral-600">Conversation and spoken-response practice.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Listening</h2><p className="mt-1 text-sm text-neutral-600">Audio recognition and comprehension.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Quiz Mode</h2><p className="mt-1 text-sm text-neutral-600">Recognition, production, fill-in and open response.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Story Mode</h2><p className="mt-1 text-sm text-neutral-600">Graded stories with comprehension and voice interaction.</p></section>
        <section className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm"><h2 className="font-semibold">Flashcards</h2><p className="mt-1 text-sm text-neutral-600">Build and review focused decks.</p></section>
      </div>
    </main>
  );
}
