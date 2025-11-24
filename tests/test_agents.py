from agents import greeting_agent, farewell_agent, forecast_agent, root_agent_stateful

def test_agents_exist():
    assert greeting_agent.name == "greeting_agent"
    assert farewell_agent.name == "farewell_agent"
    assert forecast_agent.name == "forecast_agent"
    assert root_agent_stateful.name == "weather_agent_stateful"
