from pydantic import BaseModel
from typing import Optional

class AnswerIn(BaseModel):
    user_id: int
    question_code: str
    answer_text: str
    answer_value: Optional[str] = None

class AnswerOut(BaseModel):
    answer_id: int
    user_id: int
    question_code: str
    answer_text: str
    answer_value: Optional[str]
