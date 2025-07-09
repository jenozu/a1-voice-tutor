import json
import os
import random

# Grammar Tipper Module

def get_grammar_tip(context, tips_path='data/grammar_tips.json'):
    """
    Retrieve a grammar tip based on context (topic/word). If no match, return a random tip.
    Args:
        context (str): Topic, word, or lesson context
        tips_path (str): Path to grammar_tips.json
    Returns:
        str: Grammar tip
    """
    try:
        if not os.path.exists(tips_path):
            return "No grammar tips available."
        with open(tips_path, 'r', encoding='utf-8') as f:
            tips = json.load(f)
        # Try to find a tip matching the context
        for tip in tips:
            if context and (context.lower() in tip.get('topic','').lower() or context.lower() in tip.get('word','').lower()):
                return tip.get('tip', 'No tip found.')
        # If no match, return a random tip
        if tips:
            return random.choice(tips).get('tip', 'No tip found.')
        return "No grammar tips found."
    except Exception as e:
        return f"Error loading grammar tips: {e}"


