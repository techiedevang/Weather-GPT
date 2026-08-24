from typing import Dict, Any
from app.engine.risk_engine import calculate_risk
from app.engine.rules import get_advisories
from app.schemas.advisory import AdvisoryResult

def get_advisory_for_weather(weather_data: Dict[str, Any], intent: str) -> Dict[str, Any]:
    # Determine domain based on intent
    domain = "farmer" if intent == "farmer_advisory" else "travel"
    
    # Calculate risk
    risk = calculate_risk(weather_data)
    
    # Generate advice
    advice_list = get_advisories(domain, risk)
    
    result = AdvisoryResult(domain=domain, risk=risk, advice=advice_list)
    return result.model_dump()
