# Spaced Repetition System (SRS) Engine

import pandas as pd
from datetime import datetime, timedelta
import math

def calculate_next_review(familiarity_score, last_review_date=None, correct_answer=True):
    """
    Calculate when a word should be reviewed next based on SRS algorithm
    
    Args:
        familiarity_score (int): Current familiarity score (1-10)
        last_review_date (datetime): When the word was last reviewed
        correct_answer (bool): Whether the user answered correctly
    
    Returns:
        datetime: Next review date
    """
    if last_review_date is None:
        last_review_date = datetime.now()
    
    # Adjust familiarity based on performance
    if correct_answer:
        new_familiarity = min(10, familiarity_score + 1)
    else:
        new_familiarity = max(1, familiarity_score - 2)
    
    # Calculate interval based on familiarity (exponential growth)
    if new_familiarity <= 2:
        interval_days = 1  # Review tomorrow
    elif new_familiarity <= 4:
        interval_days = 3  # Review in 3 days
    elif new_familiarity <= 6:
        interval_days = 7  # Review in a week
    elif new_familiarity <= 8:
        interval_days = 14  # Review in 2 weeks
    else:
        interval_days = 30  # Review in a month
    
    next_review = last_review_date + timedelta(days=interval_days)
    return next_review, new_familiarity

def update_familiarity(word_id, correct_answer, word_bank_path='data/word_bank.csv'):
    """
    Update familiarity score for a word based on user performance
    
    Args:
        word_id (str): The word to update
        correct_answer (bool): Whether the user answered correctly
        word_bank_path (str): Path to word bank CSV
    """
    try:
        # Load word bank
        word_bank = pd.read_csv(word_bank_path)
        
        # Find the word
        word_index = word_bank[word_bank['word'] == word_id].index
        
        if len(word_index) > 0:
            current_familiarity = word_bank.loc[word_index[0], 'familiarity']
            
            # Calculate new familiarity and next review
            next_review, new_familiarity = calculate_next_review(
                current_familiarity, 
                datetime.now(), 
                correct_answer
            )
            
            # Update the word bank
            word_bank.loc[word_index[0], 'familiarity'] = new_familiarity
            word_bank.loc[word_index[0], 'last_review'] = datetime.now().strftime('%Y-%m-%d')
            word_bank.loc[word_index[0], 'next_review'] = next_review.strftime('%Y-%m-%d')
            
            # Save back to CSV
            word_bank.to_csv(word_bank_path, index=False)
            
            return new_familiarity
        else:
            return None
            
    except Exception as e:
        print(f"Error updating familiarity: {e}")
        return None

def get_words_for_review(word_bank_path='data/word_bank.csv', max_words=10):
    """
    Get words that need to be reviewed today
    
    Args:
        word_bank_path (str): Path to word bank CSV
        max_words (int): Maximum number of words to return
    
    Returns:
        DataFrame: Words that need review
    """
    try:
        word_bank = pd.read_csv(word_bank_path)
        today = datetime.now().date()
        
        # Add next_review column if it doesn't exist
        if 'next_review' not in word_bank.columns:
            word_bank['next_review'] = today.strftime('%Y-%m-%d')
        
        # Convert next_review to datetime
        word_bank['next_review'] = pd.to_datetime(word_bank['next_review'], errors='coerce')
        
        # Fill NaN values with today's date
        word_bank['next_review'] = word_bank['next_review'].fillna(pd.Timestamp(today))
        
        # Filter words that need review (next_review <= today)
        words_for_review = word_bank[word_bank['next_review'].dt.date <= today]
        
        # Sort by familiarity (lowest first) and limit
        words_for_review = words_for_review.sort_values('familiarity').head(max_words)
        
        return words_for_review
        
    except Exception as e:
        print(f"Error getting words for review: {e}")
        return pd.DataFrame()

def get_learning_stats(word_bank_path='data/word_bank.csv'):
    """
    Get learning statistics from the word bank
    
    Args:
        word_bank_path (str): Path to word bank CSV
    
    Returns:
        dict: Learning statistics
    """
    try:
        word_bank = pd.read_csv(word_bank_path)
        
        total_words = len(word_bank)
        needs_review = len(word_bank[word_bank['familiarity'] <= 3])
        learning = len(word_bank[(word_bank['familiarity'] >= 4) & (word_bank['familiarity'] <= 6)])
        known = len(word_bank[word_bank['familiarity'] >= 7])
        
        stats = {
            'total_words': total_words,
            'needs_review': needs_review,
            'learning': learning,
            'known': known,
            'completion_percentage': (known / total_words * 100) if total_words > 0 else 0
        }
        
        return stats
        
    except Exception as e:
        print(f"Error getting learning stats: {e}")
        return {
            'total_words': 0,
            'needs_review': 0,
            'learning': 0,
            'known': 0,
            'completion_percentage': 0
        }

