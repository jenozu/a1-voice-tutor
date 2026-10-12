import FeaturePage from "@/components/FeaturePage";


export default function Page() {
  return (
    <FeaturePage eyebrow="Practice" title="Quiz Mode" description="Quick active-recall practice for high-value Russian." color="bg-[var(--arova-yellow)]">
      <div className="mt-6 rounded-3xl bg-white/70 p-5">
        <p className="text-sm font-bold text-neutral-500">Quick question</p>
        <p className="mt-3 text-2xl font-black">What does сегодня mean?</p>
        <div className="mt-5 grid gap-2">
          <div className="rounded-2xl border border-black/10 bg-white p-3 font-bold">today</div>
          <div className="rounded-2xl border border-black/10 bg-white p-3">tomorrow</div>
          <div className="rounded-2xl border border-black/10 bg-white p-3">yesterday</div>
        </div>
      </div>
    </FeaturePage>
  );
}
