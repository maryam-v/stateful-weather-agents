import logging
from google.adk.runners import Runner
from google.genai import types

logger = logging.getLogger(__name__)

async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str) -> str:
    """Send a query to the agent runner and return the final response text."""
    logger.info("User query: %s", query)

    content = types.Content(role="user", parts=[types.Part(text=query)])
    final_response_text = "Agent did not produce a final response."

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break

    logger.info("Agent response: %s", final_response_text)
    return final_response_text
