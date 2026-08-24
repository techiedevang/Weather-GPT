import pytest
from app.tools.forecast_tool import forecast_tool
from app.ai.tool_router import route_tool

def test_forecast_tool():
    result = forecast_tool("Noida", "tomorrow")
    assert result["location"] == "Noida"
    assert result["forecast_time"] == "tomorrow"
    assert "temperature" in result

def test_tool_router_advisory():
    # Advisory intent should append advisory data
    result = route_tool("farmer_advisory", "Pune", "today")
    assert result["location"] == "Pune"
    assert "advisory" in result
    assert result["advisory"]["domain"] == "farmer"

def test_tool_router_current_weather():
    result = route_tool("current_weather", "Delhi", "now")
    assert result["location"] == "Delhi"
    # Current weather tool shouldn't append advisory by default
    assert "advisory" not in result
