import logging
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from weather_app.tools import (
    say_hello,
    say_goodbye,
    get_weather_stateful,
    get_forecast_stateful,
)

logger = logging.getLogger(__name__)

# Model constants
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

# Greeting Agent
greeting_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="greeting_agent",
    instruction="Provide a friendly greeting using the 'say_hello' tool.",
    description="Handles simple greetings.",
    tools=[say_hello],
)
logger.info("Greeting agent created.")

# Farewell Agent
farewell_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="farewell_agent",
    instruction="Provide a polite goodbye using the 'say_goodbye' tool.",
    description="Handles farewells.",
    tools=[say_goodbye],
)
logger.info("Farewell agent created.")

# Forecast Agent
forecast_agent = Agent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="forecast_agent",
    instruction="Provide multi-day forecasts using the 'get_forecast_stateful' tool.",
    description="Handles forecast queries.",
    tools=[get_forecast_stateful],
)
logger.info("Forecast agent created.")

# Root Agent
root_agent_stateful = Agent(
    name="weather_agent_stateful",
    model=Gemini(model="gemini-2.5-flash-lite"),
    description="Main agent: provides weather, delegates greetings/farewells/forecasts, saves report to state.",
    instruction=(
        "Provide current weather using 'get_weather_stateful'. "
        "Delegate greetings to 'greeting_agent', farewells to 'farewell_agent', "
        "and forecasts to 'forecast_agent'. "
        "Handle only weather, forecasts, greetings, and farewells."
    ),
    tools=[get_weather_stateful],
    sub_agents=[greeting_agent, farewell_agent, forecast_agent],
    output_key="last_weather_report",
)
logger.info("Root agent created.")
