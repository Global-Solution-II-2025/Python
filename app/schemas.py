from pydantic import BaseModel
from typing import Optional, Dict

class StartSessionRequest(BaseModel):
    external_user_id: str


class StartSessionResponse(BaseModel):
    session_id: int


class AnswerRequest(BaseModel):
    session_id: int
    question_code: str
    score: int


class ResultResponse(BaseModel):
    session_id: int
    scores: Dict[str, int]
    top_categories: list
