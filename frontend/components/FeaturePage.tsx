import Link from "next/link";
import AppNav from "@/components/AppNav";

type Props = {
  eyebrow: string;
  title: string;
  description: string;
  color?: string;
  children?: React.ReactNode;
};

export default function FeaturePage({
  eyebrow,
  title,
  description,
  color = "bg-white",
  children,
}: Props) {
  return (
    <main className="arova-shell">
      <Link href="/" className="text-sm font-bold text-neutral-500">← Arova</Link>
      <section className={`mt-5 rounded-[2rem] border border-[var(--arova-line)] p-6 ${color}`}>
        <p className="arova-kicker text-neutral-500">{eyebrow}</p>
        <h1 className="mt-2 text-4xl font-black tracking-[-0.04em]">{title}</h1>
        <p className="mt-3 max-w-xl leading-7 text-neutral-700">{description}</p>
        {children}
      </section>
      <AppNav />
    </main>
  );
}
