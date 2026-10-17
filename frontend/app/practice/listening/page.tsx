import FeaturePage from "@/components/FeaturePage";
import SpeakButton from "@/components/SpeakButton";

export default function Page() {
  return (
    <FeaturePage eyebrow="Practice" title="Listening" description="Hear natural Russian at normal or learner-friendly speed." color="bg-[var(--arova-pink)]">
      <div className="mt-6 rounded-3xl bg-white/70 p-5">
        <p className="text-sm font-bold text-neutral-500">Listen first</p>
        <div className="mt-4 flex flex-wrap gap-2">
          <SpeakButton text="Как дела?" label="Normal" />
          <SpeakButton text="Как дела?" label="Slow" rate={0.78} className="arova-button-soft" />
        </div>
        <p className="mt-5 text-sm leading-6 text-neutral-700">
          Listen before reading the answer. Slow mode reuses the same cached neural audio and changes playback speed in the browser.
        </p>
      </div>
    </FeaturePage>
  );
}
