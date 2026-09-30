# Tech Stack — Russian A1 MVP

## Chosen stack

| Layer | Choice | Why |
|---|---|---|
| Frontend | Next.js App Router + TypeScript | Responsive mobile/web UI with a clean path to PWA features |
| Styling | Tailwind CSS | Small, flexible styling layer; no UI kit required for MVP |
| Backend | FastAPI | Keeps Python for speech and learning logic while exposing a simple API |
| Speech-to-text | `faster-whisper` | Current Whisper implementation with lower memory use and faster inference than base Whisper |
| TTS | Browser Speech Synthesis | Zero server dependency for MVP; use `ru-RU` voices when available |
| Database | SQLite | Single-file persistence suited to a small self-hosted MVP |
| SRS | `py-fsrs` | Maintained open-source FSRS implementation instead of a custom scheduler |
| Lesson content | JSON | Easy to validate, version, author, and later localize |
| VPS edge | Caddy | Simple HTTPS and reverse proxy |
| Deployment | Docker Compose | Reproducible VPS deployment without orchestration overhead |

## PWA strategy
Start as a responsive web app. Add a web-app manifest immediately. Add service-worker/offline caching only when needed; use Serwist rather than an older PWA wrapper if a library is required.

## Speech defaults
Use `faster-whisper` on the FastAPI service. Default to a configurable CPU-friendly model such as `small` with INT8 for the first VPS test. Increase model size only after measuring latency and memory on the actual VPS.

## Keep out of the MVP
- Streamlit
- Vosk
- `openai-whisper`
- `pyttsx3`
- mandatory OpenAI or other paid LLM APIs
- Twilio
- Redis/Celery
- Postgres
- Kubernetes
- LangChain/LlamaIndex
- native mobile frameworks

## Minimal backend dependencies
- FastAPI
- Uvicorn
- `python-multipart`
- `faster-whisper`
- `fsrs`
- Pydantic

Use Python standard-library SQLite initially rather than adding an ORM before the schema proves it needs one.

## Important boundary
`faster-whisper` is for transcription. It must not be presented as a validated pronunciation scorer. Pronunciation feedback in the MVP should combine transcript correctness, retries, known Russian pronunciation rules, and listen/repeat guidance. Advanced phoneme scoring is a later feature.
