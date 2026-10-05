import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Arova",
    short_name: "Arova",
    description: "Learn languages through speaking, understanding, and intelligent review.",
    start_url: "/",
    display: "standalone",
    background_color: "#f7f7f5",
    theme_color: "#111827",
  };
}
