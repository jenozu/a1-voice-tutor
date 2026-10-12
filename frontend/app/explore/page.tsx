import Link from "next/link";
import AppNav from "@/components/AppNav";

const cards = [
  ["/explore/linguistics","Linguistics","Why Russian works the way it does.","bg-[var(--arova-yellow)]"],
  ["/explore/culture","Culture","Context that changes how real Russian sounds and feels.","bg-[var(--arova-pink)]"],
  ["/explore/etymology","Etymology","Word origins and families that actually help memory.","bg-[var(--arova-lilac)]"],
  ["/explore/grammar","Grammar","A reference connected back to what you have learned.","bg-[var(--arova-mint)]"],
  ["/explore/word-bank","Word Bank","Your growing collection of learned and upcoming Russian.","bg-white"],
];

export default function ExplorePage() {
  return (
    <main className="arova-shell">
      <Link href="/" className="text-sm font-bold text-neutral-500">← Arova</Link>
      <p className="arova-kicker mt-5 text-neutral-500">Go deeper</p>
      <h1 className="mt-1 text-4xl font-black tracking-[-0.04em]">Explore</h1>
      <p className="mt-2 leading-7 text-neutral-600">The part of Arova that explains the language instead of asking you to memorize it blindly.</p>
      <div className="mt-6 grid gap-3 sm:grid-cols-2">
        {cards.map(([href,title,text,bg],i) => (
          <Link key={title} href={href} className={`rounded-[2rem] border border-[var(--arova-line)] p-5 ${bg} ${i===0 ? "sm:col-span-2" : ""}`}>
            <p className="text-2xl font-black">{title}</p>
            <p className="mt-3 text-sm leading-6 text-neutral-700">{text}</p>
            <p className="mt-8 text-xs font-black uppercase tracking-[.14em]">Open →</p>
          </Link>
        ))}
      </div>
      <AppNav />
    </main>
  );
}
