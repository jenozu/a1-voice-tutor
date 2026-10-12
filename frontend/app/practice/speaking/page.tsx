import FeaturePage from "@/components/FeaturePage";
import SpeakButton from "@/components/SpeakButton";

export default function Page() {
  return (
    <FeaturePage eyebrow="Practice" title="Speaking" description="Start with a useful phrase, hear it, then say it back." color="bg-[var(--arova-lilac)]">
      <div className="mt-6 rounded-3xl bg-white/70 p-5">
        <p className="text-sm font-bold text-neutral-500">Try this</p>
        <p className="mt-3 text-3xl font-black">Привет!</p>
        <p className="mt-1 text-sm font-bold text-neutral-500">privet · hi</p>
        <div className="mt-5 flex flex-wrap gap-2"><SpeakButton text="Привет!" /><span className="arova-button-soft">Say it aloud</span></div>
      </div>
    </FeaturePage>
  );
}
