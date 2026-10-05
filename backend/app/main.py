from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .config import settings
from .content import stage_1_session, stage_1_summary
from .db import get_settings, init_db, save_settings
from .pareto import mastery_status
from .planner import build_plan


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Arova API",
    version="0.3.0",
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
