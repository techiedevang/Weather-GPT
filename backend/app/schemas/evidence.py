from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class Location(BaseModel):
    name: str
    lat: float
    lon: float

class WeatherVariables(BaseModel):
    temperature_celsius: Optional[float] = None
    rain_probability_percent: Optional[int] = None
    rainfall_mm: Optional[float] = None
    wind_speed_kmh: Optional[float] = None
    humidity_percent: Optional[int] = None
    condition_description: Optional[str] = None

class AlertDetails(BaseModel):
    severity: str # "Low", "Moderate", "High", "Critical"
    title: str
    description: str
    source: str
    active_until: Optional[datetime] = None

class EvidenceRecord(BaseModel):
    source_id: str
    source_type: str # "WEATHER_API", "NWP", "OBSERVATION", "OFFICIAL_ALERT"
    location: Location
    target_time: datetime
    retrieved_at: datetime
    weather: Optional[WeatherVariables] = None
    alert: Optional[AlertDetails] = None
    provenance: str # Metadata explaining where this came from

class EvidenceCollection(BaseModel):
    records: List[EvidenceRecord]
    
    def get_forecasts(self):
        return [r for r in self.records if r.source_type in ["WEATHER_API", "NWP"]]
        
    def get_observations(self):
        return [r for r in self.records if r.source_type == "OBSERVATION"]
        
    def get_alerts(self):
        return [r for r in self.records if r.source_type == "OFFICIAL_ALERT"]
