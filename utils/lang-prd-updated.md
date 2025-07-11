
# Product Requirements Document — Polish A1 Voice Tutor (v2.0)

| Item           | Detail                          |
|----------------|----------------------------------|
| **Owner**      | Andel O’Bryan                    |
| **Date**       | 7 July 2025                      |
| **Status**     | v2 — Comprehensive feature spec  |

---

## 1. Problem Statement

A1-level Polish learners struggle to retain vocabulary, pronounce accurately, and engage in natural conversation. Existing apps lack robust free voice features and often don’t adapt to real learner progress or needs.

---

## 2. Goals & Success Metrics

| Goal                          | Metric                                                         |
|-------------------------------|----------------------------------------------------------------|
| Efficient vocab acquisition   | ≥ 80% of 200-word bank marked “Known ≥ 7” within 4 weeks       |
| Real speech practice          | ≥ 15 min conversation / week; pronunciation score avg ≥ 80%    |
| Habit building                | 7+ day streaks for 65% of weekly active users                  |
| Timely review & retention     | SRS-driven recall improves score by ≥ 25% across 2 cycles      |
| Daily microlearning           | ≥ 70% open rate on Word of the Day and quiz reminder features  |

---

## 3. Target Users

- CEFR A0–A1 adult learners using “Polish for Dummies” or “Po Polsku 1”
- Self-taught learners, expats, and casual polyglots
- Age 16–45; interested in practical spoken Polish

---

## 4. Core Features

| #   | Feature                       | Description |
|-----|-------------------------------|-------------|
| 4.1 | Word Bank                     | 200+ A1 words w/ definitions, examples, audio, tags, and familiarity scores |
| 4.2 | Quiz Mode                     | Multiple-choice, fill-in-the-blank, open-ended (typed or spoken), with instant feedback |
| 4.3 | Conversation Mode             | Role-play dialogs by theme (café, intro, travel) with voice-enabled turns |
| 4.4 | Voice Input / TTS             | Respond via mic; app reads questions, prompts, or full conversations aloud |
| 4.5 | Spaced Repetition Review     | Automatically reschedules words for review using time-weighted familiarity |
| 4.6 | Pronunciation Feedback        | Scores user audio using Whisper or wav2vec2; shows accuracy and feedback |
| 4.7 | Story Mode                    | Short, graded Polish stories with comprehension quizzes and voice interaction |
| 4.8 | Grammar & Culture Tips        | Bite-sized context tips triggered during quiz or conversation |
| 4.9 | Thematic Study Paths          | Words, quizzes, and dialogues grouped by theme (e.g. Food, Family, Travel) |
| 4.10| Gamification                  | XP points, badge achievements, leaderboard (weekly reset), streak tracker |
| 4.11| Goals & Reminders             | Set study goals (e.g., 3x/week); daily reminder popups or SMS |
| 4.12| SMS Integration               | Optional: receive reminder SMS at chosen time (Twilio-powered) |
| 4.13| Word of the Day               | New word shown daily with audio, usage, and theme tag |
| 4.14| Ambient Mode                  | Auto-play audio dialogs that pause for user response — ideal for driving or walking |
| 4.15| Custom Tutor Voices           | Choose from voice personalities (“Tutor Magda”, “Coach Piotr”) for AI guidance |

---

## 5. User Journey (v2 Flow)

1. Home dashboard shows Word of the Day, current streak, progress bar to goal
2. Choose between: Quiz, Conversation, Story Mode, or Review
3. During quizzes: wrong answers trigger grammar tips or review tagging
4. After conversations: receive pronunciation score + option to retry
5. Optional: user receives SMS at their chosen time encouraging daily practice

---

## 6. Tech Stack

- **Frontend**: Streamlit
- **Voice I/O**: SpeechRecognition, pyttsx3, Whisper
- **Reminders**: Twilio API (for SMS)
- **Gamification**: Custom XP/badge engine
- **Persistence**: CSV for users/words/conversations or SQLite (future)
- **ML scoring**: Whisper ASR / Wav2Vec2 (local or hosted)

---

## 7. Future Considerations

- Web app auth for multi-device sync
- Push notification integration (desktop/mobile)
- Branching story dialogs
- Avatar or assistant creator
