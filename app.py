import streamlit as st
import pandas as pd
import json
from datetime import date, datetime
import random

# Placeholder for utility functions
from utils.quiz_generator import (
    generate_multiple_choice_quiz,
    generate_fill_in_blank_quiz,
    evaluate_answer,
    log_quiz_result
)
from utils.srs_engine import (
    get_words_for_review,
    update_familiarity
)
from utils.pronunciation import evaluate_pronunciation
from utils.xp_badges import add_xp, update_streak, check_for_badges
from utils.goals import set_goal, get_goal, update_goal_progress, check_goal_completion
from utils.leaderboard import get_leaderboard
from utils.grammar_tipper import get_grammar_tip
from utils.culture_tip import get_culture_tip
from utils.story_mode import evaluate_story_answer
from utils.ambient_mode import start_ambient_mode, stop_ambient_mode, is_ambient_active
from utils import voice_io
from utils import sms_reminder

st.set_page_config(page_title="Polish A1 Voice Tutor", page_icon="🇵🇱", layout="wide")

# --- Load Data (Dummy) ---
@st.cache_data
def load_data():
    word_bank = pd.read_csv('data/word_bank.csv')
    users = pd.read_csv('data/users.csv')
    quiz_log = pd.read_csv('data/quiz_log.csv')
    stories = pd.read_csv('data/stories.csv')
    leaderboard = pd.read_csv('data/leaderboard.csv')
    with open('data/grammar_tips.json', 'r') as f:
        grammar_tips = json.load(f)
    with open('data/culture_notes.json', 'r') as f:
        culture_notes = json.load(f)
    return word_bank, users, quiz_log, stories, leaderboard, grammar_tips, culture_notes

word_bank, users, quiz_log, stories, leaderboard, grammar_tips, culture_notes = load_data()

# --- Session State Initialization ---
if 'current_user' not in st.session_state:
    st.session_state.current_user = users.iloc[0] # Load first user as default
if 'word_of_the_day' not in st.session_state:
    st.session_state.word_of_the_day = word_bank.sample(1).iloc[0]
if 'daily_goal' not in st.session_state:
    st.session_state.daily_goal = 5
if 'daily_progress' not in st.session_state:
    st.session_state.daily_progress = 0

# --- Header ---
st.title("🇵🇱 Polish A1 Voice Tutor")

# --- Sidebar Navigation ---
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", ["Home", "Word Bank", "Quiz Mode", "Conversation Practice", "Story Mode", "Review Deck", "Leaderboard", "Settings"])

# --- Home Page ---
if page == "Home":
    if 'onboarded' not in st.session_state or not st.session_state['onboarded']:
        st.header("👋 Welcome to Polish A1 Voice Tutor!")
        st.write("This app will help you practice Polish with voice, quizzes, stories, and more. Let's get started!")
        if st.button("Start Onboarding"):
            st.session_state['onboarded'] = True
            st.balloons()
            st.success("You're all set! Use the sidebar to explore features.")
        st.stop()
    st.header("Welcome, " + st.session_state.current_user['username'] + "!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Current Streak", value=f"{st.session_state.current_user['streak']} days")
    with col2:
        st.metric(label="Total XP", value=st.session_state.current_user['xp'])
    with col3:
        progress_text = f"{st.session_state.daily_progress}/{st.session_state.daily_goal} Quizzes"
        st.metric(label="Daily Goal Progress", value=progress_text)
    st.progress(min(st.session_state.daily_progress / st.session_state.daily_goal, 1.0), text="Daily Goal Progress")

    st.subheader("Word of the Day")
    wotd = st.session_state.word_of_the_day
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(f"**{wotd['word']}** ({wotd['translation']})")
        st.write(f"Example: *{wotd['example']}*")
        st.write(f"Tags: {wotd['tags']}")
    with col2:
        if st.button("🔊 Play Audio"):
            # Generate TTS for the word and example
            tts_text = f"{wotd['word']}. {wotd['example']}"
            audio_file = voice_io.text_to_speech(tts_text)
            if audio_file:
                voice_io.play_audio_streamlit(audio_file)
            else:
                st.info("Audio playback not available")
        if st.button("📚 Add to Review"):
            st.success("Added to review deck!")

    st.markdown("---")
    st.subheader("Grammar Tip of the Day")
    st.info(get_grammar_tip(None))
    st.subheader("Culture Note of the Day")
    st.info(get_culture_tip(None))
    st.subheader("Quick Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎯 Start a Quick Quiz", use_container_width=True):
            st.session_state.page = "Quiz Mode"
            st.rerun()
    with col2:
        if st.button("💬 Practice Conversation", use_container_width=True):
            st.session_state.page = "Conversation Practice"
            st.rerun()

