from __future__ import annotations

import tempfile
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .config import settings
from .content import stage_1_session, stage_1_summary
from .db import get_settings, init_db, save_settings
from .pareto import mastery_status
from .planner import build_plan
from .stt import transcribe
from .tts import status as tts_runtime_status
from .tts import synthesize


MAX_TTS_CHARS = 500
MAX_STT_BYTES = 8 * 1024 * 1024


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Arova API",
    version="0.5.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(settings.cors_origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MasteryCheck(BaseModel):
    recognition_percent: float = Field(ge=0, le=100)
    production_percent: float = Field(ge=0, le=100)


class LearnerSettings(BaseModel):
    language: str = "Russian"
    target_level: str = "A1"
    target_date: str | None = None
    study_days: list[str] = []
    minutes_per_day: int = Field(default=25, ge=5, le=240)
    pace: str = Field(default="standard", pattern="^(relaxed|standard|intensive|custom)$")


class TTSRequest(BaseModel):
    text: str = Field(min_length=1, max_length=MAX_TTS_CHARS)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.app_env}


@app.get("/api/profile")
def profile() -> dict[str, object]:
    stored = get_settings()
    return {"configured": stored is not None, "profile": stored}


@app.post("/api/profile")
def update_profile(payload: LearnerSettings) -> dict[str, object]:
    plan = build_plan(
        target_date=payload.target_date,
        study_days=payload.study_days,
        minutes_per_day=payload.minutes_per_day,
        pace=payload.pace,
    )
    stored = save_settings(
        language=payload.language,
        target_level=payload.target_level,
        target_date=payload.target_date,
        study_days=payload.study_days,
        minutes_per_day=payload.minutes_per_day,
        pace=payload.pace,
        plan=plan,
    )
    return {"configured": True, "profile": stored}


@app.get("/api/tts/status")
def tts_status() -> dict[str, object]:
    return tts_runtime_status()


@app.post("/api/tts")
def text_to_speech(payload: TTSRequest) -> FileResponse:
    try:
        path, cache_hit = synthesize(payload.text)
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Local TTS failed: {exc}") from exc

    return FileResponse(
        path,
        media_type="audio/wav",
        filename="arova-speech.wav",
        headers={"X-Arova-TTS-Cache": "HIT" if cache_hit else "MISS"},
    )


@app.post("/api/stt/transcribe")
async def speech_to_text(file: UploadFile = File(...)) -> dict[str, object]:
    content = await file.read(MAX_STT_BYTES + 1)
    if len(content) > MAX_STT_BYTES:
        raise HTTPException(status_code=413, detail="Audio file is too large.")

    suffix = Path(file.filename or "speech.webm").suffix or ".webm"
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temporary:
            temporary.write(content)
            temporary_path = Path(temporary.name)

        result = await run_in_threadpool(transcribe, temporary_path, "ru")
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Transcription failed: {exc}") from exc
    finally:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink(missing_ok=True)


@app.get("/api/courses/ru-a1/stage-1")
def get_stage_1() -> dict[str, object]:
    return stage_1_summary()


@app.get("/api/courses/ru-a1/stage-1/sessions/{session_number}")
def get_stage_1_session(session_number: int) -> dict[str, object]:
    if session_number < 1 or session_number > 10:
        raise HTTPException(status_code=404, detail="Stage 1 session not found")
    try:
        return stage_1_session(session_number)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Stage 1 session not found") from exc


@app.post("/api/courses/ru-a1/stage-1/mastery")
def check_stage_1_mastery(payload: MasteryCheck) -> dict[str, object]:
    return mastery_status(payload.recognition_percent, payload.production_percent)
