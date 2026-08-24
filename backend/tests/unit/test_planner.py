import pytest
from app.planner.event_classifier import classify_calendar_event
from app.planner.time_slot_optimizer import optimize_time_window

def test_event_classifier():
    assert classify_calendar_event("Morning Run with friends") == "outdoor_exercise"
    assert classify_calendar_event("Pesticide Spray Field B") == "agriculture"
    assert classify_calendar_event("Flight to Mumbai") == "travel"
    assert classify_calendar_event("Office Meeting") == "general"

def test_time_slot_optimizer_finds_safest_window():
    timeline = [
        {"time": "14:00", "risk_score": 85}, # High risk
        {"time": "15:00", "risk_score": 60}, # Moderate risk
        {"time": "16:00", "risk_score": 15}, # Safe window
        {"time": "17:00", "risk_score": 40}  # Moderate risk
    ]
    
    best = optimize_time_window(timeline)
    assert best["time"] == "16:00"
    assert best["risk_score"] == 15
