from typing import List
from app.schemas.advisory import RiskScore

def get_advisories(domain: str, risk: RiskScore) -> List[str]:
    advice = []
    
    if domain in ["travel", "citizen"]:
        if risk.level in ["High", "Critical"]:
            advice.append("Avoid non-essential travel if possible.")
        if "High chance of rain" in risk.factors:
            advice.append("Carry an umbrella or raincoat and expect traffic delays.")
        if "Extreme heat" in risk.factors:
            advice.append("Stay hydrated and avoid direct sun exposure during peak hours.")
            
    elif domain == "farmer":
        if "High chance of rain" in risk.factors:
            advice.append("Postpone pesticide or fertilizer spraying until weather clears.")
        if "Strong winds" in risk.factors:
            advice.append("Secure loose farm equipment and structures.")
        if risk.level == "Low":
            advice.append("Conditions are favorable for normal agricultural activities.")
            
    if not advice:
        advice.append("No specific warnings at this time. Stay updated.")
        
    return advice
