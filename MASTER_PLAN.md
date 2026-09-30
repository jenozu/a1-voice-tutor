# MVP Master Plan

## Phase 0 — Foundation
- [x] Select Russian A1 as first course
- [x] Select mobile-first web architecture
- [x] Replace Streamlit direction with Next.js + FastAPI
- [x] Replace Vosk direction with `faster-whisper`
- [x] Select SQLite and `py-fsrs`
- [x] Document legacy-code boundaries
- [x] Remove tracked Streamlit secrets file from this branch

## Phase 1 — Scaffold
- [x] Create `frontend/` Next.js App Router + TypeScript + Tailwind
- [x] Create `backend/` FastAPI service
- [x] Add `/health` endpoint
- [x] Add SQLite initialization
- [x] Add Russian course content directory
- [x] Add local dev commands

## Task 2 — Pareto learning layer
- [x] Define a Pareto-inspired selection policy without claiming a literal corpus top-100
- [x] Create a 100-item Stage 1 bank: 65 building blocks + 35 conversational chunks
- [x] Split Stage 1 into ten 10-item micro-sessions
- [x] Add active-recall, speaking, recombination and romanization-fade rules
- [x] Add Stage 1/session API endpoints
- [x] Add 80% recognition / 70% production mastery-gate logic
- [ ] Persist per-item attempts and use them to unlock sessions automatically
- [ ] Feed weak/new items into FSRS review

## Phase 2 — Onboarding and planner
- [ ] Collect target date, study days, minutes/day or hours/week
- [ ] Add Relaxed, Standard, Intensive, and Custom plans
- [ ] Generate a weekly schedule
- [ ] Persist profile and plan
- [ ] Allow regeneration without losing completed work

## Phase 3 — First complete lesson
- [ ] Define lesson JSON schema
- [ ] Build Lesson 1: Russian Sounds, Cyrillic & First Conversation
- [ ] Add vocabulary and grammar
- [ ] Add listening and reading
- [ ] Add culture, linguistics, and etymology callouts
- [ ] Add text quiz
- [ ] Save completion progress

## Phase 4 — Voice
- [ ] Add browser microphone recording
- [ ] Add FastAPI audio upload endpoint
- [ ] Integrate `faster-whisper`
- [ ] Add Russian browser TTS
- [ ] Add spoken-answer feedback and retry flow
- [ ] Test on desktop and phone

## Phase 5 — Word bank and review
- [ ] Save lesson vocabulary to learner word bank
- [ ] Integrate `py-fsrs`
- [ ] Add Again / Hard / Good / Easy review actions
- [ ] Persist review logs and next-due dates

## Phase 6 — MVP QA and VPS
- [ ] Test complete onboarding-to-review flow
- [ ] Add mobile responsive polish
- [ ] Add Caddy HTTPS config
- [ ] Add Docker Compose deployment
- [ ] Deploy to VPS
- [ ] Test microphone permissions over HTTPS
- [ ] Test install/add-to-home-screen behavior

## MVP complete when
A learner can open the web app on a phone, create a study plan, finish one complete Russian A1 lesson with text and voice, save vocabulary, complete an FSRS review, leave, return, and retain progress.
