import Link from "next/link";
import AppNav from "@/components/AppNav";

const options = [
  ["/review/due","Due reviews","Practice the items Arova wants to bring back now.","bg-[var(--arova-pink)]","6 due"],
  ["/review/weak-vocabulary","Weak vocabulary","Focus on words with low recognition or production.","bg-[var(--arova-yellow)]","Focus"],
  ["/review/weak-skills","Weak skills","See where grammar, listening and speaking need attention.","bg-[var(--arova-lilac)]","Skills"],
];

export default function ReviewPage() {
  return (
    <main className="arova-shell">
      <Link href="/" className="text-sm font-bold text-neutral-500">← Arova</Link>
      <p className="arova-kicker mt-5 text-neutral-500">Remember more</p>
      <h1 className="mt-1 text-4xl font-black tracking-[-0.04em]">Review</h1>
      <p className="mt-2 max-w-xl leading-7 text-neutral-600">
        This will become your FSRS-powered memory queue. For now, every section is navigable and ready for the next data layer.
      </p>
      <div className="mt-6 grid gap-3">
        {options.map(([href,title,text,bg,meta]) => (
          <Link key={href} href={href} className={`rounded-[2rem] border border-[var(--arova-line)] p-5 ${bg}`}>
            <div className="flex items-start justify-between gap-4">
              <h2 className="text-2xl font-black">{title}</h2>
              <span className="rounded-full bg-white/70 px-3 py-1 text-xs font-bold">{meta}</span>
            </div>
            <p className="mt-3 text-sm leading-6 text-neutral-700">{text}</p>
            <p className="mt-7 text-xs font-black uppercase tracking-[.14em]">Open →</p>
          </Link>
        ))}
      </div>
      <AppNav />
    </main>
  );
}
