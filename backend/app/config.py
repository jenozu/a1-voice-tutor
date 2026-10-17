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

    # Text-to-speech: Azure Speech. The key stays server-side.
    azure_speech_key: str = os.getenv("AZURE_SPEECH_KEY", "")
    azure_speech_region: str = os.getenv("AZURE_SPEECH_REGION", "")
    azure_tts_voice: str = os.getenv("AZURE_TTS_VOICE", "ru-RU-SvetlanaNeural")
    azure_tts_output_format: str = os.getenv(
        "AZURE_TTS_OUTPUT_FORMAT",
        "audio-24khz-48kbitrate-mono-mp3",
    )
    tts_cache_dir: str = os.getenv("TTS_CACHE_DIR", "./data/tts_cache")


settings = Settings()
