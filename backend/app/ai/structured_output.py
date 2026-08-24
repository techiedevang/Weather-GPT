from pydantic import BaseModel
from typing import List

class AIAdvisoryResponse(BaseModel):
    answer: str
    risk_level: str
    confidence: str
    recommended_action: str
    reasons: List[str]
    language_used: str
