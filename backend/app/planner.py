from __future__ import annotations

import math
from datetime import date
from typing import Any


PACE_DEFAULTS = {
    "relaxed": {"minutes": 15, "days": 3},
    "standard": {"minutes": 25, "days": 4},
    "intensive": {"minutes": 35, "days": 6},
}


def build_plan(
    *,
    target_date: str | None,
    study_days: list[str],
    minutes_per_day: int | None,
    pace: str,
) -> dict[str, Any]:
    normalized_pace = pace.lower()
    defaults = PACE_DEFAULTS.get(normalized_pace, PACE_DEFAULTS["standard"])

    days_per_week = len(study_days) or defaults["days"]
    minutes = minutes_per_day or defaults["minutes"]
    weekly_minutes = days_per_week * minutes

    # A full lesson is estimated at ~35 focused minutes. This is planning guidance,
    # not a mastery requirement; actual advancement is controlled by learner performance.
    lesson_equivalents_per_week = max(1, round(weekly_minutes / 35))
    estimated_weeks = math.ceil(24 / lesson_equivalents_per_week)

    target_weeks = None
    recommended_minutes = minutes
    if target_date:
        try:
            target = date.fromisoformat(target_date)
            delta_days = max(1, (target - date.today()).days)
            target_weeks = max(1, math.ceil(delta_days / 7))
            required_lesson_equivalents = 24 / target_weeks
            recommended_minutes = max(
                10,
                math.ceil((required_lesson_equivalents * 35) / max(1, days_per_week) / 5) * 5,
            )
        except ValueError:
            target_weeks = None

    return {
        "course": "Russian A1",
        "total_lessons": 24,
        "pace": normalized_pace,
        "study_days": study_days,
        "days_per_week": days_per_week,
        "minutes_per_day": minutes,
        "weekly_minutes": weekly_minutes,
        "lesson_equivalents_per_week": lesson_equivalents_per_week,
        "estimated_weeks": estimated_weeks,
        "target_weeks": target_weeks,
        "recommended_minutes_per_day_for_target": recommended_minutes,
        "first_step": {
            "lesson": 1,
            "title": "Russian Sounds, Cyrillic & First Conversation",
            "pareto_session": 1,
        },
    }
