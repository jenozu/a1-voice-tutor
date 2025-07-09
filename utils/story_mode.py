# Story Mode Module

import pandas as pd
import random
from typing import List, Dict, Any

def get_story(story_id, stories_path='data/stories.csv'):
    """
    Retrieve a specific story by ID
    
    Args:
        story_id (str): ID of the story to retrieve
        stories_path (str): Path to stories CSV file
    
    Returns:
        dict: Story data or None if not found
    """
    try:
        stories = pd.read_csv(stories_path)
        story_row = stories[stories['story_id'] == story_id]
        
        if len(story_row) > 0:
            return story_row.iloc[0].to_dict()
        else:
            return None
            
    except Exception as e:
        print(f"Error loading story: {e}")
        return None

def get_all_stories(stories_path='data/stories.csv'):
    """
    Get all available stories
    
    Args:
        stories_path (str): Path to stories CSV file
    
    Returns:
        DataFrame: All stories
    """
    try:
        return pd.read_csv(stories_path)
    except Exception as e:
        print(f"Error loading stories: {e}")
        return pd.DataFrame()

def get_stories_by_difficulty(difficulty='beginner', stories_path='data/stories.csv'):
    """
    Get stories filtered by difficulty level
    
    Args:
        difficulty (str): Difficulty level ('beginner', 'intermediate', 'advanced')
        stories_path (str): Path to stories CSV file
    
    Returns:
        DataFrame: Filtered stories
    """
    try:
        stories = pd.read_csv(stories_path)
        
        if 'difficulty' in stories.columns:
            return stories[stories['difficulty'] == difficulty]
        else:
            # If no difficulty column, return all stories
            return stories
            
    except Exception as e:
        print(f"Error filtering stories by difficulty: {e}")
        return pd.DataFrame()

def generate_comprehension_questions(story_content, num_questions=3):
    """
    Generate comprehension questions for a story
    
    Args:
        story_content (str): The story text
        num_questions (int): Number of questions to generate
    
    Returns:
        list: List of comprehension questions
    """
    # This is a simplified version - in a real app, you might use NLP
    # to automatically generate questions from the story content
    
    # For now, we'll use predefined question templates
    question_templates = [
        "What is the main character's name?",
        "Where does the story take place?",
        "What happens at the beginning of the story?",
        "What is the main problem in the story?",
        "How does the story end?",
        "What did you learn from this story?",
        "Which character do you like most and why?",
        "What would you do differently if you were the main character?"
    ]
    
    # Select random questions
    selected_questions = random.sample(
        question_templates, 
        min(num_questions, len(question_templates))
    )
    
    questions = []
    for i, question_text in enumerate(selected_questions):
        questions.append({
            'id': i + 1,
            'question': question_text,
            'type': 'open_ended'
        })
    
    return questions

def create_story_with_blanks(story_content, word_bank, num_blanks=5):
    """
    Create a story with blanks for vocabulary practice
    
    Args:
        story_content (str): The original story text
        word_bank (DataFrame): Available vocabulary words
        num_blanks (int): Number of words to replace with blanks
    
    Returns:
        dict: Story with blanks and answer key
    """
    words = story_content.split()
    story_words = [word.lower().strip('.,!?;:') for word in words]
    
    # Find words that are in the word bank
    available_words = word_bank['word'].str.lower().tolist()
    replaceable_indices = []
    
    for i, word in enumerate(story_words):
        if word in available_words:
            replaceable_indices.append(i)
    
    # Select random words to replace
    if len(replaceable_indices) > num_blanks:
        selected_indices = random.sample(replaceable_indices, num_blanks)
    else:
        selected_indices = replaceable_indices
    
    # Create story with blanks
    blanked_words = words.copy()
    answer_key = {}
    
    for i, index in enumerate(selected_indices):
        original_word = words[index]
        blank_id = f"blank_{i+1}"
        blanked_words[index] = f"[{blank_id}]"
        answer_key[blank_id] = original_word
    
    blanked_story = ' '.join(blanked_words)
    
    return {
        'story_with_blanks': blanked_story,
        'answer_key': answer_key,
        'original_story': story_content
    }

