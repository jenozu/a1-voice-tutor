# Quiz Generator Module

import pandas as pd
import random
from typing import List, Dict, Any
from datetime import datetime
import os

def generate_multiple_choice_quiz(word_bank, num_questions=5, difficulty='easy'):
    """
    Generate a multiple choice quiz from the word bank
    
    Args:
        word_bank (DataFrame): Word bank data
        num_questions (int): Number of questions to generate
        difficulty (str): Difficulty level ('easy', 'medium', 'hard')
    
    Returns:
        list: List of quiz questions
    """
    questions = []
    
    # Filter words based on difficulty
    if difficulty == 'easy':
        filtered_words = word_bank[word_bank['familiarity'] <= 5]
    elif difficulty == 'medium':
        filtered_words = word_bank[(word_bank['familiarity'] >= 4) & (word_bank['familiarity'] <= 7)]
    else:  # hard
        filtered_words = word_bank[word_bank['familiarity'] >= 6]
    
    if len(filtered_words) < num_questions:
        filtered_words = word_bank  # Use all words if not enough in difficulty range
    
    # Sample questions
    question_words = filtered_words.sample(min(num_questions, len(filtered_words)))
    
    for _, word_row in question_words.iterrows():
        # Generate wrong answers
        other_words = word_bank[word_bank['word'] != word_row['word']]
        if len(other_words) >= 3:
            wrong_answers = other_words['translation'].sample(3).tolist()
        else:
            wrong_answers = other_words['translation'].tolist()
            while len(wrong_answers) < 3:
                wrong_answers.append("Wrong answer")
        
        # Create question
        options = [word_row['translation']] + wrong_answers
        random.shuffle(options)
        
        question = {
            'type': 'multiple_choice',
            'question': f"What does '{word_row['word']}' mean?",
            'options': options,
            'correct_answer': word_row['translation'],
            'word': word_row['word'],
            'example': word_row['example']
        }
        questions.append(question)
    
    return questions

def generate_translation_quiz(word_bank, num_questions=5, direction='polish_to_english'):
    """
    Generate a translation quiz
    
    Args:
        word_bank (DataFrame): Word bank data
        num_questions (int): Number of questions to generate
        direction (str): 'polish_to_english' or 'english_to_polish'
    
    Returns:
        list: List of quiz questions
    """
    questions = []
    question_words = word_bank.sample(min(num_questions, len(word_bank)))
    
    for _, word_row in question_words.iterrows():
        if direction == 'polish_to_english':
            question_text = f"Translate to English: '{word_row['word']}'"
            correct_answer = word_row['translation']
        else:
            question_text = f"Translate to Polish: '{word_row['translation']}'"
            correct_answer = word_row['word']
        
        question = {
            'type': 'translation',
            'question': question_text,
            'correct_answer': correct_answer,
            'word': word_row['word'],
            'example': word_row['example']
        }
        questions.append(question)
    
    return questions

def generate_fill_in_blank_quiz(word_bank, num_questions=5):
    """
    Generate a fill-in-the-blank quiz using example sentences
    
    Args:
        word_bank (DataFrame): Word bank data
        num_questions (int): Number of questions to generate
    
    Returns:
        list: List of quiz questions
    """
    questions = []
    
    # Filter words that have examples
    words_with_examples = word_bank[word_bank['example'].notna() & (word_bank['example'] != '')]
    
    if len(words_with_examples) == 0:
        return questions  # No examples available
    
    question_words = words_with_examples.sample(min(num_questions, len(words_with_examples)))
    
    for _, word_row in question_words.iterrows():
        example = word_row['example']
        word = word_row['word']
        
        # Replace the word with a blank
        if word in example:
            question_text = example.replace(word, "____")
            
            question = {
                'type': 'fill_in_blank',
                'question': f"Fill in the blank: {question_text}",
                'correct_answer': word,
                'word': word,
                'example': example,
                'translation': word_row['translation']
            }
            questions.append(question)
    
    return questions

def generate_voice_quiz(word_bank, num_questions=5):
    """
    Generate a voice pronunciation quiz
    
    Args:
        word_bank (DataFrame): Word bank data
        num_questions (int): Number of questions to generate
    
    Returns:
        list: List of quiz questions
    """
    questions = []
    question_words = word_bank.sample(min(num_questions, len(word_bank)))
    
    for _, word_row in question_words.iterrows():
        question = {
            'type': 'voice',
            'question': f"Say the Polish word for: '{word_row['translation']}'",
            'correct_answer': word_row['word'],
            'word': word_row['word'],
            'example': word_row['example'],
            'translation': word_row['translation']
        }
        questions.append(question)
    
    return questions

