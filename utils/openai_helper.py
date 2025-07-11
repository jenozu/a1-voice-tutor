import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
def get_openai_client():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return openai.OpenAI(api_key=api_key) 