from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from typing import Dict, Optional, List
from app.database import Base


# ==========================
# 🗄️ MODELOS ORM (para o Oracle)
# ==========================

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255), nullable=False)

    options = relationship("Option", back_populates="question", cascade="all, delete-orphan")


class Option(Base):
    __tablename__ = "options"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255), nullable=False)
    category = Column(String(50), nullable=False)  # RIASEC category
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)

    question = relationship("Question", back_populates="options")


class CareerProfileORM(Base):
    __tablename__ = "career_profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    riasec_code = Column(String(3), nullable=False)
    career_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)


# ==========================
# 💡 MODELOS Pydantic
# ==========================

class AnswerRequest(BaseModel):
    session_id: str
    question_id: int
    option_index: int


class CareerProfile(BaseModel):
    riasec_code: str
    career_name: str
    description: str


class ChatState(BaseModel):
    session_id: str
    current_question_id: Optional[int] = 1
    scores: Dict[str, int] = Field(default_factory=lambda: {
        "realistic": 0,
        "investigative": 0,
        "artistic": 0,
        "social": 0,
        "enterprising": 0,
        "conventional": 0
    })
    finished: bool = False
    suggested_profile: Optional[CareerProfile] = None
