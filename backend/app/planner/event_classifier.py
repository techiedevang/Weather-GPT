def classify_calendar_event(event_title: str) -> str:
    """
    Classifies a raw calendar event into a standardized activity type.
    """
    title = event_title.lower()
    
    if any(keyword in title for keyword in ["run", "jog", "hike", "trek", "walk"]):
        return "outdoor_exercise"
    elif any(keyword in title for keyword in ["spray", "farm", "crop", "harvest"]):
        return "agriculture"
    elif any(keyword in title for keyword in ["flight", "airport", "drive", "commute"]):
        return "travel"
    elif any(keyword in title for keyword in ["wedding", "picnic", "beach", "party"]):
        return "outdoor_event"
        
    return "general"
