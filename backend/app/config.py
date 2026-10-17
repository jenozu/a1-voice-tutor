from __future__ import annotations

import os
from dataclasses import dataclass


def _csv_env(name: str, default: str) -> tuple[str, ...]:
    raw = os.getenv(name, default)
    return tuple(value.strip() for value in raw.split(",") if value.strip())


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    database_path: str = os.getenv("DATABASE_PATH", "./data/a1_voice_tutor.sqlite3")
    cors_origins: tuple[str, ...] = _csv_env("CORS_ORIGINS", "http://localhost:3000")

    # Speech-to-text: local faster-whisper
    whisper_model: str = os.getenv("WHISPER_MODEL", "small")
    whisper_device: str = os.getenv("WHISPER_DEVICE", "cpu")
    whisper_compute_type: str = os.getenv("WHISPER_COMPUTE_TYPE", "int8")

    # Text-to-speech: local Piper. No API key or paid service required.
    piper_voice: str = os.getenv("PIPER_VOICE", "ru_RU-dmitri-medium")
    piper_model_dir: str = os.getenv("PIPER_MODEL_DIR", "./data/piper")
    piper_voice_repo: str = os.getenv(
        "PIPER_VOICE_REPO",
        "https://huggingface.co/rhasspy/piper-voices/resolve/main",
    )
    tts_cache_dir: str = os.getenv("TTS_CACHE_DIR", "./data/tts_cache")


settings = Settings()
