from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from typing import List

def get_areas(db: Session):
    return db.query(models.Area).order_by(models.Area.name).all()

def get_questions(db: Session, area_id: int = None):
    q = db.query(models.Question)
    if area_id:
        q = q.filter(models.Question.area_id == area_id)
    return q.order_by(models.Question.id).all()

def area_exists(db: Session, area_id: int):
    return db.query(models.Area).filter(models.Area.id == area_id).first() is not None

def save_user_scores(db: Session, user_id: str, responses: List[schemas.ResponseItem]):
    inserted = []
    for r in responses:
        score = models.UserScore(
            user_id=user_id,
            area_id=r.area_id,
            score=r.score
        )
        db.add(score)
        inserted.append(score)
    db.commit()
    for s in inserted:
        db.refresh(s)
    return inserted

def get_user_scores(db: Session, user_id: str):
    return db.query(models.UserScore).filter(
        models.UserScore.user_id == user_id
    ).order_by(models.UserScore.created_at.desc()).all()

def calculate_results(db: Session, user_id: str):
    res = (
        db.query(
            models.Area.id.label("area_id"),
            models.Area.name.label("area_name"),
            func.sum(models.UserScore.score).label("total_score"),
            func.avg(models.UserScore.score).label("avg_score")
        )
        .join(models.UserScore, models.UserScore.area_id == models.Area.id)
        .filter(models.UserScore.user_id == user_id)
        .group_by(models.Area.id, models.Area.name)
        .order_by(func.avg(models.UserScore.score).desc())
        .all()
    )

    summary = [
        {
            "area_id": int(r.area_id),
            "area_name": r.area_name,
            "total_score": int(r.total_score),
            "avg_score": float(round(r.avg_score, 2)),
        }
        for r in res
    ]

    best = []
    if summary:
        max_avg = max(s["avg_score"] for s in summary)
        best = [s for s in summary if s["avg_score"] == max_avg]

    return summary, best
