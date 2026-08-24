from app.ai.structured_output import AIAdvisoryResponse

def generate_ai_response(prompt: str) -> AIAdvisoryResponse:
    # MVP Mock: Simulating Groq LLM returning structured JSON.
    # In production, this uses the groq Python client with response_format={"type": "json_object"}
    
    # We pretend the LLM generated this based on the evidence
    return AIAdvisoryResponse(
        answer="Based on the current forecast, there is a high probability of rain.",
        risk_level="MODERATE",
        confidence="HIGH",
        recommended_action="Postpone outdoor activities.",
        reasons=["Forecast models agree on 75% rain probability.", "Observations validate the trend."],
        language_used="english"
    )
