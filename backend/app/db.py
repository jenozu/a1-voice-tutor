from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from .config import settings


SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS learner_profile (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    target_date TEXT,
    study_days_json TEXT NOT NULL DEFAULT '[]',
    minutes_per_day INTEGER,
    pace TEXT NOT NULL DEFAULT 'standard',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS learner_settings (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    language TEXT NOT NULL DEFAULT 'Russian',
    target_level TEXT NOT NULL DEFAULT 'A1',
    target_date TEXT,
    study_days_json TEXT NOT NULL DEFAULT '[]',
    minutes_per_day INTEGER,
    pace TEXT NOT NULL DEFAULT 'standard',
    plan_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lesson_progress (
    lesson_id TEXT PRIMARY KEY,
    status TEXT NOT NULL DEFAULT 'not_started',
    score REAL,
    completed_at TEXT,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS word_progress (
    item_id TEXT PRIMARY KEY,
    recognition_score REAL NOT NULL DEFAULT 0,
    production_score REAL NOT NULL DEFAULT 0,
    exposure_count INTEGER NOT NULL DEFAULT 0,
    last_seen_at TEXT,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


def database_path() -> Path:
    path = Path(settings.database_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parents[1] / path
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def connect() -> sqlite3.Connection:
    connection = sqlite3.connect(database_path())
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys=ON")
    return connection


def init_db() -> None:
    with connect() as connection:
        connection.executescript(SCHEMA)


def save_settings(
    *,
    language: str,
    target_level: str,
    target_date: str | None,
    study_days: list[str],
    minutes_per_day: int,
    pace: str,
    plan: dict[str, Any],
) -> dict[str, Any]:
    with connect() as connection:
        connection.execute(
            """
            INSERT INTO learner_settings (
                id, language, target_level, target_date, study_days_json,
                minutes_per_day, pace, plan_json, updated_at
            )
            VALUES (1, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(id) DO UPDATE SET
                language = excluded.language,
                target_level = excluded.target_level,
                target_date = excluded.target_date,
                study_days_json = excluded.study_days_json,
                minutes_per_day = excluded.minutes_per_day,
                pace = excluded.pace,
                plan_json = excluded.plan_json,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                language,
                target_level,
                target_date,
                json.dumps(study_days),
                minutes_per_day,
                pace,
                json.dumps(plan),
            ),
        )
        connection.commit()
    return get_settings() or {}


def get_settings() -> dict[str, Any] | None:
    with connect() as connection:
        row = connection.execute("SELECT * FROM learner_settings WHERE id = 1").fetchone()
    if row is None:
        return None
    return {
        "language": row["language"],
        "target_level": row["target_level"],
        "target_date": row["target_date"],
        "study_days": json.loads(row["study_days_json"] or "[]"),
        "minutes_per_day": row["minutes_per_day"],
        "pace": row["pace"],
        "plan": json.loads(row["plan_json"] or "{}"),
    }
