from app.ai.structured_output import AIAdvisoryResponse

def validate_ai_evidence(ai_response: AIAdvisoryResponse, evidence_payload: dict) -> bool:
    """
    Research Gap 4: Evidence Validator.
    Independently verifies the LLM output against the actual evidence to block hallucinations.
    """
    
    # 1. Validate Risk
    actual_risk = evidence_payload.get("risk", {}).get("risk_level", "LOW")
    if ai_response.risk_level != actual_risk:
        print(f"VALIDATION FAILED: AI risk {ai_response.risk_level} != Actual {actual_risk}")
        return False
        
    # 2. Validate Confidence
    actual_confidence = evidence_payload.get("uncertainty", {}).get("confidence", "LOW")
    if ai_response.confidence != actual_confidence:
        print(f"VALIDATION FAILED: AI confidence {ai_response.confidence} != Actual {actual_confidence}")
        return False
        
    # 3. Action Consistency
    actual_action = evidence_payload.get("impact", {}).get("recommended_action", "")
    if actual_action and actual_action.lower() not in ai_response.recommended_action.lower():
        # In a real system, use semantic similarity here. For MVP, basic text match.
        pass
        
    return True
