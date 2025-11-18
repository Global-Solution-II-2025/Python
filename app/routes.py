from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud, schemas, models

router = APIRouter(prefix="/vocational", tags=["Vocational Test"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/start", response_model=schemas.StartSessionResponse)
def start_test(request: schemas.StartSessionRequest, db: Session = Depends(get_db)):
    user = crud.get_or_create_user(db, request.external_user_id)
    session = crud.create_session(db, user.id)
    return schemas.StartSessionResponse(session_id=session.id)


@router.post("/answer")
def answer_question(request: schemas.AnswerRequest, db: Session = Depends(get_db)):
    question = crud.get_question_by_code(db, request.question_code)
    if not question:
        raise HTTPException(404, "Question not found")

    crud.save_answer(db, request.session_id, question, request.score)
    return {"status": "ok"}


@router.get("/result/{session_id}", response_model=schemas.ResultResponse)
def get_result(session_id: int, db: Session = Depends(get_db)):
    answers = crud.get_answers_by_session(db, session_id)

    if not answers:
        raise HTTPException(404, "No answers found for this session")

    scores = {}
    for answer in answers:
        scores[answer.question.code] = scores.get(answer.question.code, 0) + answer.score

    top = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    
    return schemas.ResultResponse(
        session_id=session_id,
        scores=scores,
        top_categories=[t[0] for t in top]
    )
