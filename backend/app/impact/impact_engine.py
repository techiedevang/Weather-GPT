def determine_impact(fusion_data: dict, user_type: str, activity: str) -> dict:
    """
    Research Gap 1: Forecast-to-Impact Translation.
    Maps meteorological values to specific user impacts.
    """
    rain_prob = fusion_data.get("consensus_rain_probability", 0)
    
    impact = "None"
    action = "Proceed as normal."
    
    if rain_prob > 60:
        if user_type == "farmer" and activity == "pesticide_spray":
            impact = "High risk of pesticide washout."
            action = "Postpone spraying operations."
        elif user_type == "traveller" and activity == "outdoor_event":
            impact = "Potential event disruption and waterlogging."
            action = "Avoid non-essential travel or seek indoor alternatives."
        else:
            impact = "General rain disruption."
            action = "Carry umbrella and plan for delays."
            
    return {
        "user_type": user_type,
        "activity": activity,
        "identified_impact": impact,
        "recommended_action": action
    }
