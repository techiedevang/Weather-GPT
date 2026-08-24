from app.schemas.evidence import EvidenceRecord, Location, WeatherVariables
from datetime import datetime, timedelta

def fetch_weather_api_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    # MVP Mock: Represents a call to Open-Meteo or similar
    # In production, this would make an async HTTP request
    
    target_time = datetime.now() + timedelta(hours=24) # Tomorrow forecast
    
    return EvidenceRecord(
        source_id="open-meteo-v1",
        source_type="WEATHER_API",
        location=Location(name=location_name, lat=lat, lon=lon),
        target_time=target_time,
        retrieved_at=datetime.now(),
        weather=WeatherVariables(
            temperature_celsius=32.0,
            rain_probability_percent=75,
            rainfall_mm=12.5,
            wind_speed_kmh=15.0,
            condition_description="Heavy Rain Expected"
        ),
        provenance="Mocked Open-Meteo API JSON response"
    )
