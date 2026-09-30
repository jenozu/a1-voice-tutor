# Pareto Learning Model

## Purpose

The app should optimize for useful Russian, not for completing the largest possible vocabulary list.

"Pareto" here means prioritizing the relatively small set of words, chunks and sentence-building tools that unlock a disproportionate amount of beginner comprehension and speaking. It does **not** mean claiming that exactly 20% of Russian literally equals 80% fluency.

## Stage 1 composition

Stage 1 contains 100 high-value items:

- 65 reusable building blocks: pronouns, question words, particles, connectors, core verbs and prepositions
- 35 conversational chunks: introductions, repair phrases, needs, wants, possession, preferences and practical social language

The selection is utility-first rather than a strict corpus-frequency ranking.

## Learning loop

Each micro-session introduces 10 new items. The learner should:

1. understand the meaning;
2. hear the Russian;
3. say it aloud;
4. recognize the Cyrillic;
5. recall it from English without looking;
6. recombine it in multiple tiny sentences or dialogue turns;
7. send weak items to spaced review.

Do not introduce 20 new items at once. Ten is the default; later the planner may reduce the batch when review load is high.

## Active recall

Recognition alone is not enough. The app should alternate:

- Russian → meaning;
- English → Russian;
- audio → meaning;
- prompt → spoken response;
- fill a missing word/chunk;
- build a new sentence from known pieces.

Use a five-second recall rule in quick drills. If a learner cannot produce the answer promptly, mark it for review rather than treating slow recognition as mastery.

## Mastery gate

Default Stage 1 progression:

- recognition: at least 80%
- production: at least 70%

A learner who passes advances while weak items remain in FSRS review. Do not require 100% before introducing the next session.

## Recombination

New vocabulary should immediately reuse old vocabulary. A 10-item session should generate many combinations rather than 10 isolated flashcards.

Example progression:

- Я хочу...
- Я хочу кофе.
- Я не хочу...
- Что ты хочешь?
- Я тоже хочу...

The app should prefer material that can be reused across many future prompts.

## Romanization

Romanization is a bridge:

- Sessions 1–3: visible by default
- Sessions 4–6: hint only
- Sessions 7–10: hidden by default

Cyrillic remains visible from day one.

## Speaking-first rule

Every session must contain spoken production. STT transcription can check whether the intended phrase was captured, but it must not be labeled as validated phoneme-level pronunciation scoring.

## SRS

Weak and newly learned items enter FSRS review. The learning path determines what is introduced; FSRS determines when previously introduced material should return.

## Canonical data

The new Stage 1 source is `content/ru/a1/stage_1_pareto.json`. Older files under `curriculum/russian/` and `data/russian_stage_1.json` are migration references, not the canonical MVP curriculum.
