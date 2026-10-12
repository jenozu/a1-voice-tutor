import FeaturePage from "@/components/FeaturePage";


export default function Page() {
  return (
    <FeaturePage eyebrow="Practice" title="Flashcards" description="Focused decks for vocabulary you want to strengthen." color="bg-white">
      <div className="mt-6 rounded-3xl bg-[var(--arova-pink)] p-6 text-center">
        <p className="text-4xl font-black">сегодня</p>
        <p className="mt-2 text-sm font-bold text-neutral-600">Tap-through decks will connect to FSRS next.</p>
      </div>
    </FeaturePage>
  );
}
