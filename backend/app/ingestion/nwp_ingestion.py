from app.schemas.evidence import EvidenceRecord, Location, WeatherVariables
from datetime import datetime, timedelta

def fetch_nwp_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    # MVP Mock: Represents GFS/WRF model outputs
    # Notice this might disagree slightly with the weather API (gap implementation)
    
    target_time = datetime.now() + timedelta(hours=24)
    
    return EvidenceRecord(
        source_id="gfs-0.25deg",
        source_type="NWP",
        location=Location(name=location_name, lat=lat, lon=lon),
        target_time=target_time,
        retrieved_at=datetime.now(),
        weather=WeatherVariables(
            temperature_celsius=30.5,
            rain_probability_percent=85,
            rainfall_mm=15.0,
            wind_speed_kmh=22.0,
            condition_description="Severe Thunderstorms"
        ),
        provenance="Mocked GFS 0.25 degree grid extraction"
    )
