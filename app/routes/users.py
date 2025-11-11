from fastapi import APIRouter, HTTPException
from app.models.user_models import UserCreate, UserOut
from app.repositories.user_repo import create_user, get_user_by_id

router = APIRouter()

@router.post("/", response_model=UserOut)
def create(user: UserCreate):
    user_id = create_user(user.name, user.email, user.timezone)
    if not user_id:
        raise HTTPException(status_code=500, detail="Could not create user")
    data = get_user_by_id(user_id)
    return data

@router.get("/{user_id}", response_model=UserOut)
def read(user_id: int):
    data = get_user_by_id(user_id)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data
