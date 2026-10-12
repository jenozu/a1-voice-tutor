import Link from "next/link";
import AppNav from "@/components/AppNav";

const quick = [
  { href: "/practice", title: "Speak", meta: "5 min", bg: "bg-[var(--arova-lilac)]" },
  { href: "/review", title: "Review", meta: "6 due", bg: "bg-[var(--arova-mint)]" },
  { href: "/explore/linguistics", title: "Linguistics", meta: "Learn why", bg: "bg-[var(--arova-yellow)]" },
];

export default function HomePage() {
  return (
    <main className="arova-shell">
      <header className="flex items-start justify-between gap-5">
        <div>
          <p className="arova-kicker text-neutral-500">Russian A1</p>
          <h1 className="mt-1 text-4xl font-black tracking-[-0.04em]">Arova</h1>
        </div>
        <div className="rounded-full bg-white px-3 py-2 text-sm font-bold shadow-sm">7 day streak</div>
      </header>

      <section className="mt-6 overflow-hidden rounded-[2rem] border border-black/5 bg-[var(--arova-pink)] p-6 shadow-[0_20px_55px_rgba(95,50,72,.13)]">
        <div className="flex items-center justify-between gap-4">
          <p className="arova-kicker">Today&apos;s word</p>
          <span className="rounded-full bg-white/70 px-3 py-1 text-xs font-bold">Day 1</span>
        </div>
        <p className="mt-7 text-5xl font-black tracking-tight">сегодня</p>
        <p className="mt-2 text-sm font-bold text-neutral-600">segodnya</p>
        <p className="mt-5 text-2xl font-bold">today</p>
        <div className="mt-6 rounded-2xl bg-white/65 p-4">
          <p className="text-lg font-bold">Сегодня я работаю.</p>
          <p className="mt-1 text-sm text-neutral-600">Today I am working.</p>
        </div>
        <div className="mt-5 flex flex-wrap gap-2">
          <button className="arova-button" type="button">Listen</button>
          <Link className="arova-button-soft" href="/today">Practice this word</Link>
        </div>
      </section>

            <section className="arova-card mt-5 p-5">
        <div className="flex items-center justify-between">
          <p className="arova-kicker text-neutral-500">Continue lesson</p>
          <span className="text-xs font-bold text-neutral-500">10 min</span>
        </div>
        <h2 className="mt-2 text-2xl font-black tracking-tight">Russian Sounds & First Conversation</h2>
        <p className="mt-2 text-sm leading-6 text-neutral-600">Vocabulary · Listening · Linguistics · Speaking</p>
        <div className="mt-5 h-3 overflow-hidden rounded-full bg-neutral-100">
          <div className="h-full w-[35%] rounded-full bg-[var(--arova-pink-deep)]" />
        </div>
        <div className="mt-2 flex justify-between text-xs font-bold text-neutral-500">
          <span>Lesson 1</span><span>35%</span>
        </div>
        <Link href="/learn/session/1" className="arova-button mt-5">Continue lesson</Link>
      </section>

      <section className="mt-5">
        <div className="mb-3 flex items-end justify-between">
          <div>
            <p className="arova-kicker text-neutral-500">Today&apos;s plan</p>
            <h2 className="mt-1 text-2xl font-black">Keep the streak easy.</h2>
          </div>
          <span className="text-sm font-bold">1 / 4</span>
        </div>
        <div className="grid gap-2">
          {[
            ["Daily word", "Done", true],
            ["Lesson", "10 min", false],
            ["Reviews", "6 due", false],
            ["Speaking", "5 min", false],
          ].map(([name, meta, done]) => (
            <div key={name as string} className="flex items-center justify-between rounded-2xl border border-[var(--arova-line)] bg-white px-4 py-3">
              <div className="flex items-center gap-3">
                <span className={`flex h-8 w-8 items-center justify-center rounded-full text-sm font-black ${done ? "bg-[var(--arova-pink)]" : "bg-neutral-100"}`}>
                  {done ? "✓" : "○"}
                </span>
                <span className="font-bold">{name}</span>
              </div>
              <span className="text-sm text-neutral-500">{meta}</span>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-6">
        <p className="arova-kicker text-neutral-500">Jump back in</p>
        <div className="mt-3 grid grid-cols-3 gap-3">
          {quick.map((item) => (
            <Link key={item.title} href={item.href} className={`rounded-3xl p-4 ${item.bg}`}>
              <p className="text-lg font-black">{item.title}</p>
              <p className="mt-8 text-xs font-bold text-neutral-600">{item.meta}</p>
            </Link>
          ))}
        </div>
      </section>

      <AppNav />
    </main>
  );
}
