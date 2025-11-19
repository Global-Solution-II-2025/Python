from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base

class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)

    questions = relationship("Question", back_populates="area")
    scores = relationship("UserScore", back_populates="area")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=True)

    area = relationship("Area", back_populates="questions")


class UserScore(Base):
    __tablename__ = "user_scores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(255), nullable=False, index=True)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=False)
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    area = relationship("Area", back_populates="scores")
