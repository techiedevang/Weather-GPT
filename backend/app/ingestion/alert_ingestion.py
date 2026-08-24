from app.schemas.evidence import EvidenceRecord, Location, AlertDetails
from datetime import datetime, timedelta

def fetch_alert_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    # MVP Mock: Represents Official IMD / NDMA warnings
    
    return EvidenceRecord(
        source_id="imd-warning-system",
        source_type="OFFICIAL_ALERT",
        location=Location(name=location_name, lat=lat, lon=lon),
        target_time=datetime.now() + timedelta(hours=24),
        retrieved_at=datetime.now(),
        alert=AlertDetails(
            severity="High",
            title="Orange Alert: Heavy Rainfall",
            description="Isolated extremely heavy rainfall expected in the region.",
            source="IMD",
            active_until=datetime.now() + timedelta(days=2)
        ),
        provenance="Mocked IMD District Warning Bulletin"
    )
