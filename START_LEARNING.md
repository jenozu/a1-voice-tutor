# Getting Started: Learn with the Voice Tutor

This project runs as a local Streamlit app. Follow these steps to
launch it and start practicing.

## 1) Install prerequisites
- Python 3.10+ and pip
- A working microphone and speakers (optional, for voice features)

## 2) Set up your environment
From the repo root:

```
python -m venv .venv
source .venv/bin/activate
pip install -r utils/requirements.txt
```

## 3) Launch the app
```
streamlit run app.py
```

Then open the URL shown in your terminal (usually
http://localhost:8501).

## 4) First-time usage inside the app
1. On the Home page, click "Start Onboarding".
2. Use the left sidebar to move between sections:
   - Word Bank: browse and search vocabulary
   - Quiz Mode: quick practice with feedback
   - Conversation Practice: speak or type responses
   - Story Mode: read and answer questions
   - Review Deck: spaced repetition review
   - Settings: set your daily goal and voice preferences

## 5) A simple daily routine (10 to 15 minutes)
1. Review the Word of the Day on Home.
2. Do 1 to 2 quizzes in Quiz Mode.
3. Spend 3 to 5 minutes in Conversation Practice or Story Mode.
4. Finish with the Review Deck.

## Optional: SMS reminders
The Settings page includes SMS reminders. To enable real SMS sending,
you will need Twilio credentials in your environment. If you do not
set them, you can still use the app normally.

## Troubleshooting
- If the microphone does not work, check browser permissions and try
  text input where available.
- If the app does not load data, confirm the "data/" folder exists
  and contains the CSV/JSON files from this repo.
