from fastapi import APIRouter, HTTPException
from typing import Dict
from app.core.career_mapping import CAREER_CATALOG
from app.core.study_plan import generate_study_plan
from app.repositories.plan_repo import insert_plan

router = APIRouter()

@router.get("/catalog")
def catalog():
    return CAREER_CATALOG

@router.post("/study-plan/{user_id}/{career_code}")
def create_plan(user_id: int, career_code: str, availability: Dict = None):
    if career_code not in CAREER_CATALOG:
        raise HTTPException(status_code=404, detail="Career not found")
    availability = availability or {}
    plan = generate_study_plan(user_id, career_code, availability)
    insert_plan(user_id, career_code, plan)
    return plan
