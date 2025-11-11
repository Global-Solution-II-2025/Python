from fastapi import APIRouter, HTTPException
from app.models.answer_models import AnswerIn
from app.repositories.answer_repo import insert_answer

router = APIRouter()

@router.post("/", status_code=201)
def save_answer(payload: AnswerIn):
    try:
        insert_answer(payload.user_id, payload.question_code, payload.answer_text, payload.answer_value)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
