# A1 Voice Tutor

Russian A1 mobile-first web app/PWA.

## Current architecture

The active MVP path is:

- `frontend/` — Next.js App Router + TypeScript + Tailwind CSS
- `backend/` — FastAPI + SQLite + Python learning/speech services
- `content/ru/a1/` — versioned Russian A1 curriculum data
- `faster-whisper` — server-side speech-to-text
- browser Speech Synthesis — Russian text-to-speech
- `fsrs` — spaced-repetition scheduling
- VPS deployment — Caddy + Docker Compose after the local vertical slice is working

The original Streamlit/Python prototype is still present as legacy reference while the new vertical slice is built. Do not extend `app.py` or the old CSV-first UI for new MVP features.

## Local development

### Backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Health check: `http://localhost:8000/health`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

Copy `.env.example` to `.env` when local overrides are needed.

## Build order

See `MASTER_PLAN.md`, `PRD.md`, `docs/TECH_STACK.md`, and `docs/MIGRATION_PLAN.md`.
