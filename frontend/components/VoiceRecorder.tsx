"use client";

import { useRef, useState } from "react";
import { apiUrl } from "@/lib/api";

type Props = {
  expectedText?: string;
};

type RecorderState = "idle" | "recording" | "transcribing";

export default function VoiceRecorder({ expectedText }: Props) {
  const [state, setState] = useState<RecorderState>("idle");
  const [transcript, setTranscript] = useState("");
  const [error, setError] = useState("");
  const recorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const streamRef = useRef<MediaStream | null>(null);

  async function startRecording() {
    setError("");
    setTranscript("");

    if (!navigator.mediaDevices?.getUserMedia || typeof MediaRecorder === "undefined") {
      setError("Audio recording is not supported in this browser.");
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      streamRef.current = stream;
      const recorder = new MediaRecorder(stream);
      recorderRef.current = recorder;
      chunksRef.current = [];

      recorder.addEventListener("dataavailable", (event) => {
        if (event.data.size > 0) chunksRef.current.push(event.data);
      });

      recorder.addEventListener("stop", async () => {
        const mimeType = recorder.mimeType || "audio/webm";
        const blob = new Blob(chunksRef.current, { type: mimeType });
        const extension = mimeType.includes("mp4")
          ? "m4a"
          : mimeType.includes("ogg")
            ? "ogg"
            : "webm";

        stream.getTracks().forEach((track) => track.stop());
        streamRef.current = null;
        setState("transcribing");

        try {
          const form = new FormData();
          form.append("file", new File([blob], `speech.${extension}`, { type: mimeType }));
          const response = await fetch(apiUrl("/api/stt/transcribe"), {
            method: "POST",
            body: form,
          });
          const result = await response.json();
          if (!response.ok) throw new Error(result.detail || "Transcription failed.");
          setTranscript(result.text || "No speech detected.");
        } catch (err) {
          setError(err instanceof Error ? err.message : "Transcription failed.");
        } finally {
          setState("idle");
        }
      });

      recorder.start();
      setState("recording");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Microphone access failed.");
      setState("idle");
    }
  }

  function stopRecording() {
    const recorder = recorderRef.current;
    if (recorder && recorder.state === "recording") recorder.stop();
  }

  return (
    <div className="mt-5 rounded-3xl border border-black/10 bg-white/75 p-5">
      <p className="arova-kicker text-neutral-500">Your turn</p>
      {expectedText && (
        <p className="mt-2 text-sm text-neutral-600">
          Say: <span className="font-black text-neutral-900">{expectedText}</span>
        </p>
      )}

      <div className="mt-4 flex flex-wrap gap-2">
        {state === "recording" ? (
          <button type="button" onClick={stopRecording} className="arova-button">
            Stop & transcribe
          </button>
        ) : (
          <button
            type="button"
            onClick={startRecording}
            disabled={state === "transcribing"}
            className="arova-button"
          >
            {state === "transcribing" ? "Whisper is listening…" : "Record my voice"}
          </button>
        )}
      </div>

      {transcript && (
        <div className="mt-4 rounded-2xl bg-[var(--arova-mint)] p-4">
          <p className="text-xs font-black uppercase tracking-[.12em] text-neutral-500">Whisper heard</p>
          <p className="mt-2 text-lg font-black">{transcript}</p>
          <p className="mt-2 text-xs leading-5 text-neutral-600">
            This checks what speech recognition understood; it is not yet a phoneme-level pronunciation score.
          </p>
        </div>
      )}

      {error && <p className="mt-4 text-sm font-bold text-red-700">{error}</p>}
    </div>
  );
}
