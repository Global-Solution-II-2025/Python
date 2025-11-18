from sqlalchemy.orm import Session
from . import models

def get_or_create_user(db: Session, external_user_id: str):
    user = db.query(models.User).filter(models.User.external_user_id == external_user_id).first()
    if user:
        return user
    user = models.User(external_user_id=external_user_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_session(db: Session, user_id: int):
    session = models.Session(user_id=user_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def save_answer(db: Session, session_id: int, question: models.Question, score: int):
    answer = models.Answer(session_id=session_id, question_id=question.id, score=score)
    db.add(answer)
    db.commit()
    return answer


def get_question_by_code(db: Session, code: str):
    return db.query(models.Question).filter(models.Question.code == code).first()


def get_answers_by_session(db: Session, session_id: int):
    return db.query(models.Answer).filter(models.Answer.session_id == session_id).all()
