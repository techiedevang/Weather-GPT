from app.planner.event_classifier import classify_calendar_event
from app.planner.conflict_detector import detect_conflict
from app.planner.time_slot_optimizer import optimize_time_window

def evaluate_calendar_event(event_title: str, planned_time: str, hourly_weather_timeline: list) -> dict:
    """
    Step 16 & 17 Master Service: Personal Weather Planner.
    Evaluates an event against a timeline of weather risks and finds the safest slot.
    """
    category = classify_calendar_event(event_title)
    
    # 1. Check if the currently planned time conflicts
    planned_slot = next((slot for slot in hourly_weather_timeline if slot["time"] == planned_time), None)
    
    if not planned_slot:
        # If the exact time isn't in the mock, just use the first available as the planned time
        planned_slot = hourly_weather_timeline[0]
        planned_time = planned_slot["time"]
        
    has_conflict = detect_conflict(category, planned_slot["risk_score"])
    
    if not has_conflict:
        return {
            "status": "SAFE",
            "message": f"Your planned time ({planned_time}) looks safe for {category}.",
            "recommended_time": planned_time
        }
        
    # 2. If there is a conflict, run the Optimizer
    best_slot = optimize_time_window(hourly_weather_timeline)
    
    if best_slot["time"] == planned_time:
         return {
            "status": "NO_BETTER_ALTERNATIVES",
            "message": f"High risk at {planned_time}, but no safer windows are available today.",
            "recommended_time": planned_time,
            "recommended_risk": best_slot["risk_score"]
        }
    
    return {
        "status": "CONFLICT_DETECTED",
        "message": f"High risk ({planned_slot['risk_score']}/100) at planned time. {best_slot['time']} is recommended because the weather risk is lower ({best_slot['risk_score']}/100).",
        "planned_time": planned_time,
        "recommended_time": best_slot["time"],
        "recommended_risk": best_slot["risk_score"]
    }
