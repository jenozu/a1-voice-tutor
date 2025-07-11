
# 🇵🇱 Polish A1 Voice Tutor

A voice-first Polish study companion designed to help learners reach CEFR A1 fluency faster. Built with **Streamlit**, this app combines a smart word bank, adaptive quizzes, daily speaking practice, and gamified habit tracking — all powered by AI voice interaction.

---

## ✨ Features Overview

| Area | What You Get |
|------|--------------|
| 🎙️ **Conversation Mode** | Speak with an AI tutor across themed scenarios (café, intro, shopping). The app plays its part, listens to yours, and gives feedback. |
| 🧠 **Spaced Repetition Review** | Words appear for review based on forgetting curve and familiarity rating. |
| 🎧 **Pronunciation Feedback** | Your voice is scored for clarity and accuracy using Whisper or Wav2Vec2. |
| 🧪 **Voice Quizzes** | Quiz formats include multiple choice, sentence fill-ins, translations — all answerable by voice or keyboard. |
| 📚 **Live Word Bank** | Browse or search all 200+ core A1 words. Add custom entries, sort by theme or “Needs Review.” |
| ✍️ **Story Mode** | Short Polish stories with voice narration and comprehension questions. |
| 💬 **Grammar & Culture Tips** | Mini-notes appear when needed — irregular verbs, cultural context, polite forms. |
| 🧩 **Thematic Study Paths** | Group content by Travel, Family, Food, etc. Progress badges unlock for each. |
| 🏅 **Gamification** | Earn XP and badges, maintain a streak, and climb weekly leaderboards. |
| 📆 **Daily Goals & Word of the Day** | Track goals (e.g. 5 quizzes/week) and see a new Polish word each day. |
| 📲 **Reminders & SMS Support** | Set study reminders by time — delivered via popup or optional SMS (Twilio). |
| 🚗 **Ambient Mode** | Auto-play conversation that pauses for your reply — ideal for passive practice. |
| 🗣️ **Custom Tutor Voices** | Choose from multiple AI personalities and TTS voices for your virtual guide. |

---

## 🧩 Tech Stack

- **App**: Python + Streamlit
- **Voice Recognition**: Google STT (default), Whisper/Wav2Vec2 (optional)
- **Text-to-Speech**: pyttsx3 (offline), gTTS (online fallback)
- **SMS API**: Twilio
- **Data Storage**: CSV (local dev); upgrade to SQLite or Firestore for scale

---

## 📂 Folder Structure

```
/polish_voice_tutor/
├── app.py
├── data/
│   ├── word_bank.csv
│   ├── stories.csv
│   ├── grammar_tips.json
│   ├── culture_notes.json
│   ├── users.csv
│   └── leaderboard.csv
├── utils/
│   ├── srs_engine.py
│   ├── pronunciation.py
│   ├── quiz_generator.py
│   ├── story_mode.py
│   ├── xp_badges.py
│   ├── sms_reminder.py
│   ├── grammar_tipper.py
│   ├── culture_tip.py
│   └── voice_io.py
```

---

## 🛠️ Getting Started

1. Clone repo and install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Launch the app:
   ```
   streamlit run app.py
   ```

3. Optional: set up Twilio credentials in `.env`:
   ```
   TWILIO_SID=...
   TWILIO_AUTH=...
   TWILIO_PHONE=+1xxx...
   ```

4. Add your own CSVs (or use starter files in `/data/`).

---

## 📬 Questions?

Open an issue, or contact Andel O’Bryan. Contributions welcome!
