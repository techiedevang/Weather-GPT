from pydantic import BaseModel, Field
from typing import Optional

class IntentExtraction(BaseModel):
    intent: str = Field(description="The intent of the user. E.g., forecast, current_weather, rain_query, alert_query, travel_advisory, farmer_advisory")
    location: str = Field(description="The location mentioned in the query.")
    time: str = Field(description="The time period mentioned, e.g. 'tomorrow evening', 'today', etc.")
    language: str = Field(description="The language of the user's query, e.g., 'english', 'hindi', 'hinglish'.")