# --- Word Bank Page ---
elif page == "Word Bank":
    st.header("Word Bank")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        tag_filter = st.selectbox("Filter by Tag", ["All"] + list(word_bank['tags'].unique()))
    with col2:
        familiarity_filter = st.selectbox("Filter by Familiarity", ["All", "Needs Review (≤3)", "Learning (4-6)", "Known (≥7)"])
    with col3:
        search_term = st.text_input("Search words")

    # Apply filters
    filtered_words = word_bank.copy()
    if tag_filter != "All":
        filtered_words = filtered_words[filtered_words['tags'] == tag_filter]
    if familiarity_filter == "Needs Review (≤3)":
        filtered_words = filtered_words[filtered_words['familiarity'] <= 3]
    elif familiarity_filter == "Learning (4-6)":
        filtered_words = filtered_words[(filtered_words['familiarity'] >= 4) & (filtered_words['familiarity'] <= 6)]
    elif familiarity_filter == "Known (≥7)":
        filtered_words = filtered_words[filtered_words['familiarity'] >= 7]
    if search_term:
        filtered_words = filtered_words[filtered_words['word'].str.contains(search_term, case=False)]

    st.write(f"Showing {len(filtered_words)} of {len(word_bank)} words")
    st.dataframe(filtered_words, use_container_width=True)

