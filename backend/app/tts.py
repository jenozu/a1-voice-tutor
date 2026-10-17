from __future__ import annotations

import hashlib
import logging
import threading
import wave
from functools import lru_cache
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from piper import PiperVoice

from .config import settings


LOGGER = logging.getLogger(__name__)
_DOWNLOAD_LOCK = threading.Lock()
_SYNTHESIS_LOCK = threading.Lock()


def _backend_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = Path(__file__).resolve().parents[1] / path
    return path


def cache_directory() -> Path:
    path = _backend_path(settings.tts_cache_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def model_directory() -> Path:
    path = _backend_path(settings.piper_model_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def _voice_parts() -> tuple[str, str, str]:
    try:
        locale, name, quality = settings.piper_voice.split("-", maxsplit=2)
    except ValueError as exc:
        raise RuntimeError(
            "PIPER_VOICE must look like 'ru_RU-dmitri-medium'."
        ) from exc
    return locale, name, quality


def model_path() -> Path:
    return model_directory() / f"{settings.piper_voice}.onnx"


def config_path() -> Path:
    return model_directory() / f"{settings.piper_voice}.onnx.json"


def model_downloaded() -> bool:
    return (
        model_path().exists()
        and model_path().stat().st_size > 0
        and config_path().exists()
        and config_path().stat().st_size > 0
    )


def _voice_url(filename: str) -> str:
    locale, name, quality = _voice_parts()
    language_family = locale.split("_", maxsplit=1)[0]
    base = settings.piper_voice_repo.rstrip("/")
    return (
        f"{base}/{language_family}/{locale}/{name}/{quality}/{filename}"
        "?download=true"
    )


def _download_file(url: str, destination: Path) -> None:
    temporary = destination.with_suffix(destination.suffix + ".part")
    request = Request(url, headers={"User-Agent": "Arova/1.0"})

    try:
        with urlopen(request, timeout=120) as response, temporary.open("wb") as output:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)
    except HTTPError as exc:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(
            f"Could not download Piper voice (HTTP {exc.code})."
        ) from exc
    except URLError as exc:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(
            f"Could not download Piper voice: {exc.reason}"
        ) from exc

    if not temporary.exists() or temporary.stat().st_size == 0:
        temporary.unlink(missing_ok=True)
        raise RuntimeError("Downloaded Piper voice file was empty.")

    temporary.replace(destination)


def ensure_voice_files() -> tuple[Path, Path]:
    if model_downloaded():
        return model_path(), config_path()

    with _DOWNLOAD_LOCK:
        if model_downloaded():
            return model_path(), config_path()

        model = model_path()
        config = config_path()
        LOGGER.info("Downloading Piper voice %s", settings.piper_voice)

        if not model.exists() or model.stat().st_size == 0:
            _download_file(_voice_url(model.name), model)

        if not config.exists() or config.stat().st_size == 0:
            _download_file(_voice_url(config.name), config)

        return model, config


@lru_cache(maxsize=1)
def piper_voice() -> PiperVoice:
    model, _ = ensure_voice_files()
    LOGGER.info("Loading Piper voice %s", model)
    return PiperVoice.load(model)


def _cache_key(text: str) -> str:
    material = "|".join(
        [
            "piper",
            settings.piper_voice,
            text.strip(),
        ]
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def cached_audio_path(text: str) -> Path:
    return cache_directory() / f"{_cache_key(text)}.wav"


def synthesize(text: str) -> tuple[Path, bool]:
    clean_text = text.strip()
    if not clean_text:
        raise ValueError("Text cannot be empty.")

    output_path = cached_audio_path(clean_text)
    if output_path.exists() and output_path.stat().st_size > 44:
        return output_path, True

    with _SYNTHESIS_LOCK:
        if output_path.exists() and output_path.stat().st_size > 44:
            return output_path, True

        voice = piper_voice()
        temporary = output_path.with_suffix(".tmp.wav")

        try:
            with wave.open(str(temporary), "wb") as wav_file:
                voice.synthesize_wav(clean_text, wav_file)
        except Exception:
            temporary.unlink(missing_ok=True)
            raise

        if not temporary.exists() or temporary.stat().st_size <= 44:
            temporary.unlink(missing_ok=True)
            raise RuntimeError("Piper produced no playable audio.")

        temporary.replace(output_path)
        return output_path, False


def status() -> dict[str, object]:
    return {
        "provider": "piper-local",
        "configured": True,
        "voice": settings.piper_voice,
        "model_downloaded": model_downloaded(),
        "audio_format": "wav",
        "cache": "disk",
        "paid_api_required": False,
    }
