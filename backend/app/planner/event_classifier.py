def classify_calendar_event(event_title: str) -> str:
    """
    Step 16: Event Classifier.
    Classifies a raw calendar event into a standardized activity type.
    """
    title = event_title.lower()
    
    if any(keyword in title for keyword in ["run", "jog", "hike", "trek", "walk", "exercise", "sports"]):
        return "outdoor_exercise"
    elif any(keyword in title for keyword in ["spray", "farm", "crop", "harvest", "irrigate", "tractor"]):
        return "agriculture"
    elif any(keyword in title for keyword in ["flight", "airport", "drive", "commute", "train"]):
        return "travel"
    elif any(keyword in title for keyword in ["wedding", "picnic", "beach", "party", "festival"]):
        return "outdoor_event"
        
    return "general"
