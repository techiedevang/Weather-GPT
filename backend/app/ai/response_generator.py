import json
from app.ai.groq_client import get_groq_client
from typing import Dict, Any

def generate_response(query: str, language: str, intent_data: Any, weather_data: Dict[str, Any]) -> str:
    client = get_groq_client()
    
    prompt = f"""
    You are a weather intelligence assistant answering a user's query.
    User Query: "{query}"
    Requested Language: {language}
    Intent: {intent_data.intent}
    
    Here is the exact weather and advisory data retrieved for the location:
    {json.dumps(weather_data, indent=2)}
    
    CRITICAL RULES:
    1. DO NOT invent or guess any weather values (temperature, rainfall, wind, etc.).
    2. ONLY use the values provided in the weather data above.
    3. If there is "advisory" data included, make sure to relay the "risk level" and the specific "advice" clearly to the user.
    4. If the weather data is missing, say you cannot retrieve it instead of guessing.
    5. Respond in the requested language ({language}).
    
    Provide a helpful and grounded natural-language response based ONLY on the retrieved data. Keep it concise, actionable, and easy to understand.
    """
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    return response.choices[0].message.content
