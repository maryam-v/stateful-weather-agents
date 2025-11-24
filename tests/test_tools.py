import pytest
from tools import say_hello, say_goodbye, get_weather_stateful, get_forecast_stateful
from google.adk.tools.tool_context import ToolContext

def test_say_hello_with_name():
    assert say_hello("Maryam") == "Hello, Maryam!"

def test_say_hello_without_name():
    assert say_hello() == "Hello there!"

def test_say_goodbye():
    assert say_goodbye() == "Goodbye! Have a great day."

def test_get_weather_stateful_mock(monkeypatch):
    # Mock requests.get to avoid real API call
    class MockResponse:
        def raise_for_status(self): pass
        def json(self): return {"main": {"temp": 10}, "weather": [{"description": "clear sky"}]}
    monkeypatch.setattr("requests.get", lambda *a, **k: MockResponse())

    tool_context = ToolContext(state={"user_preference_temperature_unit": "Celsius"})
    result = get_weather_stateful("London", tool_context)
    assert result["status"] == "success"
    assert "London" in result["report"]

def test_get_forecast_stateful_mock(monkeypatch):
    class MockResponse:
        def raise_for_status(self): pass
        def json(self):
            return {"list": [{"main": {"temp": 10}, "weather": [{"description": "clear sky"}]}] * 24}
    monkeypatch.setattr("requests.get", lambda *a, **k: MockResponse())

    tool_context = ToolContext(state={"user_preference_temperature_unit": "Fahrenheit"})
    result = get_forecast_stateful("Tokyo", tool_context)
    assert result["status"] == "success"
    assert "Tokyo" in result["report"]
