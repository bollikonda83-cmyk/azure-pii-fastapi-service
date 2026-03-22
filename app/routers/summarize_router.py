from fastapi import APIRouter
from app.models.summarize_models import SummarizeRequest, SummarizeResponse
from app.services.summarization_service import summarize_text

router = APIRouter(prefix="/summarize", tags=["Summarization"])

@router.post("/", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    summary = summarize_text(request.text)
    return SummarizeResponse(summary=summary)
