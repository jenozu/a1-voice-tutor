import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Arova",
    short_name: "Arova",
    description: "Learn languages through speaking, understanding, and intelligent review.",
    start_url: "/",
    display: "standalone",
    background_color: "#fffafc",
    theme_color: "#ffd8e8",
  };
}
