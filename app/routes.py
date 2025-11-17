# routes.py
from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Optional

from app.models import AnswerRequest, ChatState  # Pydantic models
from app.data import questions, careers

router = APIRouter()

# armazenamento em memória para sessões (substitua por DB em produção)
sessions: Dict[str, ChatState] = {}


def _make_initial_scores() -> Dict[str, int]:
    # garante as mesmas chaves usadas nas weights do data.py
    return {"humanas": 0, "tecnologia": 0, "artes": 0}


@router.get("/start-chat", response_model=ChatState)
def start_chat(session_id: str = Query(..., description="Session id gerada pelo frontend")):
    """
    Inicia uma sessão e retorna o ChatState com a primeira pergunta em current_question.
    Obs: o router provavelmente é incluído com prefix="/api" no main.py, então a rota final será /api/start-chat
    """
    # se já existe sessão, retorna
    if session_id in sessions:
        return sessions[session_id]

    # pega a primeira pergunta (ou None)
    first_q = questions[0] if questions else None

    # cria ChatState inicial (Pydantic vai validar/parsear current_question)
    state = ChatState(
        session_id=session_id,
        current_question=first_q,
        scores=_make_initial_scores(),
        finished=False,
        suggested_career=None
    )

    sessions[session_id] = state
    return state


@router.post("/submit-answer", response_model=ChatState)
def submit_answer(request: AnswerRequest):
    """
    Recebe { session_id, question_id, option_index }, atualiza scores e retorna o novo ChatState
    """
    # valida sessão
    if request.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")

    state = sessions[request.session_id]

    if state.finished:
        raise HTTPException(status_code=400, detail="Chat já finalizado")

    # encontra a pergunta atual pelo id
    question = next((q for q in questions if q["id"] == request.question_id), None)
    if not question:
        raise HTTPException(status_code=400, detail="Pergunta inválida")

    # valida opção
    if request.option_index < 0 or request.option_index >= len(question["options"]):
        raise HTTPException(status_code=400, detail="Opção inválida")

    # pega os weights da opção escolhida
    weights = question["options"][request.option_index].get("weights", {})

    # garante chaves em scores
    for k in weights.keys():
        if k not in state.scores:
            state.scores[k] = 0

    # atualiza pontuações
    for category, weight in weights.items():
        state.scores[category] = state.scores.get(category, 0) + int(weight)

    # calcula próxima pergunta
    current_index = next((i for i, q in enumerate(questions) if q["id"] == request.question_id), -1)
    if current_index == -1:
        # não deveria acontecer porque já validamos, mas é seguro checar
        raise HTTPException(status_code=400, detail="Pergunta não encontrada na lista")

    if current_index + 1 < len(questions):
        # existe próxima pergunta -> atualiza current_question
        state.current_question = questions[current_index + 1]
    else:
        # não tem próxima -> finaliza e sugere carreira
        state.finished = True
        state.current_question = None

        # escolhe categoria com maior pontuação
        if state.scores:
            max_category = max(state.scores, key=lambda c: state.scores.get(c, 0))
            state.suggested_career = careers.get(max_category, "Carreira indefinida")
        else:
            state.suggested_career = "Carreira indefinida"

    # salva (está em memória)
    sessions[request.session_id] = state
    return state
