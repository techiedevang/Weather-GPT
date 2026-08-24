from app.schemas.evidence import EvidenceCollection

def calculate_risk_level(fusion_data: dict, evidence: EvidenceCollection) -> dict:
    """
    Calculates overall WeatherGPT risk severity based on weather data and official warnings.
    """
    rain_prob = fusion_data.get("consensus_rain_probability", 0)
    temp = fusion_data.get("consensus_temperature", 25)
    
    risk_score = 0
    
    # 1. Weather variable severity
    if rain_prob > 80:
        risk_score += 40
    elif rain_prob > 50:
        risk_score += 20
        
    if temp > 40:
        risk_score += 30
        
    # 2. Official warning severity (takes precedence)
    alerts = evidence.get_alerts()
    if alerts:
        severity = alerts[0].alert.severity.upper()
        if severity == "CRITICAL":
            risk_score += 60
        elif severity == "HIGH":
            risk_score += 40
            
    # Classify Risk
    if risk_score >= 70:
        level = "CRITICAL"
    elif risk_score >= 40:
        level = "HIGH"
    elif risk_score >= 20:
        level = "MODERATE"
    else:
        level = "LOW"
        
    return {
        "risk_score": risk_score,
        "risk_level": level
    }
