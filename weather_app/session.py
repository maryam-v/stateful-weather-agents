import logging
from typing import Dict, Any, Optional
from google.adk.sessions import InMemorySessionService

logger = logging.getLogger(__name__)

class SessionManager:
    """Manages user sessions and state for agents."""

    def __init__(self, app_name: str):
        self.app_name = app_name
        self.service = InMemorySessionService()
        logger.info("SessionManager initialized for app '%s'", app_name)

    async def create_session(
        self,
        user_id: str,
        session_id: str,
        initial_state: Optional[Dict[str, Any]] = None
    ):
        """Create a new session with optional initial state."""
        session = await self.service.create_session(
            app_name=self.app_name,
            user_id=user_id,
            session_id=session_id,
            state=initial_state or {}
        )
        logger.info("Session '%s' created for user '%s'", session_id, user_id)
        return session

    async def get_session(self, user_id: str, session_id: str):
        """Retrieve an existing session."""
        return await self.service.get_session(
            app_name=self.app_name,
            user_id=user_id,
            session_id=session_id
        )

    async def update_state(self, user_id: str, session_id: str, updates: Dict[str, Any]):
        """Update session state with new values."""
        session = await self.get_session(user_id, session_id)
        if not session:
            logger.warning("Session '%s' not found for user '%s'", session_id, user_id)
            return None
        for key, value in updates.items():
            session.state[key] = value
            logger.info("Updated state key '%s' -> %s", key, value)
        return session.state

    async def get_state(self, user_id: str, session_id: str) -> Dict[str, Any]:
        """Return the current state dict for a session."""
        session = await self.get_session(user_id, session_id)
        return session.state if session else {}

