# perguntas, pesos, mapeamentos básicos
QUESTION_DEFINITIONS = [
    {"code": "q_like_programming", "text": "Você gosta de programar? (1-5)"},
    {"code": "q_like_data", "text": "Você gosta de trabalhar com dados? (1-5)"},
    {"code": "q_like_design", "text": "Você tem interesse em design? (1-5)"},
    {"code": "q_interest_ai", "text": "Interesse em IA? (1-5)"},
]

# mapeamento pergunta -> skill weights
WEIGHTS = {
    "q_like_programming": {"programming": 3},
    "q_like_data": {"data": 3},
    "q_like_design": {"design": 2},
    "q_interest_ai": {"ai": 4},
}
