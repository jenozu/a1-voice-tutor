import FeaturePage from "@/components/FeaturePage";
import SpeakButton from "@/components/SpeakButton";
import VoiceRecorder from "@/components/VoiceRecorder";

export default function Page() {
  return (
    <FeaturePage eyebrow="Practice" title="Speaking" description="Hear natural Russian, then answer with your own voice." color="bg-[var(--arova-lilac)]">
      <div className="mt-6 rounded-3xl bg-white/70 p-5">
        <p className="text-sm font-bold text-neutral-500">Try this</p>
        <p className="mt-3 text-3xl font-black">Привет!</p>
        <p className="mt-1 text-sm font-bold text-neutral-500">privet · hi</p>
        <div className="mt-5 flex flex-wrap gap-2">
          <SpeakButton text="Привет!" label="Normal" />
          <SpeakButton text="Привет!" label="Slow" rate={0.78} className="arova-button-soft" />
        </div>
        <VoiceRecorder expectedText="Привет!" />
      </div>
    </FeaturePage>
  );
}
