import FeaturePage from "@/components/FeaturePage";


export default function Page() {
  return (
    <FeaturePage eyebrow="Practice" title="Story Mode" description="Short graded stories will combine known vocabulary with comprehension." color="bg-[var(--arova-mint)]">
      <div className="mt-6 rounded-3xl bg-white/70 p-5">
        <p className="text-sm font-bold text-neutral-500">Mini story preview</p>
        <p className="mt-3 text-xl font-black">Сегодня я дома. Я пью кофе.</p>
        <p className="mt-3 text-sm leading-6 text-neutral-700">Today I am at home. I am drinking coffee.</p>
      </div>
    </FeaturePage>
  );
}
