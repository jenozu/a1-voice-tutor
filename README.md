# Arova

Arova is a mobile-first language-learning app. Russian A1 is the first course.

The product preserves the original Voice Tutor feature vision while moving to a lean web architecture and a Pareto-first learning model.

## Product structure

- **Learn** — structured 24-lesson A1 course
- **Practice** — speaking, listening, quizzes, stories and flashcards
- **Review** — FSRS and weak-area recovery
- **Explore** — linguistics, culture, etymology, grammar reference and word bank
- **Progress** — mastery, course map, XP, streaks and goals

Linguistics is a first-class feature and also appears inside lessons when it explains the material being learned.

See:
- `PRD.md`
- `MASTER_PLAN.md`
- `docs/FEATURE_ARCHITECTURE.md`
- `docs/LINGUISTICS.md`
- `docs/PARETO_LEARNING.md`
- `docs/TECH_STACK.md`

## Active architecture

- `frontend/` — Next.js App Router + TypeScript + Tailwind
- `backend/` — FastAPI + SQLite + Python learning/speech services
- `content/ru/a1/` — canonical Russian A1 curriculum data
- `faster-whisper` — speech-to-text
- browser Speech Synthesis — text-to-speech
- FSRS — spaced repetition
- VPS deployment — Caddy + Docker Compose after verification

The original Streamlit/Python prototype remains in the repository as migration/reference material. Do not add new product features to `app.py`.
