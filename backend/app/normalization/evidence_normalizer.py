import asyncio
from app.schemas.evidence import EvidenceCollection, EvidenceRecord
from app.ingestion.weather_ingestion import fetch_weather_api_evidence
from app.ingestion.nwp_ingestion import fetch_nwp_evidence
from app.ingestion.observation_ingestion import fetch_observation_evidence
from app.ingestion.alert_ingestion import fetch_alert_evidence
from app.utils.logging import logger

async def gather_normalized_evidence(location_name: str, lat: float, lon: float) -> EvidenceCollection:
    """
    Step 07: Normalization Layer.
    Executes all async ingestion tasks concurrently.
    Fuses heterogeneous data into the common EvidenceCollection schema.
    """
    logger.info(f"Gathering multi-source evidence for {location_name} ({lat}, {lon})")
    
    tasks = [
        fetch_weather_api_evidence(lat, lon, location_name),
        fetch_nwp_evidence(lat, lon, location_name),
        fetch_observation_evidence(lat, lon, location_name),
        fetch_alert_evidence(lat, lon, location_name)
    ]
    
    # Run all API requests concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    records = []
    for result in results:
        if isinstance(result, Exception):
            logger.error(f"Ingestion source failed: {result}")
        elif isinstance(result, EvidenceRecord):
            records.append(result)
            
    # Normalize and package
    logger.info(f"Successfully gathered {len(records)} evidence records.")
    return EvidenceCollection(records=records)
