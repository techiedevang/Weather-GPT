import httpx
from datetime import datetime, timezone
from app.schemas.evidence import EvidenceRecord, Location, WeatherVariables
from app.utils.logging import logger

async def fetch_weather_api_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    """
    Step 03: Weather API Ingestion.
    Fetches real-time current weather data using the Open-Meteo API.
    """
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
        "timezone": "auto"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            
            current = data.get("current", {})
            
            # Open-Meteo does not provide a direct 'rain probability' in the 'current' endpoint,
            # so we map precipitation to a simplistic probability for MVP, or we could fetch hourly.
            precip = current.get("precipitation", 0.0)
            prob = 100 if precip > 0 else 0
            
            condition = "Clear"
            if precip > 0:
                condition = "Rain"
                
            weather_vars = WeatherVariables(
                temperature_celsius=current.get("temperature_2m"),
                humidity_percent=current.get("relative_humidity_2m"),
                rainfall_mm=precip,
                wind_speed_kmh=current.get("wind_speed_10m"),
                rain_probability_percent=prob,
                condition_description=condition
            )
            
            return EvidenceRecord(
                source_id="open-meteo-v1-current",
                source_type="WEATHER_API",
                location=Location(name=location_name, lat=lat, lon=lon),
                target_time=datetime.now(timezone.utc),
                retrieved_at=datetime.now(timezone.utc),
                weather=weather_vars,
                provenance="Open-Meteo API (Current Weather)"
            )
            
    except Exception as e:
        logger.error(f"Failed to fetch Weather API data: {str(e)}")
        # In a production system, this might return a custom Exception or a partial EvidenceRecord 
        # indicating failure so the Fusion engine handles missing data gracefully.
        raise
