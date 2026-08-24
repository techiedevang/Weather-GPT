def detect_conflict(event_category: str, risk_score: int) -> bool:
    """
    Determines if a weather risk score actively conflicts with an event type.
    """
    # MVP thresholds
    if event_category in ["outdoor_exercise", "outdoor_event", "agriculture"]:
        return risk_score > 30 # Moderate/High risk disrupts outdoor events
        
    if event_category == "travel":
        return risk_score > 50 # Travel requires higher risk to be disrupted
        
    return risk_score > 70
