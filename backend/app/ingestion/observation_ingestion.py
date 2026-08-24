from app.schemas.evidence import EvidenceRecord, Location, WeatherVariables
from datetime import datetime

def fetch_observation_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    # MVP Mock: Represents live ground station / AWS data
    # Used to validate if the forecast is trending correctly
    
    return EvidenceRecord(
        source_id="imd-aws-station-142",
        source_type="OBSERVATION",
        location=Location(name=location_name, lat=lat, lon=lon),
        target_time=datetime.now(), # Current time observation
        retrieved_at=datetime.now(),
        weather=WeatherVariables(
            temperature_celsius=31.8,
            humidity_percent=88,
            rainfall_mm=2.5, # Already started raining
            wind_speed_kmh=12.0
        ),
        provenance="Mocked IMD AWS Ground Station Data"
    )
