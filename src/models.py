
from pydantic import BaseModel, constr


class ErrorResponse(BaseModel):
    detail: str

class SummarizeResponse(BaseModel):
    summary: str

class SummarizeRequest(BaseModel):
    text: constr(min_length=100)