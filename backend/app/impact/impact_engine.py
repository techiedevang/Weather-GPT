def determine_impact(fusion_data: dict, user_type: str, activity: str) -> dict:
    """
    Step 11: Forecast-to-Impact Translation (Impact Engine).
    Maps meteorological values to specific user impacts based on context.
    """
    rain_prob = fusion_data.get("consensus_rain_probability", 0)
    temp = fusion_data.get("consensus_temperature", 25)
    
    impact = "None"
    action = "Proceed as normal."
    
    user_lower = user_type.lower()
    activity_lower = activity.lower()
    
    # Context Logic
    if rain_prob > 60:
        if user_lower == "farmer" and "spray" in activity_lower:
            impact = "High risk of pesticide washout due to expected rain."
            action = "Postpone spraying operations until the weather clears."
        elif user_lower == "traveller" or "travel" in activity_lower:
            impact = "Potential delays and waterlogging on travel routes."
            action = "Avoid non-essential travel or use major highways."
        else:
            impact = "General rain disruption expected."
            action = "Carry an umbrella and plan for minor delays."
            
    elif temp > 40:
        if "exercise" in activity_lower or "outdoor" in activity_lower:
            impact = "Extreme heat exposure risk during outdoor activity."
            action = "Shift activity to early morning or late evening."
        elif user_lower == "farmer":
            impact = "Heat stress risk for crops and livestock."
            action = "Ensure adequate irrigation and shade."
            
    return {
        "user_type": user_type,
        "activity": activity,
        "identified_impact": impact,
        "recommended_action": action
    }