# --- Quiz Mode Page ---
elif page == "Quiz Mode":
    st.header("Quiz Mode")
    quiz_type = st.selectbox("Choose Quiz Type", ["Multiple Choice", "Fill in the Blank", "Translation", "Voice Recognition"])
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    if st.button("Start Quiz"):
        user_id = st.session_state.current_user['username']
        if quiz_type == "Multiple Choice":
            quiz_q = generate_multiple_choice_quiz(word_bank)
            st.write(f"What does '{quiz_q['question_word']}' mean?")
            answer = st.radio("Choose the correct answer:", quiz_q['options'])
            if st.button("Submit Answer"):
                is_correct = evaluate_answer(quiz_q, answer)
                log_quiz_result(user_id, quiz_q, answer, is_correct)
                if is_correct:
                    st.success("Correct! 🎉")
                    new_xp = add_xp(user_id, amount=10)
                    update_streak(user_id)
                    new_badges = check_for_badges(user_id)
                    if new_badges:
                        st.success(f"New badge(s) earned: {', '.join(new_badges)}")
                    update_goal_progress(user_id, xp_earned=10)
                    if check_goal_completion(user_id, 'daily'):
                        st.balloons()
                        st.success("Daily goal completed! 🎉")
                    st.info(get_grammar_tip(quiz_q.get('question_word', None)))
                    st.info(get_culture_tip(quiz_q.get('question_word', None)))
            else:
                    st.error(f"Incorrect. The correct answer is: {quiz_q['answer']}")
        elif quiz_type == "Fill in the Blank":
            quiz_q = generate_fill_in_blank_quiz(word_bank)
            st.write(quiz_q['prompt'])
            answer = st.text_input("Your answer:")
            if st.button("Submit Answer"):
                is_correct = evaluate_answer(quiz_q, answer)
                log_quiz_result(user_id, quiz_q, answer, is_correct)
                if is_correct:
                    st.success("Correct! 🎉")
                    new_xp = add_xp(user_id, amount=10)
                    update_streak(user_id)
                    new_badges = check_for_badges(user_id)
                    if new_badges:
                        st.success(f"New badge(s) earned: {', '.join(new_badges)}")
                    update_goal_progress(user_id, xp_earned=10)
                    if check_goal_completion(user_id, 'daily'):
                        st.balloons()
                        st.success("Daily goal completed! 🎉")
                    st.info(get_grammar_tip(quiz_q.get('question_word', None)))
                    st.info(get_culture_tip(quiz_q.get('question_word', None)))
                else:
                    st.error(f"Incorrect. The correct answer is: {quiz_q['answer']}")
        elif quiz_type == "Translation":
            st.write(f"Translate the following Polish sentence: **{word_bank.sample(1).iloc[0]['word']}**")
            
            # Record audio
            audio_file = voice_io.record_audio_streamlit()
            
            if audio_file:
                st.write("Processing your translation...")
                transcribed_text = voice_io.transcribe_audio(audio_file)
                st.write(f"You said: '{transcribed_text}'")
                
                # Get feedback
                feedback, score = voice_io.get_voice_feedback(word_bank.sample(1).iloc[0]['word'], transcribed_text)
                st.write(f"**Feedback:** {feedback}")
                st.write(f"**Score:** {score:.1f}%")
                
                if score >= 70:
                    st.success("Great translation! 🎉")
                    new_xp = add_xp(user_id, amount=10)
                    update_streak(user_id)
                    new_badges = check_for_badges(user_id)
                    if new_badges:
                        st.success(f"New badge(s) earned: {', '.join(new_badges)}")
                    update_goal_progress(user_id, xp_earned=10)
                    if check_goal_completion(user_id, 'daily'):
                        st.balloons()
                        st.success("Daily goal completed! 🎉")
                    st.info(get_grammar_tip(word_bank.sample(1).iloc[0]['word']))
                    st.info(get_culture_tip(word_bank.sample(1).iloc[0]['word']))
                else:
                    st.info(f"Expected: '{word_bank.sample(1).iloc[0]['translation']}'. Keep practicing!")
                
                # Play correct translation
                if st.button("🔊 Hear Correct Translation"):
                    correct_translation = word_bank.sample(1).iloc[0]['translation']
                    correct_audio = voice_io.text_to_speech(correct_translation)
                    if correct_audio:
                        voice_io.play_audio_streamlit(correct_audio)
            else:
                st.info("Click the record button above to start translation")
        elif quiz_type == "Voice Recognition":
            st.write(f"Say the Polish word for: **{word_bank.sample(1).iloc[0]['translation']}**")
            audio_file = voice_io.record_audio_streamlit()
            if audio_file:
                st.write("Processing your pronunciation...")
                expected_phrase = word_bank.sample(1).iloc[0]['word']
                feedback_result = evaluate_pronunciation(expected_phrase, audio_file)
                st.write(f"You said: '{feedback_result['transcription']}'")
                st.write(f"**Feedback:** {feedback_result['feedback']}")
                st.write(f"**Score:** {feedback_result['score']:.1f}%")
                if feedback_result['score'] >= 70:
                    st.success("Great pronunciation! 🎉")
                    new_xp = add_xp(user_id, amount=10)
                    update_streak(user_id)
                    new_badges = check_for_badges(user_id)
                    if new_badges:
                        st.success(f"New badge(s) earned: {', '.join(new_badges)}")
                    update_goal_progress(user_id, xp_earned=10)
                    if check_goal_completion(user_id, 'daily'):
                        st.balloons()
                        st.success("Daily goal completed! 🎉")
                    st.info(get_grammar_tip(expected_phrase))
                    st.info(get_culture_tip(expected_phrase))
                else:
                    st.info(f"Expected: '{expected_phrase}'. Keep practicing!")
                if st.button("🔊 Hear Correct Pronunciation"):
                    correct_audio = voice_io.text_to_speech(expected_phrase)
                    if correct_audio:
                        voice_io.play_audio_streamlit(correct_audio)
            else:
                st.info("Click the record button above to start voice recognition")

