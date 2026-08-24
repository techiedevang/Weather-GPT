from app.schemas.evidence import EvidenceCollection

def fuse_forecasts(evidence: EvidenceCollection) -> dict:
    """
    Step 09: Forecast Fusion.
    Fuses multiple forecast sources (e.g. Open-Meteo + GFS) to find consensus and spread.
    """
    forecasts = evidence.get_forecasts()
    if not forecasts:
        return {"status": "NO_FORECASTS"}

    temps = [f.weather.temperature_celsius for f in forecasts if f.weather and f.weather.temperature_celsius is not None]
    rain_probs = [f.weather.rain_probability_percent for f in forecasts if f.weather and f.weather.rain_probability_percent is not None]
    
    if not temps or not rain_probs:
        return {"status": "MISSING_VARIABLES"}
        
    avg_temp = sum(temps) / len(temps)
    avg_rain_prob = sum(rain_probs) / len(rain_probs)
    
    # Calculate source disagreement (max diff)
    temp_spread = max(temps) - min(temps)
    rain_spread = max(rain_probs) - min(rain_probs)
    
    if rain_spread > 20 or temp_spread > 3.0:
        disagreement = "HIGH"
    elif rain_spread > 10 or temp_spread > 1.5:
        disagreement = "MODERATE"
    else:
        disagreement = "LOW"

    return {
        "status": "SUCCESS",
        "consensus_temperature": round(avg_temp, 1),
        "consensus_rain_probability": round(avg_rain_prob, 1),
        "temperature_spread": round(temp_spread, 1),
        "rain_probability_spread": round(rain_spread, 1),
        "source_disagreement": disagreement,
        "sources_fused": len(forecasts)
    }