def generate_adaptive_quiz(word_bank, user_performance=None, num_questions=5):
    """
    Generate an adaptive quiz based on user performance
    
    Args:
        word_bank (DataFrame): Word bank data
        user_performance (dict): User's past performance data
        num_questions (int): Number of questions to generate
    
    Returns:
        list: List of quiz questions
    """
    if user_performance is None:
        # Default to mixed difficulty
        return generate_mixed_quiz(word_bank, num_questions)
    
    # Analyze performance to determine focus areas
    weak_areas = []
    if 'tags' in word_bank.columns:
        for tag in word_bank['tags'].unique():
            tag_performance = user_performance.get(tag, 0)
            if tag_performance < 70:  # Less than 70% accuracy
                weak_areas.append(tag)
    
    # Focus on weak areas
    if weak_areas:
        focus_words = word_bank[word_bank['tags'].isin(weak_areas)]
        if len(focus_words) >= num_questions:
            return generate_multiple_choice_quiz(focus_words, num_questions)
    
    # Default to mixed quiz
    return generate_mixed_quiz(word_bank, num_questions)

def generate_mixed_quiz(word_bank, num_questions=5):
    """
    Generate a mixed quiz with different question types
    
    Args:
        word_bank (DataFrame): Word bank data
        num_questions (int): Number of questions to generate
    
    Returns:
        list: List of quiz questions
    """
    questions = []
    
    # Distribute question types
    mc_questions = max(1, num_questions // 2)
    translation_questions = max(1, num_questions // 3)
    fill_blank_questions = num_questions - mc_questions - translation_questions
    
    # Generate different types of questions
    questions.extend(generate_multiple_choice_quiz(word_bank, mc_questions))
    questions.extend(generate_translation_quiz(word_bank, translation_questions))
    
    if fill_blank_questions > 0:
        questions.extend(generate_fill_in_blank_quiz(word_bank, fill_blank_questions))
    
    # Shuffle the questions
    random.shuffle(questions)
    
    return questions[:num_questions]

def evaluate_answer(question, user_answer):
    """
    Evaluate user's answer to a quiz question
    
    Args:
        question (dict): Quiz question
        user_answer (str): User's answer
    
    Returns:
        dict: Evaluation result
    """
    correct_answer = question['correct_answer'].lower().strip()
    user_answer = user_answer.lower().strip()
    
    is_correct = correct_answer == user_answer
    
    # For partial credit in translation questions
    if question['type'] == 'translation' and not is_correct:
        # Check if user answer contains the correct answer
        if correct_answer in user_answer or user_answer in correct_answer:
            is_correct = True
    
    result = {
        'is_correct': is_correct,
        'correct_answer': question['correct_answer'],
        'user_answer': user_answer,
        'feedback': get_feedback(is_correct, question),
        'word': question['word']
    }
    
    return result

def get_feedback(is_correct, question):
    """
    Generate feedback for quiz answers
    
    Args:
        is_correct (bool): Whether the answer was correct
        question (dict): Quiz question
    
    Returns:
        str: Feedback message
    """
    if is_correct:
        feedback_options = [
            "Excellent! 🎉",
            "Perfect! 👍",
            "Great job! ⭐",
            "Well done! 🌟",
            "Fantastic! 🎊"
        ]
        return random.choice(feedback_options)
    else:
        return f"Not quite right. The correct answer is: {question['correct_answer']}"

def log_quiz_result(user_id, question, user_answer, is_correct, timestamp=None, quiz_log_path='data/quiz_log.csv'):
    """
    Log the result of a quiz attempt to quiz_log.csv
    Args:
        user_id (str): The user's ID or username
        question (dict): The quiz question dict
        user_answer (str): The user's answer
        is_correct (bool): Whether the answer was correct
        timestamp (datetime, optional): When the attempt was made
        quiz_log_path (str): Path to the quiz log CSV
    """
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    log_entry = {
        'user_id': user_id,
        'timestamp': timestamp,
        'question_type': question.get('type', ''),
        'question_text': question.get('question', ''),
        'word': question.get('word', ''),
        'correct_answer': question.get('correct_answer', ''),
        'user_answer': user_answer,
        'is_correct': is_correct
    }
    
    # Append to CSV (create if doesn't exist)
    try:
        if os.path.exists(quiz_log_path):
            df = pd.read_csv(quiz_log_path)
            df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([log_entry])
        df.to_csv(quiz_log_path, index=False)
    except Exception as e:
        print(f"Error logging quiz result: {e}")

