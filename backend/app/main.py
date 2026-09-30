from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .config import settings
from .content import stage_1_session, stage_1_summary
from .db import init_db
from .pareto import mastery_status


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="A1 Voice Tutor API",
    version="0.2.0",
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


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.app_env}


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
