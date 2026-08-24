from app.schemas.alerts import Alert
from app.database.database import get_supabase_client
from typing import List

# Mock in-memory storage for alerts when Supabase is not configured
_mock_alerts: List[Alert] = []

def get_recent_alerts() -> List[Alert]:
    client = get_supabase_client()
    if client:
        # Fetch from Supabase
        response = client.table("alerts").select("*").order("timestamp", desc=True).limit(10).execute()
        return [Alert(**row) for row in response.data]
    else:
        return _mock_alerts

def add_alert(alert: Alert) -> Alert:
    client = get_supabase_client()
    if client:
        response = client.table("alerts").insert(alert.model_dump(exclude={"id"})).execute()
        return Alert(**response.data[0])
    else:
        _mock_alerts.insert(0, alert)
        return alert