def evaluate_story_answer(question, user_answer):
    """
    Evaluate user's answer to a story comprehension question
    
    Args:
        question (dict): The question
        user_answer (str): User's answer
    
    Returns:
        dict: Evaluation result
    """
    # For open-ended questions, we'll provide encouraging feedback
    # In a real app, you might use NLP to evaluate the quality of answers
    
    if len(user_answer.strip()) == 0:
        feedback = "Please provide an answer to continue."
        score = 0
    elif len(user_answer.strip()) < 10:
        feedback = "Good start! Try to provide a more detailed answer."
        score = 50
    else:
        feedback = "Great answer! You're understanding the story well."
        score = 100
    
    return {
        'feedback': feedback,
        'score': score,
        'user_answer': user_answer
    }

def get_story_vocabulary(story_content, word_bank):
    """
    Extract vocabulary words from a story that are in the word bank
    
    Args:
        story_content (str): The story text
        word_bank (DataFrame): Available vocabulary words
    
    Returns:
        list: List of vocabulary words found in the story
    """
    story_words = story_content.lower().split()
    story_words = [word.strip('.,!?;:') for word in story_words]
    
    available_words = word_bank['word'].str.lower().tolist()
    found_vocabulary = []
    
    for word in story_words:
        if word in available_words:
            # Get the original word data from word bank
            word_data = word_bank[word_bank['word'].str.lower() == word].iloc[0]
            if word_data['word'] not in [v['word'] for v in found_vocabulary]:
                found_vocabulary.append({
                    'word': word_data['word'],
                    'translation': word_data['translation'],
                    'example': word_data['example']
                })
    
    return found_vocabulary

def create_enhanced_stories():
    """
    Create enhanced story data with more detailed stories
    
    Returns:
        list: List of enhanced stories
    """
    enhanced_stories = [
        {
            'story_id': 1,
            'title': 'My First Day',
            'difficulty': 'beginner',
            'content': 'Dzień dobry. Nazywam się Anna. Jestem z Polski. Dziś jest mój pierwszy dzień w nowej szkole. Jestem bardzo szczęśliwa. Mam nową torbę i nowe książki. Moja mama dała mi kanapkę z chlebem i serem. Lubię ser. W szkole poznaję nowych przyjaciół. Oni są bardzo mili.',
            'translation': 'Good day. My name is Anna. I am from Poland. Today is my first day at a new school. I am very happy. I have a new bag and new books. My mother gave me a sandwich with bread and cheese. I like cheese. At school I meet new friends. They are very nice.',
            'questions': 'What is the girl\'s name? Where is she from? What did her mother give her?'
        },
        {
            'story_id': 2,
            'title': 'At the Café',
            'difficulty': 'beginner',
            'content': 'Idę do kawiarni. Kawiarnia jest bardzo ładna. Zamawiam kawę i ciasto. Kawa jest gorąca i smaczna. Ciasto jest słodkie. Czytam książkę i piję kawę. Jest bardzo spokojnie. Lubię spędzać czas w kawiarni.',
            'translation': 'I go to the café. The café is very nice. I order coffee and cake. The coffee is hot and tasty. The cake is sweet. I read a book and drink coffee. It is very peaceful. I like spending time at the café.',
            'questions': 'Where does the person go? What do they order? What do they do while drinking coffee?'
        },
        {
            'story_id': 3,
            'title': 'Shopping Day',
            'difficulty': 'intermediate',
            'content': 'W sobotę idę na zakupy z mamą. Najpierw idziemy do sklepu spożywczego. Kupujemy chleb, mleko, jajka i warzywa. Potem idziemy do sklepu z ubraniami. Mama kupuje nową sukienkę, a ja kupuję nowe buty. Na końcu idziemy do księgarni. Kupuję nową książkę o przygodach.',
            'translation': 'On Saturday I go shopping with my mother. First we go to the grocery store. We buy bread, milk, eggs and vegetables. Then we go to the clothing store. Mom buys a new dress, and I buy new shoes. Finally we go to the bookstore. I buy a new adventure book.',
            'questions': 'Who goes shopping? What do they buy at the grocery store? What does the narrator buy at the bookstore?'
        }
    ]
    
    return enhanced_stories

def save_enhanced_stories(stories_path='data/stories.csv'):
    """
    Save enhanced stories to CSV file
    
    Args:
        stories_path (str): Path to save the stories
    """
    try:
        enhanced_stories = create_enhanced_stories()
        stories_df = pd.DataFrame(enhanced_stories)
        stories_df.to_csv(stories_path, index=False)
        print(f"Enhanced stories saved to {stories_path}")
    except Exception as e:
        print(f"Error saving enhanced stories: {e}")

