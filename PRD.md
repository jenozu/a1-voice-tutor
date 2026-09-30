# Russian A1 Voice Tutor — MVP PRD

## Product goal
Build a mobile-first web app for complete beginners studying Russian A1, with a strong speaking/listening focus and an exam-oriented curriculum. The app must work in normal mobile/desktop browsers and be self-hostable on the existing VPS.

## MVP must-have
- onboarding with target date, study days, minutes/day or hours/week, and preset pace
- dynamic study plan that can be regenerated without losing completed work
- structured Russian A1 lessons stored as data, not hard-coded UI
- Pareto-inspired curriculum ordering that prioritizes high-utility, highly recombinable language
- Cyrillic plus optional early transliteration support
- vocabulary, grammar, listening, reading, writing, and speaking practice
- browser microphone capture
- Russian STT with `faster-whisper`
- browser TTS for Russian playback
- text and voice quizzes
- persistent word bank
- FSRS review deck
- learner progress, XP, streak, and weak-skill tracking
- cultural, linguistics, and etymology callouts inside lessons
- one complete end-to-end lesson before expanding the curriculum

## Pareto curriculum rule

Stage 1 is a 100-item survival core made from 65 reusable building blocks and 35 conversational chunks. The app introduces 10 items per micro-session, immediately recombines new material with known material, and uses active recall plus speaking rather than passive rereading.

Default progression gate:
- recognition >= 80%
- production >= 70%

Passing the gate unlocks the next micro-session while weak items remain in spaced review. The curriculum is utility-prioritized; it must not be described as a literal corpus-frequency "top 100" list.

## First vertical slice
Onboarding → generated plan → Pareto Session 1 → listening → spoken response → transcription → quiz → word-bank update → FSRS review → saved progress.

## Lesson 1 target
Russian Sounds, Cyrillic & First Conversation. Include greetings, yes/no, thanks, introductions, formal/informal address, one pronunciation concept, one cultural note, one linguistics note, and one etymology note. Use the Stage 1 Pareto bank as the vocabulary source.

## Deferred until after the vertical slice
- free-form LLM tutor
- leaderboard/multi-user social features
- SMS reminders
- native iOS/Android apps
- advanced phoneme-level pronunciation scoring
- full offline mode
- all 24 lessons fully authored

## Product principles
- Keep the architecture language-agnostic, dependencies minimal, and core learning features usable without a paid API.
- Teach fewer items more deeply: hear, say, recognize, recall, recombine, review.
- Prefer words and chunks that can be reused across many future sentences.
- Use romanization as a temporary bridge, not a permanent dependency.
- Speech transcription quality is not the same as pronunciation quality; MVP feedback may score phrase correctness and provide targeted pronunciation tips, but must not present ASR text similarity as validated phoneme scoring.
