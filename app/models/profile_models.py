from pydantic import BaseModel
from typing import Any, Dict

class ProfileOut(BaseModel):
    user_id: int
    computed_json: Dict[str, Any]
    recommended_career: str
