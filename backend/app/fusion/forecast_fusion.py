from app.schemas.evidence import EvidenceCollection

def fuse_forecasts(evidence: EvidenceCollection) -> dict:
    """
    Fuses multiple forecast sources (e.g. Open-Meteo + GFS) to find consensus.
    """
    forecasts = evidence.get_forecasts()
    if not forecasts:
        return {}

    temps = [f.weather.temperature_celsius for f in forecasts if f.weather and f.weather.temperature_celsius]
    rain_probs = [f.weather.rain_probability_percent for f in forecasts if f.weather and f.weather.rain_probability_percent]
    
    if not temps or not rain_probs:
        return {}
        
    avg_temp = sum(temps) / len(temps)
    avg_rain_prob = sum(rain_probs) / len(rain_probs)
    
    # Calculate source disagreement (max diff)
    temp_spread = max(temps) - min(temps)
    rain_spread = max(rain_probs) - min(rain_probs)
    
    disagreement = "HIGH" if rain_spread > 20 or temp_spread > 3.0 else "LOW"

    return {
        "consensus_temperature": round(avg_temp, 1),
        "consensus_rain_probability": round(avg_rain_prob, 1),
        "temperature_spread": round(temp_spread, 1),
        "rain_probability_spread": round(rain_spread, 1),
        "source_disagreement": disagreement
    }
