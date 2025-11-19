from typing import List, Optional, Annotated
from pydantic import BaseModel, Field, validator
from pydantic.functional_validators import AfterValidator



class AreaBase(BaseModel):
    name: str
    description: Optional[str] = None


class AreaOut(AreaBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class QuestionOut(BaseModel):
    id: int
    text: str
    area_id: int | None = None

    model_config = {
        "from_attributes": True
    }

def validate_score(v: int) -> int:
    if v < 1 or v > 5:
        raise ValueError("score must be between 1 and 5")
    return v

ScoreType = Annotated[int, AfterValidator(validate_score)]


class ResponseItem(BaseModel):
    area_id: int
    score: ScoreType = Field(...)


class ResponsesPayload(BaseModel):
    user_id: str = Field(..., min_length=1)
    responses: List[ResponseItem]

    @validator("responses")
    def not_empty(cls, v):
        if not v:
            raise ValueError("responses cannot be empty")
        return v


class ResultsArea(BaseModel):
    area_id: int
    area_name: str
    total_score: int
    avg_score: float

    model_config = {
        "from_attributes": True
    }


class ResultsOut(BaseModel):
    user_id: str
    summary: List[ResultsArea]
    best_areas: List[ResultsArea]

    model_config = {
        "from_attributes": True
    }
