import os
import httpx
import json
from app.ai.structured_output import AIAdvisoryResponse
from app.utils.logging import logger

async def generate_ai_response(prompt: str) -> AIAdvisoryResponse:
    """
    Step 14: Structured AI.
    Calls Groq API and forces it to return JSON matching AIAdvisoryResponse.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        logger.warning("GROQ_API_KEY not found. Returning fallback mock response.")
        return AIAdvisoryResponse(
            answer="[Fallback] Based on the current forecast, there is a probability of rain.",
            risk_level="MODERATE",
            confidence="HIGH",
            recommended_action="Exercise caution based on weather.",
            reasons=["Fallback mode active without API key."],
            language_used="english"
        )
        
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # We use response_format={"type": "json_object"} to force structured output
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": prompt + "\n\nYou must respond ONLY with a valid JSON object with keys: answer, risk_level, confidence, recommended_action, reasons (array), language_used."
            }
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.1
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload, timeout=15.0)
            response.raise_for_status()
            data = response.json()
            
            content_str = data["choices"][0]["message"]["content"]
            result = json.loads(content_str)
            
            return AIAdvisoryResponse(
                answer=result.get("answer", "No answer provided."),
                risk_level=result.get("risk_level", "UNKNOWN"),
                confidence=result.get("confidence", "UNKNOWN"),
                recommended_action=result.get("recommended_action", "None"),
                reasons=result.get("reasons", []),
                language_used=result.get("language_used", "english")
            )
    except Exception as e:
        logger.error(f"Failed to generate AI response: {e}")
        raise