# --- Conversation Practice Page ---
elif page == "Conversation Practice":
    st.header("Conversation Practice")
    
    scenario = st.selectbox("Choose a Scenario", ["Café Order", "Self Introduction", "Shopping", "Asking for Directions"])
    tutor_voice = st.selectbox("Choose Tutor Voice", ["Tutor Magda", "Coach Piotr", "Professor Jan"])
    
    if st.button("Start Conversation"):
        st.subheader(f"Scenario: {scenario}")
        
        if scenario == "Café Order":
            tutor_message = "Dzień dobry! Co mogę dla Pana/Pani zrobić?"
            tutor_translation = "(Good day! What can I do for you?)"
            
            st.write(f"**Tutor {tutor_voice}:** {tutor_message}")
            st.write(f"*{tutor_translation}*")
            
            # Play tutor's message
            if st.button("🔊 Play Tutor's Message"):
                tutor_audio = voice_io.text_to_speech(tutor_message)
                if tutor_audio:
                    voice_io.play_audio_streamlit(tutor_audio)
            
            # User response options
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Type your response:**")
                user_response = st.text_area("Your response (Polish):", key="text_response")
                
                if st.button("Submit Text Response"):
                    if user_response:
                        st.write("**You:** " + user_response)
                        st.write("**Tutor:** Bardzo dobrze! Czy chce Pan/Pani coś jeszcze?")
                        st.write("*(Very good! Would you like anything else?)*")
            
            with col2:
                st.write("**Or speak your response:**")
                audio_file = voice_io.record_audio_streamlit()
                
                if audio_file:
                    transcribed_response = voice_io.transcribe_audio(audio_file)
                    st.write(f"**You said:** {transcribed_response}")
                    
                    if transcribed_response and "error" not in transcribed_response.lower():
                        st.write("**Tutor:** Bardzo dobrze! Czy chce Pan/Pani coś jeszcze?")
                        st.write("*(Very good! Would you like anything else?)*")
                        
                        # Play tutor's response
                        response_audio = voice_io.text_to_speech("Bardzo dobrze! Czy chce Pan/Pani coś jeszcze?")
                        if response_audio:
                            voice_io.play_audio_streamlit(response_audio)

    st.markdown("---")
    st.subheader("Ambient Mode (Free Conversation)")
    persona = st.selectbox("Select AI Persona", ["Tutor Magda", "Coach Piotr", "Professor Jan"], key="ambient_persona")
    if not is_ambient_active():
        if st.button("Start Ambient Mode"):
            def on_user_speech(text):
                st.write(f"**You:** {text}")
            def on_ai_response(text):
                st.write(f"**{persona}:** {text}")
                audio = voice_io.text_to_speech(text)
                if audio:
                    voice_io.play_audio_streamlit(audio)
            start_ambient_mode(st.session_state.current_user, persona, on_user_speech, on_ai_response)
            st.success("Ambient Mode started. Speak freely!")
    else:
        if st.button("Stop Ambient Mode"):
            stop_ambient_mode()
            st.info("Ambient Mode stopped.")
    st.info("Ambient Mode lets you have a freeform voice conversation with your AI tutor. The AI will listen and respond in real time.")

