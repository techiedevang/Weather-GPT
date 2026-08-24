from app.schemas.evidence import EvidenceCollection
from app.ingestion.weather_ingestion import fetch_weather_api_evidence
from app.ingestion.nwp_ingestion import fetch_nwp_evidence
from app.ingestion.observation_ingestion import fetch_observation_evidence
from app.ingestion.alert_ingestion import fetch_alert_evidence

def gather_normalized_evidence(location_name: str, lat: float = 28.53, lon: float = 77.39) -> EvidenceCollection:
    """
    Central function to gather all raw data and normalize it into a single EvidenceCollection.
    In production, these would be fetched concurrently via asyncio.gather.
    """
    
    records = []
    
    # 1. Fetch from Weather API
    records.append(fetch_weather_api_evidence(lat, lon, location_name))
    
    # 2. Fetch from NWP/GFS
    records.append(fetch_nwp_evidence(lat, lon, location_name))
    
    # 3. Fetch current observations
    records.append(fetch_observation_evidence(lat, lon, location_name))
    
    # 4. Fetch official alerts
    records.append(fetch_alert_evidence(lat, lon, location_name))
    
    return EvidenceCollection(records=records)
