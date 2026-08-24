from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.ai.intent_parser import parse_intent
from app.ai.tool_router import route_tool
from app.ai.response_generator import generate_response
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/ai/query", response_model=ChatResponse)
async def ai_query(request: ChatRequest):
    try:
        # 1. Parse intent, location, time, language
        intent_extraction = parse_intent(request.query)
        
        # Override language if explicitly provided in request
        language = request.language if request.language else intent_extraction.language
        
        # 2. Route to tool to get structured data
        weather_data = route_tool(
            intent=intent_extraction.intent,
            location=intent_extraction.location,
            time=intent_extraction.time
        )
        
        # 3. Generate grounded response
        response_text = generate_response(
            query=request.query,
            language=language,
            intent_data=intent_extraction,
            weather_data=weather_data
        )
        
        return ChatResponse(
            response=response_text,
            intent=intent_extraction.intent,
            location=intent_extraction.location,
            time=intent_extraction.time,
            language=language,
            weather_data=weather_data
        )
        
    except Exception as e:
        logger.error(f"Error processing AI query: {{str(e)}}")
        raise HTTPException(status_code=500, detail=str(e))
