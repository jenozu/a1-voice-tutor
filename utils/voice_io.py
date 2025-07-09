# Voice Input/Output Module

import streamlit as st
import speech_recognition as sr
import pyttsx3
import tempfile
import os
from io import BytesIO
import wave
from vosk import Model, KaldiRecognizer
import json

def initialize_tts():
    """Initialize text-to-speech engine"""
    try:
        engine = pyttsx3.init()
        # Set properties for Polish voice if available
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'polish' in voice.name.lower() or 'pl' in voice.id.lower():
                engine.setProperty('voice', voice.id)
                break
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 0.8)  # Volume level
        return engine
    except Exception as e:
        st.error(f"Failed to initialize TTS engine: {e}")
        return None

def text_to_speech(text, voice_id="default"):
    """Convert text to speech and return audio file path"""
    try:
        engine = initialize_tts()
        if engine is None:
            return None
        
        # Create temporary file for audio
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_file.close()
        
        # Save speech to file
        engine.save_to_file(text, temp_file.name)
        engine.runAndWait()
        
        return temp_file.name
    except Exception as e:
        st.error(f"Text-to-speech error: {e}")
        return None

def record_audio_streamlit():
    """Record audio using Streamlit's audio input widget"""
    st.write("🎤 Click the button below to record your voice:")
    
    # Use Streamlit's experimental audio input
    audio_bytes = st.audio_input("Record your pronunciation")
    
    if audio_bytes:
        # Save audio to temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_file.write(audio_bytes.getvalue())
        temp_file.close()
        return temp_file.name
    
    return None

def transcribe_audio_vosk(audio_file_path, model_path="models/vosk-pl"):
    """Transcribe audio file to text using Vosk offline speech recognition"""
    try:
        model = Model(model_path)
        wf = wave.open(audio_file_path, "rb")
        rec = KaldiRecognizer(model, wf.getframerate())
        results = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                results.append(json.loads(rec.Result()))
        results.append(json.loads(rec.FinalResult()))
        transcript = " ".join([r.get("text", "") for r in results])
        return transcript.strip()
    except Exception as e:
        return f"Vosk transcription error: {e}"


def transcribe_audio(audio_file_path):
    """Transcribe audio file to text using Vosk (offline)"""
    return transcribe_audio_vosk(audio_file_path)

def play_audio_streamlit(audio_file_path):
    """Play audio file in Streamlit"""
    try:
        if os.path.exists(audio_file_path):
            with open(audio_file_path, 'rb') as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/wav')
        else:
            st.error("Audio file not found")
    except Exception as e:
        st.error(f"Error playing audio: {e}")

def get_voice_feedback(expected_text, spoken_text):
    """Compare expected text with spoken text and provide feedback"""
    expected_words = expected_text.lower().split()
    spoken_words = spoken_text.lower().split()
    
    if expected_text.lower() == spoken_text.lower():
        return "Perfect! 🎉", 100
    
    # Calculate similarity score
    correct_words = 0
    for word in spoken_words:
        if word in expected_words:
            correct_words += 1
    
    if len(spoken_words) > 0:
        score = (correct_words / len(expected_words)) * 100
    else:
        score = 0
    
    if score >= 80:
        feedback = "Great pronunciation! 👍"
    elif score >= 60:
        feedback = "Good effort! Keep practicing. 😊"
    elif score >= 40:
        feedback = "Not bad, but try again. 🤔"
    else:
        feedback = "Let's practice this word more. 💪"
    
    return feedback, score

def cleanup_temp_files():
    """Clean up temporary audio files"""
    try:
        temp_dir = tempfile.gettempdir()
        for filename in os.listdir(temp_dir):
            if filename.endswith('.wav') and filename.startswith('tmp'):
                file_path = os.path.join(temp_dir, filename)
                try:
                    os.remove(file_path)
                except:
                    pass  # Ignore errors when cleaning up
    except:
        pass  # Ignore errors when cleaning up