# --- Story Mode Page ---
elif page == "Story Mode":
    st.header("Story Mode")
    
    if len(stories) > 0:
        story = stories.iloc[0]
        st.subheader(story['title'])
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(story['content'])
        with col2:
            if st.button("🔊 Listen to Story"):
                story_audio = voice_io.text_to_speech(story['content'])
                if story_audio:
                    voice_io.play_audio_streamlit(story_audio)
                else:
                    st.info("Audio narration not available")
        
        st.subheader("Comprehension Question")
        st.write(story['questions'])
        answer = st.text_input("Your answer:")
        if st.button("Submit Answer"):
            feedback = evaluate_story_answer({'question': story['questions']}, answer)
            st.success(f"Feedback: {feedback['feedback']} (Score: {feedback['score']})")
        st.markdown("---")
        st.subheader("Grammar Tip for this Story")
        st.info(get_grammar_tip(story['title']))
        st.subheader("Culture Note for this Story")
        st.info(get_culture_tip(story['title']))

# --- Review Deck Page ---
elif page == "Review Deck":
    st.header("Review Deck (Spaced Repetition)")
    user_id = st.session_state.current_user['username']
    review_words = get_words_for_review(user_id, word_bank)
    if len(review_words) > 0:
        st.write(f"You have {len(review_words)} words to review today.")
        if st.button("Start Review Session"):
            review_word = review_words.sample(1).iloc[0]
            st.subheader("Review Word")
            st.write(f"**{review_word['word']}**")
            st.write(f"Example: {review_word['example']}")
            col1, col2, col3, col4 = st.columns(4)
            if col1.button("😰 Hard"):
                update_familiarity(user_id, False)
                st.info("Marked as hard - will review again soon")
            if col2.button("😐 Good"):
                update_familiarity(user_id, True)
                st.info("Marked as good - will review in a few days")
            if col3.button("😊 Easy"):
                update_familiarity(user_id, True)
                st.info("Marked as easy - will review in a week")
            if col4.button("🎯 Perfect"):
                update_familiarity(user_id, True)
                st.info("Marked as perfect - will review in a month")
    else:
        st.success("🎉 No words to review today! Great job!")

# --- Leaderboard Page ---
elif page == "Leaderboard":
    st.header("Leaderboard (Weekly XP)")
    try:
        leaderboard_df = get_leaderboard(top_n=10)
        if not leaderboard_df.empty:
            leaderboard_df = leaderboard_df.reset_index(drop=True)
            leaderboard_df['Rank'] = leaderboard_df.index + 1
            st.table(leaderboard_df[['Rank', 'username', 'xp']].rename(columns={'username': 'User', 'xp': 'XP'}))
        else:
            st.info("No leaderboard data available for this week.")
    except Exception as e:
        st.error(f"Error loading leaderboard: {e}")

# --- Settings Page ---
elif page == "Settings":
    st.header("Settings")
    
    st.subheader("Study Goals")
    user_id = st.session_state.current_user['username']
    current_goal = get_goal(user_id, 'daily')
    daily_goal = st.slider("Daily Quiz Goal", 1, 20, current_goal or 5)
    if st.button("Save Daily Goal"):
        set_goal(user_id, 'daily', daily_goal)
        st.success("Daily goal updated!")
    
    st.subheader("Voice Settings")
    voice_speed = st.slider("Speech Speed", 0.5, 2.0, 1.0, 0.1)
    voice_volume = st.slider("Voice Volume", 0.0, 1.0, 0.8, 0.1)
    
    st.subheader("Reminders")
    enable_reminders = st.checkbox("Enable Daily Reminders")
    if enable_reminders:
        reminder_time = st.time_input("Reminder Time", value=datetime.strptime("19:00", "%H:%M").time())
        
        st.subheader("SMS Notifications (Optional)")
        enable_sms = st.checkbox("Enable SMS Reminders")
        if enable_sms:
            phone_number = st.text_input("Phone Number (with country code)")
            if st.button("Test SMS"):
                st.info("Test SMS would be sent here")
    
    st.subheader("Data Management")
    if st.button("Export Progress"):
        st.info("Progress data would be exported here")
    if st.button("Reset Progress"):
        if st.checkbox("I understand this will reset all my progress"):
            st.warning("Progress reset functionality would be implemented here")

