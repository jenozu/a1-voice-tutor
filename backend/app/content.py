from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
STAGE_1_PATH = REPO_ROOT / "content" / "ru" / "a1" / "stage_1_pareto.json"


@lru_cache(maxsize=1)
def load_stage_1() -> dict[str, Any]:
    with STAGE_1_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def stage_1_summary() -> dict[str, Any]:
    data = load_stage_1()
    return {
        "language": data["language"],
        "level": data["level"],
        "stage": data["stage"],
        "title": data["title"],
        "selection_model": data["selection_model"],
        "mastery_gate": data["mastery_gate"],
        "romanization_policy": data["romanization_policy"],
        "sessions": data["sessions"],
    }


def stage_1_session(session_number: int) -> dict[str, Any]:
    data = load_stage_1()
    session = next(
        (entry for entry in data["sessions"] if entry["number"] == session_number),
        None,
    )
    if session is None:
        raise KeyError(session_number)

    wanted = set(session["item_ids"])
    items_by_id = {item["id"]: item for item in data["items"]}
    ordered_items = [items_by_id[item_id] for item_id in session["item_ids"] if item_id in wanted]

    return {
        **session,
        "items": ordered_items,
        "teaching_cycle": data["teaching_cycle"],
        "practice_rules": data["practice_rules"],
        "mastery_gate": data["mastery_gate"],
    }
