# Backend

Lean FastAPI service for the Russian A1 MVP.

## Run

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The SQLite database is created automatically on startup. Runtime database files are ignored by Git.

`faster-whisper` is intentionally included as the STT engine, but model loading/transcription is added in the voice phase so the health endpoint and core API remain fast during foundation work.
