# Vosk Model Setup for Polish A1 Voice Tutor

This app now uses Vosk for offline Polish speech recognition.

## How to Set Up the Vosk Polish Model

1. Download the Polish model from the official Vosk models page:
   https://alphacephei.com/vosk/models
   (Recommended: `vosk-model-small-pl-0.22.zip`)

2. Unzip the downloaded model to a directory in your project, e.g.:
   `models/vosk-pl/`

3. The app will use this model for all speech recognition tasks. No API keys or internet connection required!

4. Do NOT commit the model files to GitHub. Add `models/vosk-pl/` to your `.gitignore`.

For more details, see the [Vosk documentation](https://alphacephei.com/vosk/). 