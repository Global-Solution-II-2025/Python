from fastapi import APIRouter, HTTPException
from app.repositories.answer_repo import get_answers_by_user
from app.core.scoring import compute_user_profile
from app.repositories.profile_repo import insert_profile, get_latest_profile

router = APIRouter()

@router.post("/compute/{user_id}")
def compute_profile(user_id: int):
    answers = get_answers_by_user(user_id)
    if not answers:
        raise HTTPException(status_code=404, detail="No answers for user")
    profile = compute_user_profile(answers)
    insert_profile(user_id, profile, profile.get("recommended_career"))
    return profile

@router.get("/latest/{user_id}")
def latest_profile(user_id: int):
    profile = get_latest_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
