# Arova Product & Feature Architecture

This document locks the feature layout inherited from the original Voice Tutor prototype while the product moves to the new Next.js + FastAPI architecture.

## Product rule

Arova is not a vocabulary-only app. The learning experience combines structured lessons, speaking, listening, reading, writing, linguistics, culture, stories, adaptive review and progress tracking.

The Pareto model determines **what is introduced first and how deeply it is practiced**. It does not remove the broader feature set.

## Primary navigation

### 1. Learn
The structured CEFR course.

Core responsibilities:
- 24 Russian A1 lessons
- adaptive lesson schedule
- Pareto-selected vocabulary and reusable chunks
- grammar in context
- listening, reading, writing and speaking tasks
- embedded linguistics, culture and etymology callouts
- lesson quizzes and mastery checks

### 2. Practice
Skill-focused practice outside the linear course.

Includes:
- Quiz Mode
- Conversation Mode
- Speaking practice
- Listening practice
- Story Mode
- Flashcard Builder
- thematic practice paths
- Ambient Mode later

### 3. Review
Retention and weak-area recovery.

Includes:
- FSRS due reviews
- weak vocabulary
- weak grammar
- weak listening/speaking items
- recently learned items
- failed lesson prompts
- recognition and production review

### 4. Explore
Reference and curiosity-driven learning.

Includes:
- Linguistics
- Culture
- Etymology
- Grammar Reference
- Word Bank

Explore content may be opened directly, but relevant entries must also appear inside lessons when they explain current material.

### 5. Progress
Learner feedback and motivation.

Includes:
- A1 course map
- lesson completion
- vocabulary mastery
- recognition vs production mastery
- speaking time
- listening time
- streak
- XP
- weekly goal
- achievements/badges
- leaderboard later

## Original feature preservation

The following original Voice Tutor features remain part of the product direction:

| Original feature | Arova status |
|---|---|
| Word Bank | Keep |
| Quiz Mode | Keep |
| Conversation Mode | Keep |
| Voice Input / TTS | Keep |
| Spaced Repetition | Keep; FSRS replaces custom scheduler |
| Pronunciation Feedback | Keep with honest ASR limitations |
| Story Mode | Keep |
| Grammar Tips | Keep and embed in lessons |
| Culture Tips | Keep and expand into Explore |
| Thematic Study Paths | Keep |
| Gamification | Keep |
| Goals & Reminders | Keep |
| SMS Integration | Later / optional |
| Word of the Day | Keep |
| Ambient Mode | Later |
| Custom Tutor Voices | Later |
| Linguistics | Promote to first-class module |
| Etymology | Promote to first-class Explore content |

## Lesson anatomy

A complete lesson can contain:

1. lesson goal / scenario
2. Pareto vocabulary and chunks
3. pronunciation or sound focus
4. grammar
5. linguistics explanation
6. culture note
7. etymology note where useful
8. listening
9. reading
10. speaking
11. writing / sentence construction
12. quiz / mastery check
13. FSRS review handoff

Not every lesson needs every section at equal length. Content should appear when it helps explain or use the lesson material.

## Architecture boundary

New product work belongs in:
- `frontend/`
- `backend/`
- `content/`
- `docs/`

The Streamlit prototype remains reference material only.
