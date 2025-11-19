from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas
from .database import get_db

router = APIRouter()

@router.get("/areas", response_model=List[schemas.AreaOut])
def list_areas(db: Session = Depends(get_db)):
    try:
        return crud.get_areas(db)
    except:
        raise HTTPException(500, "Internal server error")

@router.get("/questions", response_model=List[schemas.QuestionOut])
def list_questions(area_id: int = None, db: Session = Depends(get_db)):
    try:
        return crud.get_questions(db, area_id)
    except:
        raise HTTPException(500, "Internal server error")

@router.post("/responses", status_code=status.HTTP_201_CREATED)
def post_responses(payload: schemas.ResponsesPayload, db: Session = Depends(get_db)):
    try:
        for r in payload.responses:
            if not crud.area_exists(db, r.area_id):
                raise HTTPException(404, f"area_id {r.area_id} not found")

        inserted = crud.save_user_scores(db, payload.user_id, payload.responses)
        return {"message": "saved", "inserted": len(inserted)}

    except HTTPException:
        raise
    except:
        raise HTTPException(500, "Internal server error")

@router.get("/results/{user_id}", response_model=schemas.ResultsOut)
def get_results(user_id: str, db: Session = Depends(get_db)):
    try:
        summary, best = crud.calculate_results(db, user_id)
        return {"user_id": user_id, "summary": summary, "best_areas": best}
    except:
        raise HTTPException(500, "Internal server error")

@router.get("/users/{user_id}/history")
def history(user_id: str, db: Session = Depends(get_db)):
    try:
        rows = crud.get_user_scores(db, user_id)
        return [
            {
                "id": r.id,
                "area_id": r.area_id,
                "score": r.score,
                "created_at": r.created_at.isoformat(),
            }
            for r in rows
        ]
    except:
        raise HTTPException(500, "Internal server error")
