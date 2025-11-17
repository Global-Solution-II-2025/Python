# app/schemas.py
from pydantic import BaseModel
from typing import Optional, List


class OptionSchema(BaseModel):
    id: int
    text: str
    category: str

    class Config:
        orm_mode = True


class QuestionSchema(BaseModel):
    id: int
    text: str
    options: List[OptionSchema]

    class Config:
        orm_mode = True


class CareerSchema(BaseModel):
    id: int
    riasec_code: str
    career_name: str
    description: str

    class Config:
        orm_mode = True
