from pydantic import BaseModel
from typing import Optional, Any


class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    question_id: int
    sql_result: Any
    report_link: Optional[str] = None