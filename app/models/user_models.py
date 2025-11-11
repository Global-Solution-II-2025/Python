from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    timezone: Optional[str] = "America/Sao_Paulo"

class UserOut(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    timezone: str
