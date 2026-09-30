import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "A1 Voice Tutor",
    short_name: "A1 Tutor",
    description: "Russian A1 speaking and listening practice",
    start_url: "/",
    display: "standalone",
    background_color: "#f7f7f5",
    theme_color: "#111827",
  };
}
