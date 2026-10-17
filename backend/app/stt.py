from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

from faster_whisper import WhisperModel

from .config import settings


@lru_cache(maxsize=1)
def whisper_model() -> WhisperModel:
    return WhisperModel(
        settings.whisper_model,
        device=settings.whisper_device,
        compute_type=settings.whisper_compute_type,
    )


def transcribe(audio_path: Path, language: str = "ru") -> dict[str, Any]:
    model = whisper_model()
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        vad_filter=True,
        condition_on_previous_text=False,
    )
    text = " ".join(segment.text.strip() for segment in segments if segment.text.strip()).strip()
    return {
        "text": text,
        "language": getattr(info, "language", language),
        "language_probability": float(getattr(info, "language_probability", 0.0)),
    }
