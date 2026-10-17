# Arova Voice Architecture

## Zero-recurring-cost rule

Arova's core speech stack is self-hosted. The app must not require a paid speech API for its normal learning flow.

- **Text to speech (Arova speaks):** local Piper TTS
- **Speech to text (learner speaks):** local `faster-whisper`
- **Fallback:** browser Speech Synthesis if local TTS is temporarily unavailable
- **Storage:** local disk cache on the VPS

## Local Piper TTS

The backend endpoint is:

`POST /api/tts`

Request:

```json
{"text":"сегодня"}
```

Default Russian voice:

`ru_RU-dmitri-medium`

The first synthesis request automatically downloads the selected Piper voice model and its config into:

`backend/data/piper/`

The default model is roughly 63 MB. This is a one-time model download, not one file per vocabulary word.

Generated speech is stored as WAV in:

`backend/data/tts_cache/`

A cache key includes the voice and exact text, so Arova only synthesizes identical text once.

The frontend supports:
- **Normal** — cached Piper audio at 1.0x
- **Slow** — the same cached audio played at a lower browser playback rate
- **Sentence** — a separate sentence clip generated only when used

Slow mode therefore does not duplicate stored audio.

## Speech recognition

The backend endpoint is:

`POST /api/stt/transcribe`

with multipart form field `file`.

The learner's recording stays within the self-hosted Arova flow and is transcribed with `faster-whisper`.

Default configuration:
- model: `small`
- device: `cpu`
- compute type: `int8`
- language: Russian

The model loads lazily on the first transcription request.

Arova displays the text Whisper understood. This is not presented as validated phoneme-level pronunciation scoring.

## Status endpoint

`GET /api/tts/status`

reports:
- provider
- selected Piper voice
- whether the voice model is already downloaded
- local cache type
- whether a paid API is required

## Limits

- TTS input: 500 characters/request
- STT upload: 8 MB/request
- generated TTS is disk-cached
- Piper model files and audio cache are not committed to Git
- there are no cloud speech credentials to manage

## Voice licensing

Voice models can have licenses that differ from Piper itself. The default `ru_RU-dmitri-medium` model is selected because its current model card identifies its source dataset as CC0. Re-check the model card before major redistribution or commercial release.

## Future

- compare several locally hosted Russian voices for learner preference
- per-user tutor voice selection
- sentence/story pre-generation
- object storage only if the local audio library eventually outgrows the VPS
- pronunciation feedback that separately models phoneme accuracy
