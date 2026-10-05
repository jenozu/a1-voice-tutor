# Arova — Russian A1 MVP PRD

## Product goal
Build a mobile-first language-learning app for complete beginners studying Russian A1, with a strong speaking/listening focus, a structured CEFR course, and deeper explanations of how the language works. The app must work in normal mobile/desktop browsers and be self-hostable on the existing VPS.

## Product identity
Arova is broader than a voice tutor or vocabulary trainer. The product combines:
- structured lessons
- adaptive scheduling
- Pareto-prioritized language
- speaking and listening
- reading and writing
- linguistics
- grammar
- culture
- etymology
- stories
- FSRS review
- progress and gamification

The legacy Voice Tutor feature set is preserved in `docs/FEATURE_ARCHITECTURE.md`.

## Primary navigation
- **Learn** — 24-lesson A1 course
- **Practice** — quiz, conversation, speaking, listening, stories and flashcards
- **Review** — FSRS and weak-area recovery
- **Explore** — linguistics, culture, etymology, grammar reference and word bank
- **Progress** — course map, mastery, XP, streaks and goals

## MVP must-have
- onboarding with target date, study days, minutes/day or hours/week, and preset pace
- dynamic study plan that can be regenerated without losing completed work
- structured Russian A1 lessons stored as data, not hard-coded UI
- Pareto-inspired curriculum ordering that prioritizes high-utility, highly recombinable language
- Cyrillic plus temporary early transliteration support
- vocabulary, grammar, linguistics, culture, listening, reading, writing, and speaking practice
- browser microphone capture
- Russian STT with `faster-whisper`
- browser TTS for Russian playback
- text and voice quizzes
- persistent word bank
- FSRS review deck
- learner progress, XP, streak, and weak-skill tracking
- embedded linguistics/culture/etymology cards with links to deeper Explore content
- one complete end-to-end lesson before expanding the curriculum

## Pareto curriculum rule
Stage 1 is a 100-item survival core made from 65 reusable building blocks and 35 conversational chunks. The app introduces 10 items per micro-session, immediately recombines new material with known material, and uses active recall plus speaking rather than passive rereading.

Default progression gate:
- recognition >= 80%
- production >= 70%

Passing the gate unlocks the next micro-session while weak items remain in spaced review. The curriculum is utility-prioritized; it must not be described as a literal corpus-frequency "top 100" list.

Pareto logic also applies to grammar and linguistics: teach high-leverage concepts early when they explain many recurring patterns.

## First vertical slice
Onboarding → generated plan → Lesson 1/Pareto Session 1 → linguistics/culture callout → listening → spoken response → transcription → quiz → word-bank update → FSRS review → saved progress.

## Lesson 1 target
**Russian Sounds, Cyrillic & First Conversation**

Include:
- first Pareto vocabulary/chunks
- greetings and introductions
- yes/no and negation
- formal/informal address
- Cyrillic/sound introduction
- one high-leverage linguistics concept
- one pronunciation concept
- one cultural note
- one useful etymology/word-family note
- listening
- speaking
- text quiz
- progress save

## Full product features retained
- Word Bank
- Quiz Mode
- Conversation Mode
- Voice Input / TTS
- Spaced Repetition
- Pronunciation Feedback
- Story Mode
- Grammar Tips
- Culture Tips
- Linguistics Module
- Etymology
- Thematic Study Paths
- Gamification
- Goals & Reminders
- Word of the Day
- Flashcard Builder
- Ambient Mode (later)
- SMS Integration (optional/later)
- Custom Tutor Voices (later)
- Leaderboards (later)

## Product principles
- Keep the architecture language-agnostic, dependencies minimal, and core learning features usable without a paid API.
- Teach fewer items more deeply: hear, say, recognize, recall, recombine, review.
- Prefer words, chunks and concepts that can be reused across many future lessons.
- Use romanization as a temporary bridge, not a permanent dependency.
- Linguistics explains recurring patterns; it is not trivia or a detached textbook.
- Culture and etymology should improve understanding or memory rather than interrupt flow.
- Speech transcription quality is not the same as pronunciation quality; MVP feedback may score phrase correctness and provide targeted pronunciation tips, but must not present ASR text similarity as validated phoneme scoring.
