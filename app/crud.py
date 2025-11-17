from sqlalchemy.orm import Session
from app.models import Question, Option, CareerProfileORM

# 🔹 Buscar todas as perguntas
def get_questions(db: Session):
    return db.query(Question).all()

# 🔹 Buscar uma pergunta específica
def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()

# 🔹 Buscar todos os perfis de carreira
def get_career_profiles(db: Session):
    return db.query(CareerProfileORM).all()

# 🔹 Inserir pergunta + opções
def create_question(db: Session, text: str, options: list[dict]):
    q = Question(text=text)
    for opt in options:
        q.options.append(Option(text=opt["text"], category=opt["category"]))
    db.add(q)
    db.commit()
    db.refresh(q)
    return q
