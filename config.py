# /config.py
import os
from dotenv import load_dotenv

# Load environment variables from a .env file for local development
load_dotenv()

# --- API KEY CONFIGURATION ---
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
LUSHA_API_KEY = os.getenv('LUSHA_API_KEY')

# --- APPLICATION SETTINGS ---
CONNECTIONS_CSV_PATH = os.path.join('data', 'linkedin_connections.csv')
DEMO_COMPANY_NAME = "commonwealth bank" # Lowercase for easy comparison

# --- VALIDATION ---
def check_api_keys():
    """Checks if essential API keys are set and prints a warning if not."""
    if not all([GOOGLE_API_KEY, GOOGLE_CSE_ID, GEMINI_API_KEY]):
        print("\nWARNING: One or more environment variables are missing.")
        print("Please set GOOGLE_API_KEY, GOOGLE_CSE_ID, and GEMINI_API_KEY in your .env file for full functionality.\n")