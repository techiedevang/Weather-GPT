def generate_grounded_prompt(evidence_payload: dict, language: str) -> str:
    """
    Constructs a strict system prompt that forces the LLM to use only the provided evidence.
    """
    return f"""
    You are WeatherGPT, a highly accurate decision-support assistant.
    You MUST base your response ONLY on the following structured evidence.
    Do NOT invent or hallucinate any weather numbers, locations, or warnings.
    
    EVIDENCE DATA:
    {evidence_payload}
    
    INSTRUCTIONS:
    1. Respond in {language}.
    2. Explain the weather condition and uncertainty.
    3. State the identified impact.
    4. Provide the exact recommended action.
    5. Output your response adhering strictly to the JSON schema requested.
    """
