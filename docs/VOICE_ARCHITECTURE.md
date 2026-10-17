# Arova Voice Architecture

## Direction

Arova treats speech output and speech input as separate systems:

- **Text to speech (Arova speaks):** Azure Speech neural TTS
- **Speech to text (learner speaks):** local `faster-whisper`
- **Fallback:** browser Speech Synthesis only when neural TTS is unavailable

## Neural TTS

The backend endpoint is:

`POST /api/tts`

Request:

```json
{"text":"сегодня"}
```

The Azure key never goes to the browser. The backend generates MP3 audio, stores it under the configured TTS cache directory, and returns the cached file on later requests for the same text/voice/output-format combination.

Default voice:

`ru-RU-SvetlanaNeural`

Default output:

`audio-24khz-48kbitrate-mono-mp3`

The frontend provides normal and slow playback. Slow mode changes browser playback rate, so it does not create or store a duplicate audio file.

## Speech recognition

The backend endpoint is:

`POST /api/stt/transcribe`

with multipart form field `file`.

The model loads lazily on the first transcription request. Default configuration:

- model: `small`
- device: `cpu`
- compute type: `int8`
- language: Russian

Arova displays the text Whisper understood. This is **not** presented as phoneme-level pronunciation scoring.

## Limits

- TTS input: 500 characters/request
- STT upload: 8 MB/request
- TTS audio is disk-cached
- TTS credentials remain server-side

## Future

- per-user tutor voice preference
- sentence and story pre-generation
- object-storage/CDN cache when the library becomes large
- pronunciation feedback that separately models phoneme accuracy
