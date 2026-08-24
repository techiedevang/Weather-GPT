from typing import List, Dict

def optimize_time_window(hourly_risks: List[Dict]) -> Dict:
    """
    Takes a list of time slots and their associated weather risks.
    Returns the safest contiguous time window.
    
    hourly_risks example:
    [
      {"time": "16:00", "risk_score": 22},
      {"time": "16:30", "risk_score": 15},
      {"time": "17:00", "risk_score": 31}
    ]
    """
    if not hourly_risks:
        return {}
        
    # Find the time slot with the absolute minimum risk
    best_slot = min(hourly_risks, key=lambda x: x["risk_score"])
    
    return best_slot
