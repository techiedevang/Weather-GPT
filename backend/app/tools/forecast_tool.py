from typing import Dict, Any

def forecast_tool(location: str, time: str) -> Dict[str, Any]:
    # Mock implementation as per requirements
    # "Later the tool implementation will be connected to the real weather/NWP service."
    return {
        "location": location if location else "Unknown",
        "temperature": 31,
        "rain_probability": 72,
        "wind_speed": 18,
        "forecast_time": time if time else "tomorrow evening",
        "condition": "Cloudy with chance of rain"
    }

def current_weather_tool(location: str) -> Dict[str, Any]:
    return {
        "location": location if location else "Unknown",
        "temperature": 28,
        "humidity": 65,
        "wind_speed": 12,
        "condition": "Clear skies"
    }
