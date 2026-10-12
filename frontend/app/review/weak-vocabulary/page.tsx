import FeaturePage from "@/components/FeaturePage";


export default function Page() {
  return (
    <FeaturePage eyebrow="Review" title="Weak vocabulary" description="Words with low recognition or production will collect here." color="bg-[var(--arova-yellow)]">
      <div className="mt-6 rounded-2xl bg-white/70 p-4 text-sm leading-6 text-neutral-700">This screen is now wired into navigation. The learning logic for it is the next implementation step.</div>
    </FeaturePage>
  );
}
