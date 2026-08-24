from app.planner.event_classifier import classify_calendar_event
from app.planner.conflict_detector import detect_conflict
from app.planner.time_slot_optimizer import optimize_time_window

def evaluate_calendar_event(event_title: str, planned_time: str, hourly_weather_timeline: list) -> dict:
    """
    Master service for the Personal Weather Planner.
    Takes a calendar event and a timeline of weather, and recommends the safest window.
    """
    category = classify_calendar_event(event_title)
    
    # Check if the currently planned time conflicts
    planned_slot = next((slot for slot in hourly_weather_timeline if slot["time"] == planned_time), None)
    
    if not planned_slot:
        return {"status": "NO_DATA", "message": "Weather timeline not available for planned time."}
        
    has_conflict = detect_conflict(category, planned_slot["risk_score"])
    
    if not has_conflict:
        return {
            "status": "SAFE",
            "message": "Your planned time looks safe.",
            "recommended_time": planned_time
        }
        
    # If there is a conflict, optimize for a better slot
    best_slot = optimize_time_window(hourly_weather_timeline)
    
    return {
        "status": "CONFLICT_DETECTED",
        "message": f"High risk ({planned_slot['risk_score']}/100) at planned time. {best_slot['time']} is the safer available window.",
        "planned_time": planned_time,
        "recommended_time": best_slot["time"],
        "recommended_risk": best_slot["risk_score"]
    }
