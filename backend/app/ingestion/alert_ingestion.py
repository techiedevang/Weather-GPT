import httpx
import uuid
from datetime import datetime, timezone, timedelta
from app.schemas.evidence import EvidenceRecord, Location, AlertDetails
from app.utils.logging import logger

async def fetch_alert_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    """
    Step 06: Alert Ingestion.
    Simulates fetching official warnings (e.g. NDMA/IMD).
    For MVP, we fetch from a public severe weather API (e.g. US NWS or similar) 
    or just conditionally mock a warning based on weather severity if an API isn't available.
    Here we'll conditionally mock a warning so the demo always works reliably.
    """
    # For a real integration, you would hit an API like:
    # url = f"https://api.weather.gov/alerts/active?point={lat},{lon}"
    
    # Conditional Mock for reliable demoing based on time or random chance
    # Let's say if lat > 20 (North India), generate a moderate alert to demonstrate capability
    has_alert = lat > 20.0
    
    alert = None
    if has_alert:
        alert = AlertDetails(
            severity="High",
            title="Orange Alert: Heavy Rainfall",
            description="Isolated extremely heavy rainfall expected in the region.",
            source="IMD-Proxy",
            active_until=datetime.now(timezone.utc) + timedelta(days=1)
        )
        
    return EvidenceRecord(
        source_id=f"alert-{uuid.uuid4().hex[:8]}",
        source_type="OFFICIAL_ALERT",
        location=Location(name=location_name, lat=lat, lon=lon),
        target_time=datetime.now(timezone.utc),
        retrieved_at=datetime.now(timezone.utc),
        alert=alert,
        provenance="Proxy Official Warning Service"
    )
