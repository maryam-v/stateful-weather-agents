import asyncio
import logging
from dotenv import load_dotenv

from agents import root_agent_stateful
from session import SessionManager
from runner import call_agent_async
from google.adk.runners import Runner

from config import APP_NAME, DEFAULT_USER_ID, DEFAULT_SESSION_ID, DEFAULT_INITIAL_STATE

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from .env
# load_dotenv()

async def run_demo():
    # Initialize session manager
    manager = SessionManager(APP_NAME)
    await manager.create_session(
        user_id=DEFAULT_USER_ID,
        session_id=DEFAULT_SESSION_ID,
        initial_state=DEFAULT_INITIAL_STATE
    )

    # Create runner
    runner = Runner(agent=root_agent_stateful, app_name=APP_NAME, session_service=manager.service)

    # Interact
    await call_agent_async("What's the weather in London?", runner, DEFAULT_USER_ID, DEFAULT_SESSION_ID)
    # await manager.update_state(USER_ID, SESSION_ID, {"user_preference_temperature_unit": "Fahrenheit"})
    # await call_agent_async("Give me a 3-day forecast for Tokyo.", runner, USER_ID, SESSION_ID)
    # await call_agent_async("Hi!", runner, USER_ID, SESSION_ID)

    # Inspect final state
    state = await manager.get_state(DEFAULT_USER_ID, DEFAULT_SESSION_ID)
    print("\n--- Final Session State ---")
    for k, v in state.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    asyncio.run(run_demo())
