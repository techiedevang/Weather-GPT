import json
from app.ai.groq_client import get_groq_client
from app.schemas.ai_models import IntentExtraction

def parse_intent(query: str) -> IntentExtraction:
    client = get_groq_client()
    
    prompt = f"""
    Analyze the following user query about weather.
    Extract the following details:
    1. intent: Must be one of [current_weather, forecast, rain_query, alert_query, travel_advisory, farmer_advisory, climate_analytics]
    2. location: The location mentioned. If none, return empty string.
    3. time: The time period mentioned. If none, return 'current'.
    4. language: The language of the query (e.g., english, hindi, hinglish).
    
    Return ONLY a valid JSON object matching this schema, no other text:
    {{
        "intent": "string",
        "location": "string",
        "time": "string",
        "language": "string"
    }}
    
    Query: "{query}"
    """
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    data = json.loads(content)
    return IntentExtraction(**data)
