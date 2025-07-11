
## Todo List for Polish A1 Voice Tutor App

- [ ] **Phase 1: Analyze requirements and set up project structure**
  - [x] Read and understand `pasted_content.txt`
  - [x] Read and understand `lang-readme-updated.md`
  - [x] Read and understand `lang-prd-updated.md`
  - [x] Create `polish_voice_tutor` directory
  - [x] Create `data` and `utils` subdirectories
  - [x] Create `requirements.txt`
  - [x] Create dummy data files in `/data`
  - [x] Create empty utility modules in `/utils`
  - [x] Create `app.py` with basic Streamlit structure

- [x] **Phase 2: Implement core Streamlit app with basic UI**
  - [x] Implement Home dashboard with Word of the Day, Streak tracker, Daily goal progress
  - [x] Implement tabs or sidebar for navigation (Word Bank, Quiz Mode, Conversation Practice, Story Mode, Review Deck, Settings)
  - [x] Set up basic UI for each section

- [x] **Phase 3: Integrate voice recognition and text-to-speech features**
  - [x] Implement `voice_io.py` for handling all voice input/output
  - [x] Integrate Whisper/Google STT for speech recognition
  - [x] Integrate pyttsx3/gTTS for text-to-speech

- [ ] **Phase 4: Implement lesson content and interactive exercises**
  - [ ] Implement `srs_engine.py` for spaced repetition logic
  - [ ] Implement `quiz_generator.py` for smart quiz builder
  - [ ] Implement `story_mode.py` for graded stories with Q&A
  - [ ] Implement `pronunciation.py` for speech scoring with feedback
  - [ ] Implement `grammar_tipper.py` and `culture_tip.py` for injecting tips

- [ ] **Phase 5: Add progress tracking and user interface enhancements**
  - [ ] Implement `xp_badges.py` for tracking XP, badges, and streaks
  - [ ] Implement `goals.py` for daily/weekly goal tracking
  - [ ] Implement gamification logic (XP, badges, leaderboard)
  - [ ] Implement Word of the Day system
  - [ ] Implement Custom AI Tutor Voices selection
  - [ ] Implement `sms_reminder.py` for optional SMS via Twilio
  - [ ] Implement `ambient_mode.py` for continuous conversation with auto-pause

- [ ] **Phase 6: Test the application and deploy**
  - [ ] Test all features with mock data
  - [ ] Ensure modularity and clean code
  - [ ] Prepare for deployment
  - [ ] Deploy the application
  - [ ] Deliver the outcome to the user


