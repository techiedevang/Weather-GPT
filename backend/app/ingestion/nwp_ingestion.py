import httpx
from datetime import datetime, timezone, timedelta
from app.schemas.evidence import EvidenceRecord, Location, WeatherVariables
from app.utils.logging import logger

async def fetch_nwp_evidence(lat: float, lon: float, location_name: str) -> EvidenceRecord:
    """
    Step 04: NWP Ingestion.
    Fetches forecasting model data (GFS) via Open-Meteo's models endpoint.
    This provides a distinct data source for the Fusion engine to compare against.
    """
    url = f"https://api.open-meteo.com/v1/gfs"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation_probability,precipitation,wind_speed_10m",
        "forecast_days": 1,
        "timezone": "auto"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            
            hourly = data.get("hourly", {})
            times = hourly.get("time", [])
            
            # Find the index closest to the current time + 1 hour (representing a near-term forecast)
            # For simplicity in this MVP snippet, we just grab the first valid future index.
            # (Assuming standard structure where index 0 is midnight, etc. We just grab index 12 for noon as a mock placeholder if needed,
            # or better: we extract the current hour's index)
            
            current_hour_str = datetime.now().strftime("%Y-%m-%dT%H:00")
            target_index = 0
            for i, t in enumerate(times):
                if t >= current_hour_str:
                    target_index = i
                    break
                    
            weather_vars = WeatherVariables(
                temperature_celsius=hourly.get("temperature_2m", [])[target_index],
                rain_probability_percent=hourly.get("precipitation_probability", [])[target_index],
                rainfall_mm=hourly.get("precipitation", [])[target_index],
                wind_speed_kmh=hourly.get("wind_speed_10m", [])[target_index],
                condition_description="NWP Forecast Projection"
            )
            
            return EvidenceRecord(
                source_id="gfs-0.25deg-hourly",
                source_type="NWP",
                location=Location(name=location_name, lat=lat, lon=lon),
                target_time=datetime.now(timezone.utc) + timedelta(hours=1),
                retrieved_at=datetime.now(timezone.utc),
                weather=weather_vars,
                provenance="GFS 0.25deg Model via Open-Meteo"
            )
            
    except Exception as e:
        logger.error(f"Failed to fetch NWP data: {str(e)}")
        raise
