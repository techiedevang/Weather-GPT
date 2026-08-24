from typing import Dict, Any
from app.schemas.advisory import RiskScore

def calculate_risk(weather_data: Dict[str, Any]) -> RiskScore:
    # Prototype deterministic risk score
    # weather_data expected to have temperature, rain_probability, wind_speed, etc.
    
    # Defaults
    temp = weather_data.get("temperature", 25)
    rain_prob = weather_data.get("rain_probability", 0)
    wind = weather_data.get("wind_speed", 0)
    warning_severity = weather_data.get("warning_severity", 0) # 0 to 1 scale
    
    # Severity scaling (0 to 1)
    temp_severity = max(0, (temp - 35) / 15) if temp > 35 else 0
    rain_severity = rain_prob / 100
    wind_severity = min(1, wind / 100)
    
    risk_score_value = (
        (rain_severity * 0.30) +
        (wind_severity * 0.20) +
        (temp_severity * 0.15) +
        (warning_severity * 0.35)
    )
    
    # Classify
    if risk_score_value > 0.75:
        level = "Critical"
    elif risk_score_value > 0.5:
        level = "High"
    elif risk_score_value > 0.25:
        level = "Moderate"
    else:
        level = "Low"
        
    factors = []
    if temp_severity > 0.3:
        factors.append("Extreme heat")
    if rain_severity > 0.5:
        factors.append("High chance of rain")
    if wind_severity > 0.4:
        factors.append("Strong winds")
    if warning_severity > 0:
        factors.append("Official weather warning active")
        
    if not factors:
        factors.append("Normal weather conditions")
        
    return RiskScore(level=level, score=round(risk_score_value, 2), factors=factors)
