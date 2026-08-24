from app.schemas.evidence import EvidenceCollection

def calculate_risk_level(fusion_data: dict, evidence: EvidenceCollection) -> dict:
    """
    Step 12: Risk Engine.
    Calculates overall WeatherGPT risk severity based on weather data and keeps official warnings separate.
    """
    rain_prob = fusion_data.get("consensus_rain_probability", 0)
    temp = fusion_data.get("consensus_temperature", 25)
    
    risk_score = 0
    
    # 1. Weather variable severity
    if rain_prob > 80:
        risk_score += 60
    elif rain_prob > 50:
        risk_score += 30
        
    if temp > 40:
        risk_score += 40
    elif temp > 35:
        risk_score += 20
        
    # Classify WeatherGPT Risk
    if risk_score >= 80:
        level = "CRITICAL"
    elif risk_score >= 50:
        level = "HIGH"
    elif risk_score >= 25:
        level = "MODERATE"
    else:
        level = "LOW"
        
    # 2. Official warning severity (kept separate as per build plan)
    alerts = evidence.get_alerts()
    official_severity = "NONE"
    if alerts and alerts[0].alert:
        official_severity = alerts[0].alert.severity.upper()
        
    return {
        "risk_score": min(risk_score, 100),
        "risk_level": level,
        "official_severity": official_severity
    }
