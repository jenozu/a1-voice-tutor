import FeaturePage from "@/components/FeaturePage";
import SpeakButton from "@/components/SpeakButton";

export default function Page() {
  return (
    <FeaturePage eyebrow="Practice" title="Listening" description="Hear a short Russian phrase and connect the sound to meaning." color="bg-[var(--arova-pink)]">
      <div className="mt-6 rounded-3xl bg-white/70 p-5">
        <p className="text-sm font-bold text-neutral-500">Listen first</p>
        <SpeakButton text="Как дела?" label="Play Russian" className="arova-button mt-4" />
        <p className="mt-5 text-sm leading-6 text-neutral-700">After listening, say what you think it means before revealing or continuing.</p>
      </div>
    </FeaturePage>
  );
}
