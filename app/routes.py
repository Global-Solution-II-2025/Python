# routes.py
from fastapi import APIRouter, HTTPException
from app.models import AnswerRequest, ChatState
from app.data import questions, careers
from typing import Dict

router = APIRouter()

# Armazenamento simples em memória para sessões (use um banco depois)
sessions: Dict[str, ChatState] = {}


@router.get("/start-chat", response_model=ChatState)
def start_chat(session_id: str):
    if session_id in sessions:
        return sessions[session_id]

    # Inicia uma nova sessão
    state = ChatState(session_id=session_id, current_question=questions[0] if questions else None)
    sessions[session_id] = state
    return state


@router.post("/submit-answer", response_model=ChatState)
def submit_answer(request: AnswerRequest):
    if request.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")

    state = sessions[request.session_id]
    if state.finished:
        raise HTTPException(status_code=400, detail="Chat já finalizado")

    # Encontra a pergunta atual
    question = next((q for q in questions if q["id"] == request.question_id), None)
    if not question or request.option_index >= len(question["options"]):
        raise HTTPException(status_code=400, detail="Pergunta ou opção inválida")

    # Atualiza pontuações
    weights = question["options"][request.option_index]["weights"]
    for category, weight in weights.items():
        state.scores[category] += weight

    # Próxima pergunta ou finaliza
    current_index = next((i for i, q in enumerate(questions) if q["id"] == request.question_id), -1)
    if current_index + 1 < len(questions):
        state.current_question = questions[current_index + 1]
    else:
        # Finaliza e sugere carreira
        state.finished = True
        state.current_question = None
        max_category = max(state.scores, key=state.scores.get)
        state.suggested_career = careers.get(max_category, "Carreira indefinida")

    return state