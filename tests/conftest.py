import pytest
from google.adk.tools.tool_context import ToolContext

@pytest.fixture
def tool_context():
    return ToolContext(state={"user_preference_temperature_unit": "Celsius"})
