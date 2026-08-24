from app.ai.structured_output import AIAdvisoryResponse
from app.utils.logging import logger

def validate_ai_evidence(ai_response: AIAdvisoryResponse, evidence_payload: dict) -> bool:
    """
    Step 15: Evidence Validator.
    Independently verifies the LLM output against the actual evidence to block hallucinations.
    """
    
    # 1. Validate Risk
    actual_risk = evidence_payload.get("risk", {}).get("risk_level", "LOW")
    if ai_response.risk_level.upper() != actual_risk.upper():
        logger.warning(f"VALIDATION FAILED: AI Risk '{ai_response.risk_level}' != Actual Risk '{actual_risk}'")
        return False
        
    # 2. Validate Confidence
    actual_confidence = evidence_payload.get("uncertainty", {}).get("confidence", "LOW")
    if ai_response.confidence.upper() != actual_confidence.upper():
        logger.warning(f"VALIDATION FAILED: AI Confidence '{ai_response.confidence}' != Actual Confidence '{actual_confidence}'")
        return False
        
    logger.info("Evidence Validation Passed: LLM output aligns with mathematical backend.")
    return True
