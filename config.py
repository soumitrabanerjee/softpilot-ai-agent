# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM Provider Selection ---
# Change this to "openai" if you want to switch back later
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google") # Default to Google

# --- API Keys ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- Model Configuration ---
# We can specify different models for each provider
MODEL_CONFIG = {
    "openai": "gpt-4o",
    "google": "gemini-1.5-flash-latest" # A fast and capable free-tier model
}

DEFAULT_MODEL = MODEL_CONFIG.get(LLM_PROVIDER)