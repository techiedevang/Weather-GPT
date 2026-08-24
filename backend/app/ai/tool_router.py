from app.tools.forecast_tool import forecast_tool, current_weather_tool
from app.tools.advisory_tool import get_advisory_for_weather
from app.tools.climate_tool import get_climate_trends
from typing import Dict, Any

def route_tool(intent: str, location: str, time: str) -> Dict[str, Any]:
    # 1. Fetch base weather data depending on time/intent
    if intent == "current_weather":
        data = current_weather_tool(location)
    elif intent == "climate_analytics":
        data = get_climate_trends(location, time)
    else:
        # Default fallback to forecast for most intents (rain_query, alert_query, advisories, forecast)
        data = forecast_tool(location, time)
        
    # 2. If the user is asking for advice/alerts, append advisory analysis
    if intent in ["travel_advisory", "farmer_advisory", "alert_query"]:
        advisory_data = get_advisory_for_weather(data, intent)
        data["advisory"] = advisory_data
        
    return data
