import httpx
from datetime import datetime, timezone
from app.schemas.evidence import EvidenceRecord, Location, WeatherVariables
from app.utils.logging import logger

async def fetch_observation_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    """
    Step 05: Observation Ingestion.
    Simulates fetching ground station/AWS data.
    Since public live IMD AWS APIs are often restricted, we'll use Open-Meteo's
    'past 24h' or current endpoint as a stand-in for 'recent observation'.
    """
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,precipitation",
        "timezone": "auto"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            
            current = data.get("current", {})
            
            weather_vars = WeatherVariables(
                temperature_celsius=current.get("temperature_2m"),
                humidity_percent=current.get("relative_humidity_2m"),
                rainfall_mm=current.get("precipitation", 0.0),
                condition_description="Ground Station Observation"
            )
            
            return EvidenceRecord(
                source_id="proxy-aws-station",
                source_type="OBSERVATION",
                location=Location(name=location_name, lat=lat, lon=lon),
                target_time=datetime.now(timezone.utc),
                retrieved_at=datetime.now(timezone.utc),
                weather=weather_vars,
                provenance="Proxy Ground Station via Open-Meteo"
            )
            
    except Exception as e:
        logger.error(f"Failed to fetch Observation data: {str(e)}")
        raise
