def calculate_uncertainty(observation_validation: dict, fusion_data: dict) -> dict:
    """
    Step 10: Forecast Uncertainty Engine.
    Estimates uncertainty based on source disagreement and observation mismatch.
    Outputs a score from 0 (Perfect Confidence) to 100 (Total Uncertainty).
    """
    uncertainty_score = 0
    reasons = []
    
    # 1. Source Disagreement Penalty
    disagreement = fusion_data.get("source_disagreement", "UNKNOWN")
    if disagreement == "HIGH":
        uncertainty_score += 40
        reasons.append("High disagreement between forecast models.")
    elif disagreement == "MODERATE":
        uncertainty_score += 20
        reasons.append("Moderate disagreement between forecast models.")
    else:
        reasons.append("Forecast sources broadly agree.")
        
    # 2. Observation Error Penalty
    if observation_validation.get("status") == "SUCCESS":
        mae = observation_validation.get("mae_temperature", 0)
        if mae > 2.5:
            uncertainty_score += 40
            reasons.append(f"Recent observations heavily deviate from forecast (MAE: {mae}°C).")
        elif mae > 1.0:
            uncertainty_score += 20
            reasons.append(f"Minor deviation in recent observations (MAE: {mae}°C).")
        else:
            reasons.append("Recent observations perfectly validate the forecast trend.")
    else:
        uncertainty_score += 15
        reasons.append("Missing live observation data to validate forecast.")
        
    # Clamp score
    uncertainty_score = min(uncertainty_score, 100)
        
    # Categorize Confidence (Inverted from Uncertainty)
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
