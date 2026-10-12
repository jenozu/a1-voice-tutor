import Link from "next/link";
import AppNav from "@/components/AppNav";

const options = [
  ["/practice/speaking","Speaking","Conversation and spoken-response practice.","bg-[var(--arova-lilac)]","5 min"],
  ["/practice/listening","Listening","Audio recognition and comprehension.","bg-[var(--arova-pink)]","5 min"],
  ["/practice/quiz","Quiz Mode","Recognition, production, fill-in and open response.","bg-[var(--arova-yellow)]","Quick"],
  ["/practice/story","Story Mode","Graded stories with comprehension and voice interaction.","bg-[var(--arova-mint)]","Read"],
  ["/practice/flashcards","Flashcards","Build and review focused decks.","bg-white","Review"],
];

export default function PracticePage() {
  return (
    <main className="arova-shell">
      <Link href="/" className="text-sm font-bold text-neutral-500">← Arova</Link>
      <p className="arova-kicker mt-5 text-neutral-500">Train a skill</p>
      <h1 className="mt-1 text-4xl font-black tracking-[-0.04em]">Practice</h1>
      <p className="mt-2 max-w-xl leading-7 text-neutral-600">
        Pick one thing to work on without losing your place in the course.
      </p>
      <div className="mt-6 grid gap-3 sm:grid-cols-2">
        {options.map(([href,title,text,bg,meta],i) => (
          <Link key={href} href={href} className={`rounded-[2rem] border border-[var(--arova-line)] p-5 transition hover:-translate-y-0.5 ${bg} ${i===0 ? "sm:col-span-2" : ""}`}>
            <div className="flex items-start justify-between gap-4">
              <h2 className="text-2xl font-black">{title}</h2>
              <span className="rounded-full bg-white/70 px-3 py-1 text-xs font-bold">{meta}</span>
            </div>
            <p className="mt-3 text-sm leading-6 text-neutral-700">{text}</p>
            <p className="mt-8 text-xs font-black uppercase tracking-[.14em]">Open →</p>
          </Link>
        ))}
      </div>
      <AppNav />
    </main>
  );
}
