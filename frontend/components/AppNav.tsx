import Link from "next/link";

const items = [
  ["/learn", "Learn", "L"],
  ["/practice", "Practice", "P"],
  ["/review", "Review", "R"],
  ["/explore", "Explore", "E"],
  ["/progress", "Progress", "G"],
];

export default function AppNav() {
  return (
    <nav className="arova-bottom-nav" aria-label="Primary navigation">
      {items.map(([href, label, glyph]) => (
        <Link key={href} href={href}>
          <span className="mx-auto mb-1 flex h-7 w-7 items-center justify-center rounded-full bg-white text-[11px] shadow-sm">
            {glyph}
          </span>
          {label}
        </Link>
      ))}
    </nav>
  );
}
