import os

from fastapi import APIRouter

from src.config import settings
from src.models import ErrorResponse, SummarizeRequest, SummarizeResponse
from src.service_llm import (
  LARGE_TEXT_THRESHOLD,
  summarize_large_text,
  summarize_small_text,
)

router = APIRouter()

APP_NAME = "LLM summarization Service"

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = settings.get("OPENAI_API_KEY")


@router.post("/llm/summarize",
            responses={500: {"model": ErrorResponse}},
            response_model=SummarizeResponse,
            description="Summarize data"
            )
async def summarize(
    summarize_request: SummarizeRequest,  # Accept text as form data
) -> SummarizeResponse | ErrorResponse:

    if len(summarize_request.text) > LARGE_TEXT_THRESHOLD:
        summary = summarize_large_text(summarize_request.text)
    else:
        summary = summarize_small_text(summarize_request.text)

    return SummarizeResponse(
        summary=summary
    )
