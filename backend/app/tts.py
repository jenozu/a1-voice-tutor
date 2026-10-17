from __future__ import annotations

import hashlib
import html
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .config import settings


def _backend_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = Path(__file__).resolve().parents[1] / path
    return path


def cache_directory() -> Path:
    path = _backend_path(settings.tts_cache_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def is_configured() -> bool:
    return bool(settings.azure_speech_key and settings.azure_speech_region)


def _cache_key(text: str) -> str:
    material = "|".join(
        [
            "azure",
            settings.azure_speech_region,
            settings.azure_tts_voice,
            settings.azure_tts_output_format,
            text.strip(),
        ]
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def cached_audio_path(text: str) -> Path:
    return cache_directory() / f"{_cache_key(text)}.mp3"


def synthesize(text: str) -> tuple[Path, bool]:
    clean_text = text.strip()
    if not clean_text:
        raise ValueError("Text cannot be empty.")
    if not is_configured():
        raise RuntimeError("Azure Speech is not configured.")

    output_path = cached_audio_path(clean_text)
    if output_path.exists() and output_path.stat().st_size > 0:
        return output_path, True

    escaped_text = html.escape(clean_text)
    escaped_voice = html.escape(settings.azure_tts_voice, quote=True)
    ssml = (
        "<speak version='1.0' xml:lang='ru-RU'>"
        f"<voice name='{escaped_voice}'>{escaped_text}</voice>"
        "</speak>"
    )

    url = (
        f"https://{settings.azure_speech_region}."
        "tts.speech.microsoft.com/cognitiveservices/v1"
    )
    request = Request(
        url,
        data=ssml.encode("utf-8"),
        method="POST",
        headers={
            "Ocp-Apim-Subscription-Key": settings.azure_speech_key,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": settings.azure_tts_output_format,
            "User-Agent": "Arova",
        },
    )

    try:
        with urlopen(request, timeout=20) as response:
            audio = response.read()
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Azure Speech returned HTTP {exc.code}: {detail[:300]}") from exc
    except URLError as exc:
        raise RuntimeError(f"Azure Speech could not be reached: {exc.reason}") from exc

    if not audio:
        raise RuntimeError("Azure Speech returned an empty audio response.")

    temporary = output_path.with_suffix(".tmp")
    temporary.write_bytes(audio)
    temporary.replace(output_path)
    return output_path, False
