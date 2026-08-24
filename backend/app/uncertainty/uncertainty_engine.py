def calculate_uncertainty(observation_validation: dict, fusion_data: dict) -> dict:
    """
    Research Gap 3: Forecast Uncertainty Engine.
    Estimates uncertainty based on source disagreement and observation mismatch.
    """
    uncertainty_score = 0
    reasons = []
    
    # 1. Source Disagreement Penalty
    if fusion_data.get("source_disagreement") == "HIGH":
        uncertainty_score += 40
        reasons.append("High disagreement between forecast models.")
    else:
        reasons.append("Forecast sources broadly agree.")
        
    # 2. Observation Error Penalty
    mae = observation_validation.get("mae_temperature", 0)
    if mae > 2.0:
        uncertainty_score += 30
        reasons.append(f"Recent observations deviate from forecast by {mae}°C.")
    else:
        reasons.append("Recent observations validate the forecast trend.")
        
    # Categorize
    if uncertainty_score < 30:
        confidence = "HIGH"
    elif uncertainty_score < 60:
        confidence = "MODERATE"
    else:
        confidence = "LOW"
        
    return {
        "uncertainty_score": uncertainty_score,
        "confidence": confidence,
        "reasons": reasons
    }
