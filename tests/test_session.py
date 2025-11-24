import pytest
import asyncio
from session import SessionManager

APP_NAME = "test_app"
USER_ID = "test_user"
SESSION_ID = "test_session"

@pytest.mark.asyncio
async def test_session_create_and_update():
    manager = SessionManager(APP_NAME)
    await manager.create_session(USER_ID, SESSION_ID, {"user_preference_temperature_unit": "Celsius"})
    state = await manager.get_state(USER_ID, SESSION_ID)
    assert state["user_preference_temperature_unit"] == "Celsius"

    await manager.update_state(USER_ID, SESSION_ID, {"user_preference_temperature_unit": "Fahrenheit"})
    state = await manager.get_state(USER_ID, SESSION_ID)
    assert state["user_preference_temperature_unit"] == "Fahrenheit"
