import Link from "next/link";

const navigation = [
  { href: "/learn", title: "Learn", text: "Follow your structured A1 course and today's lesson." },
  { href: "/practice", title: "Practice", text: "Speaking, listening, quizzes, stories and flashcards." },
  { href: "/review", title: "Review", text: "FSRS reviews and weak-area recovery." },
  { href: "/explore", title: "Explore", text: "Linguistics, culture, etymology, grammar and word bank." },
  { href: "/progress", title: "Progress", text: "Course progress, mastery, XP, streaks and goals." },
];

export default function HomePage() {
  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <header className="mb-8">
        <p className="text-sm font-semibold uppercase tracking-[0.18em] text-neutral-500">
          Russian A1
        </p>
        <h1 className="mt-2 text-4xl font-bold tracking-tight">Arova</h1>
        <p className="mt-3 text-base leading-7 text-neutral-700">
          Learn useful Russian, understand how it works, speak it, and keep it.
        </p>
      </header>

      <section className="mb-8 rounded-2xl border border-neutral-200 bg-white p-5 shadow-sm">
        <p className="text-xs font-semibold uppercase tracking-[0.15em] text-neutral-500">
          Continue learning
        </p>
        <h2 className="mt-2 text-xl font-semibold">Russian Sounds, Cyrillic & First Conversation</h2>
        <p className="mt-2 text-sm leading-6 text-neutral-600">
          Pareto vocabulary, pronunciation, linguistics, culture, listening and speaking.
        </p>
        <Link
          href="/learn"
          className="mt-4 inline-flex rounded-xl bg-neutral-900 px-4 py-2.5 text-sm font-semibold text-white"
        >
          Continue
        </Link>
      </section>

      <section>
        <h2 className="mb-3 text-lg font-semibold">Arova</h2>
        <div className="grid gap-3 sm:grid-cols-2">
          {navigation.map((item) => (
            <Link
              key={item.title}
              href={item.href}
              className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm transition hover:border-neutral-400"
            >
              <h3 className="font-semibold">{item.title}</h3>
              <p className="mt-1 text-sm leading-5 text-neutral-600">{item.text}</p>
            </Link>
          ))}
        </div>
      </section>
    </main>
  );
}
