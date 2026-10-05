# Linguistics Module Specification

## Purpose

Linguistics is a first-class Arova feature. It explains **why the language behaves the way it does**, rather than presenting grammar as disconnected rules.

It must exist in two forms:

1. **Embedded linguistics** — short explanations inside lessons when a concept becomes relevant.
2. **Explore > Linguistics** — a browsable reference where learners can go deeper.

## Russian A1 linguistics map

### Sounds & phonology
- Cyrillic sound mapping
- stressed vs unstressed vowels
- vowel reduction
- hard vs soft consonants
- palatalization
- `ь` soft sign
- `ъ` hard sign
- consonant devoicing
- common sound changes in natural speech

### Word structure / morphology
- roots
- prefixes
- suffixes
- endings
- how endings carry grammatical information
- recognizing word families
- why one root can generate many useful words

### Cases
Introduce the concept before memorizing full paradigms.

Explain:
- what a grammatical case is
- why Russian uses cases
- how endings replace information English often expresses through word order/prepositions
- nominative
- accusative
- prepositional
- genitive
- dative
- instrumental

A1 lessons should introduce only the case functions needed for the current material.

### Verbs
- infinitives
- conjugation concept
- subject endings
- present tense
- past tense
- future structures
- aspect as an early conceptual introduction
- imperfective vs perfective
- verbs of motion as a later A1 concept

### Sentence structure
- Russian's relatively flexible word order
- topic and emphasis
- omitted present-tense forms of "to be"
- negation with `не`
- question formation without English-style do/does
- agreement

### Language connections
- Russian within the Slavic language family
- useful cognate/word-family observations
- differences between Russian and English structure
- comparisons only when they genuinely reduce learning effort

### Language history
Optional deeper Explore material:
- Proto-Slavic background
- Old Church Slavonic influence
- historical sound/word connections
- development of Cyrillic

### Etymology
Etymology is linked but separately browsable.

Use it when it makes a word easier to remember, reveals a word family, or explains an otherwise confusing form. Avoid trivia that adds cognitive load without helping the learner.

## Pareto rule for linguistics

Apply the same utility filter used for vocabulary.

Teach concepts early when one concept explains many recurring patterns.

Examples:
- understanding roots + prefixes + suffixes + endings has high leverage
- understanding vowel reduction explains many pronunciation differences
- understanding case as a concept is more useful initially than memorizing six full declension tables

## Content object requirements

Future lesson JSON should support:

```json
{
  "linguistics": [
    {
      "id": "ru-phonology-vowel-reduction",
      "title": "Why unstressed vowels sound different",
      "summary": "...",
      "concept": "vowel_reduction",
      "depth": "lesson",
      "related_items": ["..."],
      "explore_slug": "vowel-reduction"
    }
  ]
}
```

Explore entries can include:
- short explanation
- examples
- audio examples
- visual breakdown
- related lessons
- related vocabulary
- quick check / mini quiz

## UX rule

Linguistics should feel optional-but-useful, not like a textbook detour.

Inside a lesson:
- show a concise card
- allow "Learn why" / "Go deeper"
- return the learner to the lesson afterward

In Explore:
- group concepts by Sounds, Words, Cases, Verbs, Sentences, History
- show which concepts the learner has encountered
- unlock deeper explanations progressively
