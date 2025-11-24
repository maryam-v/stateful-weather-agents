import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# App constants
APP_NAME = "weather_app"
DEFAULT_USER_ID = "user_demo"
DEFAULT_SESSION_ID = "session_demo"

# Default state schema
DEFAULT_INITIAL_STATE = {
    "user_preference_temperature_unit": "Celsius",
    "user_preference_location": "Montreal",
    "notifications_enabled": True,
    "conversation_summary": []
}
