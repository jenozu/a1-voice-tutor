import FeaturePage from "@/components/FeaturePage";


export default function Page() {
  return (
    <FeaturePage eyebrow="Explore" title="Word Bank" description="A growing library of the high-value words and chunks you encounter." color="bg-white">
      <div className="mt-6 grid gap-2">
        {["сегодня · today","привет · hi","спасибо · thank you","я · I","да · yes"].map((item) => <div key={item} className="rounded-2xl border border-black/10 bg-white p-4 font-bold">{item}</div>)}
      </div>
    </FeaturePage>
  );
}
