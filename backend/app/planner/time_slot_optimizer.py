from typing import List, Dict

def optimize_time_window(hourly_risks: List[Dict]) -> Dict:
    """
    Step 17: Time-Slot Optimizer.
    Takes a list of time slots and their associated weather risks.
    Returns the safest contiguous time window based on constraints.
    
    hourly_risks example:
    [
      {"time": "16:00", "risk_score": 76},
      {"time": "16:30", "risk_score": 15},
      {"time": "17:00", "risk_score": 31}
    ]
    """
    if not hourly_risks:
        return {}
        
    # In a full implementation, this checks event duration (e.g. 2 hours) and finds a contiguous block.
    # For MVP, we extract the absolute minimum risk slot.
    best_slot = min(hourly_risks, key=lambda x: x.get("risk_score", 100))
    
    return best_slot
