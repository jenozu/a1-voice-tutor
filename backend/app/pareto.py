from __future__ import annotations


RECOGNITION_TARGET = 80.0
PRODUCTION_TARGET = 70.0


def mastery_status(recognition_percent: float, production_percent: float) -> dict[str, object]:
    recognition_passed = recognition_percent >= RECOGNITION_TARGET
    production_passed = production_percent >= PRODUCTION_TARGET
    advance = recognition_passed and production_passed

    weak_areas: list[str] = []
    if not recognition_passed:
        weak_areas.append("recognition")
    if not production_passed:
        weak_areas.append("production")

    return {
        "advance": advance,
        "recognition_passed": recognition_passed,
        "production_passed": production_passed,
        "weak_areas": weak_areas,
        "targets": {
            "recognition_percent": RECOGNITION_TARGET,
            "production_percent": PRODUCTION_TARGET,
        },
    }
