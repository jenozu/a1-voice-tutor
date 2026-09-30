# Migration Plan

## Goal
Move from the existing Polish/Streamlit prototype to the Russian mobile-first web MVP without losing useful ideas or extending obsolete architecture.

## Reuse after review
- quiz concepts and question types
- XP/streak behavior
- goal-tracking concepts
- story-mode concepts
- word-bank fields
- cultural-tip/grammar-tip ideas

## Replace
- Streamlit UI → Next.js
- Polish content → Russian A1 content
- Vosk → `faster-whisper`
- `pyttsx3` → browser Speech Synthesis for MVP
- custom familiarity scheduler → `py-fsrs`
- CSV user/progress writes → SQLite
- monolithic `app.py` flow → frontend routes + FastAPI services

## Do not port into the first vertical slice
- Ambient Mode thread loop
- OpenAI helper/API dependency
- Twilio SMS
- public leaderboard
- custom tutor personalities
- advanced pronunciation scores

## Planned new structure

`frontend/` — Next.js/TypeScript UI

`backend/` — FastAPI, SQLite, speech, quiz/SRS services

`content/ru/a1/` — lessons, vocabulary, stories, culture, linguistics, etymology

`docs/` — canonical product and architecture decisions

## Build order
1. Scaffold frontend and backend.
2. Add SQLite schema and local learner profile.
3. Implement onboarding and schedule generator.
4. Define lesson JSON schema.
5. Build one complete Russian lesson.
6. Add quiz attempt logging and word-bank writes.
7. Integrate FSRS review scheduling.
8. Add microphone capture and `faster-whisper` transcription.
9. Add browser Russian TTS.
10. Test the full vertical slice on desktop and phone.
11. Deploy behind HTTPS on the VPS.
12. Only then expand lessons and standalone culture/linguistics/etymology sections.

## Definition of first MVP
A user can create a local profile, receive a personalized plan, finish one complete Russian A1 lesson using text and voice, save vocabulary, review it later through FSRS, and return without losing progress.
