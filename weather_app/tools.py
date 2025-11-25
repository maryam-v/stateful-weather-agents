import os
import requests
import logging
from typing import Optional
from google.adk.tools.tool_context import ToolContext
from weather_app.config import OPENWEATHER_API_KEY

logger = logging.getLogger(__name__)

def say_hello(name: Optional[str] = None) -> str:
    """Return a friendly greeting message."""
    if name:
        logger.info("say_hello called with name: %s", name)
        return f"Hello, {name}!"
    logger.info("say_hello called without a specific name")
    return "Hello there!"

def say_goodbye() -> str:
    """Return a polite farewell message."""
    logger.info("say_goodbye called")
    return "Goodbye! Have a great day."

def get_weather_stateful(city: str, tool_context: ToolContext) -> dict:
    """Retrieve current weather from OpenWeatherMap, respecting unit preference in session state."""
    logger.info("get_weather_stateful called for city: %s", city)

    preferred_unit = tool_context.state.get("user_preference_temperature_unit", "Celsius")
    api_key = OPENWEATHER_API_KEY
    if not api_key:
        return {"status": "error", "error_message": "Missing OPENWEATHER_API_KEY."}
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        temp_c = data["main"]["temp"]
        condition = data["weather"][0]["description"].capitalize()

        temp_value = (temp_c * 9/5) + 32 if preferred_unit == "Fahrenheit" else temp_c
        temp_unit = "°F" if preferred_unit == "Fahrenheit" else "°C"

        report = f"The weather in {city.capitalize()} is {condition} with a temperature of {temp_value:.0f}{temp_unit}."
        tool_context.state["last_city_checked_stateful"] = city
        return {"status": "success", "report": report}

    except Exception as e:
        logger.error("Weather API call failed: %s", e)
        return {"status": "error", "error_message": str(e)}

def get_forecast_stateful(city: str, tool_context: ToolContext) -> dict:
    """Retrieve a 3-day forecast from OpenWeatherMap, respecting unit preference in session state."""
    logger.info("get_forecast_stateful called for city: %s", city)

    preferred_unit = tool_context.state.get("user_preference_temperature_unit", "Celsius")
    api_key = OPENWEATHER_API_KEY
    if not api_key:
        return {"status": "error", "error_message": "Missing OPENWEATHER_API_KEY."}
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        forecasts = []
        for i in range(0, 24, 8):  # 3 days
            temp_c = data["list"][i]["main"]["temp"]
            condition = data["list"][i]["weather"][0]["description"].capitalize()

            temp_value = (temp_c * 9/5) + 32 if preferred_unit == "Fahrenheit" else temp_c
            temp_unit = "°F" if preferred_unit == "Fahrenheit" else "°C"

            forecasts.append(f"{condition}, {temp_value:.0f}{temp_unit}")

        report = f"3-day forecast for {city.capitalize()}: " + "; ".join(forecasts)
        tool_context.state["last_forecast_city"] = city
        tool_context.state["last_forecast_report"] = report
        return {"status": "success", "report": report}

    except Exception as e:
        logger.error("Forecast API call failed: %s", e)
        return {"status": "error", "error_message": str(e)}
