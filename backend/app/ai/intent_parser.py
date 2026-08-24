import re

def parse_intent(query: str) -> str:
    """
    Step 13: Intent Parser.
    Determines what the user is actually asking for to route to the correct tool.
    """
    query_lower = query.lower()
    
    if any(word in query_lower for word in ["plan", "calendar", "time", "when"]):
        return "planner"
    elif any(word in query_lower for word in ["alert", "warning", "danger", "cyclone", "flood"]):
        return "alert"
    elif any(word in query_lower for word in ["farmer", "crop", "spray", "agriculture"]):
        return "agriculture"
    elif any(word in query_lower for word in ["travel", "flight", "drive", "road"]):
        return "travel"
    else:
        return "weather_general"
