# Pronunciation Feedback Module

import speech_recognition as sr
import tempfile
import os
from difflib import SequenceMatcher
import re
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import voice_io

def analyze_pronunciation(audio_file, expected_text):
    """
    Analyze pronunciation by comparing spoken text with expected text
    
    Args:
        audio_file (str): Path to audio file
        expected_text (str): Expected text to be spoken
    
    Returns:
        dict: Analysis result with transcription and similarity score
    """
    try:
        # Use Vosk-based transcription from voice_io
        transcribed_text = voice_io.transcribe_audio(audio_file)
        if not transcribed_text or 'error' in transcribed_text.lower():
            return {
                'transcribed_text': '',
                'similarity_score': 0,
                'error': transcribed_text if transcribed_text else 'Could not understand audio'
            }
        # Calculate similarity score
        similarity_score = calculate_similarity(expected_text, transcribed_text)
        return {
            'transcribed_text': transcribed_text,
            'similarity_score': similarity_score,
            'error': None
        }
    except Exception as e:
        return {
            'transcribed_text': '',
            'similarity_score': 0,
            'error': f'Audio analysis error: {e}'
        }

def calculate_similarity(expected, actual):
    """
    Calculate similarity between expected and actual text
    
    Args:
        expected (str): Expected text
        actual (str): Actual transcribed text
    
    Returns:
        float: Similarity score (0-100)
    """
    # Normalize texts
    expected_clean = normalize_text(expected)
    actual_clean = normalize_text(actual)
    
    # Calculate sequence similarity
    similarity = SequenceMatcher(None, expected_clean, actual_clean).ratio()
    
    # Convert to percentage
    return similarity * 100

def normalize_text(text):
    """
    Normalize text for comparison
    
    Args:
        text (str): Text to normalize
    
    Returns:
        str: Normalized text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and extra spaces
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    
    # Strip whitespace
    text = text.strip()
    
    return text

def get_pronunciation_score(analysis_result):
    """
    Get pronunciation score and feedback based on analysis
    
    Args:
        analysis_result (dict): Result from analyze_pronunciation
    
    Returns:
        dict: Score and feedback
    """
    if analysis_result.get('error'):
        return {
            'score': 0,
            'feedback': f"Error: {analysis_result['error']}",
            'level': 'error'
        }
    
    similarity_score = analysis_result['similarity_score']
    transcribed = analysis_result['transcribed_text']
    
    if similarity_score >= 90:
        feedback = "Excellent pronunciation! 🌟"
        level = "excellent"
    elif similarity_score >= 80:
        feedback = "Very good pronunciation! 👍"
        level = "very_good"
    elif similarity_score >= 70:
        feedback = "Good pronunciation! Keep practicing. 😊"
        level = "good"
    elif similarity_score >= 50:
        feedback = "Not bad, but needs improvement. 🤔"
        level = "needs_improvement"
    elif similarity_score >= 30:
        feedback = "Keep practicing! You're getting there. 💪"
        level = "practice_more"
    else:
        feedback = "Let's try again. Listen carefully and repeat. 🎯"
        level = "try_again"
    
    return {
        'score': similarity_score,
        'feedback': feedback,
        'level': level,
        'transcribed': transcribed
    }

def get_detailed_feedback(expected_text, transcribed_text):
    """
    Get detailed feedback comparing expected and transcribed text
    
    Args:
        expected_text (str): Expected text
        transcribed_text (str): Transcribed text
    
    Returns:
        dict: Detailed feedback
    """
    expected_words = normalize_text(expected_text).split()
    transcribed_words = normalize_text(transcribed_text).split()
    
    feedback = {
        'word_accuracy': [],
        'missing_words': [],
        'extra_words': [],
        'suggestions': []
    }
    
    # Check word-by-word accuracy
    for i, expected_word in enumerate(expected_words):
        if i < len(transcribed_words):
            transcribed_word = transcribed_words[i]
            word_similarity = SequenceMatcher(None, expected_word, transcribed_word).ratio()
            
            feedback['word_accuracy'].append({
                'expected': expected_word,
                'transcribed': transcribed_word,
                'accuracy': word_similarity * 100
            })
        else:
            feedback['missing_words'].append(expected_word)
    
    # Check for extra words
    if len(transcribed_words) > len(expected_words):
        feedback['extra_words'] = transcribed_words[len(expected_words):]
    
    # Generate suggestions
    if feedback['missing_words']:
        feedback['suggestions'].append("Try to pronounce all words clearly.")
    
    if any(word['accuracy'] < 70 for word in feedback['word_accuracy']):
        feedback['suggestions'].append("Focus on pronouncing each syllable clearly.")
    
    if feedback['extra_words']:
        feedback['suggestions'].append("Be careful not to add extra words.")
    
    return feedback

def practice_word_pronunciation(word, audio_file):
    """
    Practice pronunciation of a specific word
    
    Args:
        word (str): Word to practice
        audio_file (str): Path to recorded audio
    
    Returns:
        dict: Practice result with detailed feedback
    """
    analysis = analyze_pronunciation(audio_file, word)
    score_result = get_pronunciation_score(analysis)
    detailed_feedback = get_detailed_feedback(word, analysis.get('transcribed_text', ''))
    
    return {
        'word': word,
        'transcribed': analysis.get('transcribed_text', ''),
        'score': score_result['score'],
        'feedback': score_result['feedback'],
        'level': score_result['level'],
        'detailed_feedback': detailed_feedback
    }

def get_pronunciation_tips(word, language='polish'):
    """
    Get pronunciation tips for a specific word
    
    Args:
        word (str): Word to get tips for
        language (str): Language of the word
    
    Returns:
        list: List of pronunciation tips
    """
    # Basic Polish pronunciation tips
    polish_tips = {
        'ą': "Pronounce 'ą' like 'on' in French 'bon'",
        'ę': "Pronounce 'ę' like 'en' in French 'vent'",
        'ć': "Pronounce 'ć' like 'ch' in 'cheap' but softer",
        'ł': "Pronounce 'ł' like 'w' in 'water'",
        'ń': "Pronounce 'ń' like 'ny' in 'canyon'",
        'ś': "Pronounce 'ś' like 'sh' in 'sheep' but softer",
        'ź': "Pronounce 'ź' like 'z' but softer",
        'ż': "Pronounce 'ż' like 's' in 'measure'",
        'sz': "Pronounce 'sz' like 'sh' in 'shop'",
        'cz': "Pronounce 'cz' like 'ch' in 'church'",
        'rz': "Pronounce 'rz' like 'zh' sound",
        'dz': "Pronounce 'dz' like 'ds' in 'woods'",
        'dż': "Pronounce 'dż' like 'j' in 'judge'",
        'dź': "Pronounce 'dź' like soft 'j'"
    }
    
    tips = []
    word_lower = word.lower()
    
    for pattern, tip in polish_tips.items():
        if pattern in word_lower:
            tips.append(tip)
    
    # General tips
    if not tips:
        tips.append("Break the word into syllables and pronounce each one clearly.")
        tips.append("Listen to native speakers and try to imitate their pronunciation.")
    
    return tips

