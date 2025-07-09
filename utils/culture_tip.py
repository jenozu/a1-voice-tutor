import json
import os
import random

# Culture Tip Module

def get_culture_tip(context, notes_path='data/culture_notes.json'):
    """
    Retrieve a culture note based on context (topic/word). If no match, return a random note.
    Args:
        context (str): Topic, word, or lesson context
        notes_path (str): Path to culture_notes.json
    Returns:
        str: Culture note
    """
    try:
        if not os.path.exists(notes_path):
            return "No culture notes available."
        with open(notes_path, 'r', encoding='utf-8') as f:
            notes = json.load(f)
        # Try to find a note matching the context
        for note in notes:
            if context and (context.lower() in note.get('topic','').lower() or context.lower() in note.get('word','').lower()):
                return note.get('note', 'No note found.')
        # If no match, return a random note
        if notes:
            return random.choice(notes).get('note', 'No note found.')
        return "No culture notes found."
    except Exception as e:
        return f"Error loading culture notes: {e}"


