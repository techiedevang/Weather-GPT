import pytest
from app.engine.risk_engine import calculate_risk
from app.engine.rules import get_advisories
from app.schemas.advisory import RiskScore

def test_risk_engine_critical():
    weather_data = {
        "temperature": 40,
        "rain_probability": 90,
        "wind_speed": 60,
        "warning_severity": 0.8
    }
    risk = calculate_risk(weather_data)
    assert risk.level in ["High", "Critical"]
    assert "Extreme heat" in risk.factors
    assert "High chance of rain" in risk.factors

def test_risk_engine_low():
    weather_data = {
        "temperature": 25,
        "rain_probability": 10,
        "wind_speed": 10,
        "warning_severity": 0
    }
    risk = calculate_risk(weather_data)
    assert risk.level == "Low"
    assert "Normal weather conditions" in risk.factors

def test_advisory_rules_farmer():
    risk = RiskScore(level="Moderate", score=0.4, factors=["High chance of rain"])
    advice = get_advisories("farmer", risk)
    assert any("Postpone pesticide" in a for a in advice)

def test_advisory_rules_travel():
    risk = RiskScore(level="Critical", score=0.9, factors=["Extreme heat", "High chance of rain"])
    advice = get_advisories("travel", risk)
    assert any("Avoid non-essential travel" in a for a in advice)
