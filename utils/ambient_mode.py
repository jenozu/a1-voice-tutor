import threading

# In-memory state for ambient mode
_ambient_active = False
_ambient_thread = None

def start_ambient_mode(user_profile, persona, on_user_speech, on_ai_response):
    """
    Start ambient mode: listens for user speech, responds with AI persona.
    Args:
        user_profile (dict): User profile info
        persona (str): AI voice persona (e.g., 'Tutor Magda')
        on_user_speech (callable): Function to call with user speech (str)
        on_ai_response (callable): Function to call with AI response (str)
    """
    global _ambient_active, _ambient_thread
    if _ambient_active:
        return False
    _ambient_active = True
    def ambient_loop():
        while _ambient_active:
            try:
                # Simulate listening for user speech (replace with real STT)
                user_speech = on_user_speech()
                if user_speech is None:
                    continue
                # Generate AI response (stub)
                ai_response = generate_ai_response(user_speech, persona)
                on_ai_response(ai_response)
            except Exception as e:
                print(f"Ambient mode error: {e}")
                break
    _ambient_thread = threading.Thread(target=ambient_loop, daemon=True)
    _ambient_thread.start()
    return True

def stop_ambient_mode():
    """
    Stop the ambient mode session.
    """
    global _ambient_active
    _ambient_active = False

def is_ambient_active():
    """
    Check if ambient mode is running.
    Returns:
        bool: True if running, False otherwise
    """
    global _ambient_active
    return _ambient_active

def generate_ai_response(user_speech, persona):
    """
    Stub for AI response generation. Replace with LLM or scripted dialog.
    Args:
        user_speech (str): What the user said
        persona (str): AI persona name
    Returns:
        str: AI response
    """
    # Simple scripted response for demo
    if persona == 'Tutor Magda':
        return f"Magda: Ciekawa odpowiedź! Powiedz mi więcej o tym: '{user_speech}'."
    elif persona == 'Coach Piotr':
        return f"Piotr: Świetnie! Spróbuj teraz powiedzieć to inaczej. '{user_speech}'"
    elif persona == 'Professor Jan':
        return f"Jan: Bardzo dobrze. Czy możesz rozwinąć swoją wypowiedź? '{user_speech}'"
    else:
        return f"AI: Interesting! Tell me more about: '{user_speech}'." 