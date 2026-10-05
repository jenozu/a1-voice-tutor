import Link from "next/link";

const areas = [
  ["Sounds & Phonology", "Stress, vowel reduction, palatalization, hard/soft consonants and natural speech."],
  ["Word Structure", "Roots, prefixes, suffixes, endings and reusable word families."],
  ["Cases", "Why Russian uses cases and how endings carry meaning."],
  ["Verbs", "Conjugation, tense, aspect and later verbs of motion."],
  ["Sentence Structure", "Flexible word order, emphasis, negation, questions and agreement."],
  ["Language History", "Optional deeper context on Slavic history and Cyrillic."],
];

export default function LinguisticsPage() {
  return (
    <main className="mx-auto min-h-screen max-w-xl px-5 py-8">
      <Link href="/explore" className="text-sm text-neutral-500">← Explore</Link>
      <p className="mt-6 text-xs font-semibold uppercase tracking-[0.15em] text-neutral-500">Explore</p>
      <h1 className="mt-2 text-3xl font-bold">Linguistics</h1>
      <p className="mt-3 leading-7 text-neutral-600">
        Understand why Russian works the way it does. Concepts appear inside lessons when useful,
        and this library lets you go deeper without interrupting your course.
      </p>
      <div className="mt-6 grid gap-3">
        {areas.map(([title, text]) => (
          <section key={title} className="rounded-2xl border border-neutral-200 bg-white p-4 shadow-sm">
            <h2 className="font-semibold">{title}</h2>
            <p className="mt-1 text-sm leading-6 text-neutral-600">{text}</p>
          </section>
        ))}
      </div>
    </main>
  );
}
