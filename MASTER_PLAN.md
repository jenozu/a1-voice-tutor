# Arova MVP Master Plan

## Phase 0 — Foundation
- [x] Select Russian A1 as first course
- [x] Select mobile-first web architecture
- [x] Replace Streamlit direction with Next.js + FastAPI
- [x] Replace Vosk direction with `faster-whisper`
- [x] Select SQLite and FSRS
- [x] Document legacy-code boundaries
- [x] Remove tracked Streamlit secrets file from this branch
- [x] Lock product name: Arova

## Phase 1 — Scaffold
- [x] Create `frontend/` Next.js App Router + TypeScript + Tailwind
- [x] Create `backend/` FastAPI service
- [x] Add `/health` endpoint
- [x] Add SQLite initialization
- [x] Add Russian course content directory
- [x] Add local dev commands

## Task 2 — Pareto learning layer
- [x] Define Pareto-inspired selection policy
- [x] Create 100-item Stage 1 bank: 65 building blocks + 35 conversational chunks
- [x] Split Stage 1 into ten 10-item micro-sessions
- [x] Add active-recall, speaking, recombination and romanization-fade rules
- [x] Add Stage 1/session API endpoints
- [x] Add 80% recognition / 70% production mastery-gate logic
- [ ] Persist per-item attempts and use them to unlock sessions automatically
- [ ] Feed weak/new items into FSRS review

## Task 3 — Lock legacy feature layout into Arova
- [x] Preserve old Voice Tutor feature set as product requirements
- [x] Define Learn / Practice / Review / Explore / Progress navigation
- [x] Promote Linguistics to a first-class Explore module
- [x] Preserve embedded grammar, culture and linguistics inside lessons
- [x] Define dedicated Linguistics content map
- [x] Add initial Arova UI/navigation scaffold
- [ ] Verify frontend production build
- [ ] Verify FastAPI runtime and curriculum endpoints on VPS/local checkout

## Task 4 — First functional learning flow
- [x] Add onboarding screen for target date, study days, time and pace
- [x] Add Relaxed / Standard / Intensive / Custom pace selection
- [x] Generate a 24-lesson study-plan estimate
- [x] Persist learner settings and generated plan in SQLite
- [x] Add functional Learn dashboard
- [x] Add Pareto Session 1 recognition and production practice
- [x] Add embedded Linguistics and Culture cards
- [x] Connect session result to the 80% / 70% mastery gate
- [ ] Persist individual item attempts
- [ ] Unlock Session 2 automatically after mastery
- [ ] Send weak items into FSRS

## Phase 2 — Onboarding and planner
- [x] Collect language, target level/date, study days and available time
- [x] Add Relaxed, Standard, Intensive, and Custom plans
- [x] Generate a weekly schedule estimate across the structured course
- [x] Persist profile and plan
- [x] Allow plan regeneration without deleting progress
- [ ] Add calendar-style weekly schedule UI

## Phase 3 — First complete lesson
- [ ] Define lesson JSON schema including linguistics/culture/etymology objects
- [ ] Build full Lesson 1: Russian Sounds, Cyrillic & First Conversation
- [x] Pull first vocabulary from Pareto Stage 1 data
- [ ] Add grammar
- [x] Add embedded linguistics
- [x] Add culture
- [ ] Add etymology
- [ ] Add listening and reading
- [ ] Add speaking and sentence construction
- [x] Add recognition/production mastery check
- [ ] Save detailed completion progress

## Phase 4 — Voice
- [ ] Add browser microphone recording
- [ ] Add FastAPI audio upload endpoint
- [ ] Integrate `faster-whisper`
- [ ] Add Russian browser TTS
- [ ] Add spoken-answer feedback and retry flow
- [ ] Test on desktop and phone

## Phase 5 — Word bank and review
- [ ] Save lesson vocabulary to learner word bank
- [ ] Integrate FSRS
- [ ] Add Again / Hard / Good / Easy review actions
- [ ] Persist review logs and next-due dates
- [ ] Add weak-skill review beyond vocabulary

## Phase 6 — Practice & Explore expansion
- [ ] Conversation Mode
- [ ] Story Mode
- [ ] Flashcard Builder
- [ ] Linguistics Explore library
- [ ] Culture Explore library
- [ ] Etymology Explore library
- [ ] Grammar Reference
- [ ] Thematic Study Paths
- [ ] Word of the Day

## Phase 7 — Progress & gamification
- [ ] A1 course map
- [ ] skill mastery dashboard
- [ ] speaking/listening time
- [ ] XP and streaks
- [ ] weekly goals
- [ ] badges
- [ ] leaderboard later

## Phase 8 — MVP QA and VPS
- [ ] Test complete onboarding-to-review flow
- [ ] Add mobile responsive polish
- [ ] Add Caddy HTTPS config
- [ ] Add Docker Compose deployment
- [ ] Deploy to VPS
- [ ] Test microphone permissions over HTTPS
- [ ] Test install/add-to-home-screen behavior

## Deferred
- free-form LLM tutor
- advanced phoneme-level pronunciation scoring
- full offline mode
- SMS reminders
- custom tutor personalities/voices
- native iOS/Android apps

## MVP complete when
A learner can open Arova on a phone, create a study plan, finish one complete Russian A1 lesson containing Pareto language plus embedded linguistics/culture, use text and voice practice, save vocabulary, complete an FSRS review, leave, return, and retain progress.
