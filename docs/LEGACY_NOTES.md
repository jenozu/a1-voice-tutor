# Legacy Notes

The original Python/Streamlit prototype remains in the repository temporarily so useful behavior can be referenced during migration.

Do not build new MVP features in:
- `app.py`
- the old Streamlit UI
- Vosk/pyttsx3 code paths
- CSV-based learner progress flows

The active implementation lives in `frontend/`, `backend/`, and `content/`.

For Russian curriculum specifically, `content/ru/a1/stage_1_pareto.json` is canonical. The older `curriculum/russian/stage_1.md` and `data/russian_stage_1.json` are retained only as migration references.
