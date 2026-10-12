import Link from "next/link";
import AppNav from "@/components/AppNav";

const cards = [
  ["/progress/course","Course progress","Your path through Russian A1.","bg-[var(--arova-pink)]","35%"],
  ["/progress/mastery","Mastery","Recognition and production tracked separately.","bg-[var(--arova-mint)]","2 skills"],
  ["/progress/practice-time","Practice time","Speaking and listening time.","bg-[var(--arova-lilac)]","0 min"],
  ["/progress/goals","Goals","Weekly study target, streak and XP.","bg-[var(--arova-yellow)]","7 day"],
];

export default function ProgressPage() {
  return (
    <main className="arova-shell">
      <Link href="/" className="text-sm font-bold text-neutral-500">← Arova</Link>
      <p className="arova-kicker mt-5 text-neutral-500">Your learning</p>
      <h1 className="mt-1 text-4xl font-black tracking-[-0.04em]">Progress</h1>
      <p className="mt-2 max-w-xl leading-7 text-neutral-600">See what you can actually recognize, produce and use.</p>
      <div className="mt-6 grid gap-3 sm:grid-cols-2">
        {cards.map(([href,title,text,bg,meta]) => (
          <Link key={href} href={href} className={`rounded-[2rem] border border-[var(--arova-line)] p-5 ${bg}`}>
            <div className="flex items-start justify-between gap-3">
              <h2 className="text-xl font-black">{title}</h2>
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
