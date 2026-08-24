import math
from app.schemas.evidence import EvidenceCollection

def validate_forecast_against_observation(evidence: EvidenceCollection) -> dict:
    """
    Step 08: Observation Validator.
    Calculates the error between the forecast and actual observations (MAE, RMSE, Bias).
    """
    forecasts = evidence.get_forecasts()
    observations = evidence.get_observations()
    
    if not forecasts or not observations:
        return {"status": "INSUFFICIENT_DATA"}
        
    # Extract temperature for validation
    f_temp = forecasts[0].weather.temperature_celsius if forecasts[0].weather else None
    o_temp = observations[0].weather.temperature_celsius if observations[0].weather else None
    
    if f_temp is None or o_temp is None:
        return {"status": "MISSING_VARIABLES"}
    
    # Calculate Error Metrics
    bias = round(f_temp - o_temp, 2)
    mae = round(abs(bias), 2)
    rmse = round(math.sqrt(mae ** 2), 2)
    
    agreement = "POOR"
    if mae < 1.0:
        agreement = "EXCELLENT"
    elif mae <= 2.5:
        agreement = "GOOD"
        
    return {
        "status": "SUCCESS",
        "mae_temperature": mae,
        "rmse_temperature": rmse,
        "bias": bias,
        "agreement_status": agreement
    }
