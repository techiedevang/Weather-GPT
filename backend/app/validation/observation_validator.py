from app.schemas.evidence import EvidenceCollection

def validate_forecast_against_observation(evidence: EvidenceCollection) -> dict:
    """
    Research Gap 2: Hyperlocal Reliability.
    Calculates the error between the current forecast and current observations.
    """
    forecasts = evidence.get_forecasts()
    observations = evidence.get_observations()
    
    if not forecasts or not observations:
        return {"status": "INSUFFICIENT_DATA"}
        
    # Simple MVP: Compare first forecast's temp against first observation's temp
    forecast_temp = forecasts[0].weather.temperature_celsius
    obs_temp = observations[0].weather.temperature_celsius
    
    mae = abs(forecast_temp - obs_temp)
    
    agreement = "GOOD" if mae < 2.0 else "POOR"
    
    return {
        "mae_temperature": mae,
        "rmse_temperature": mae ** 2, # simplified for MVP
        "bias": forecast_temp - obs_temp,
        "agreement_status": agreement
    }
