# script de exemplo para popular perguntas (gera prints; integração de seed em DB pode ser adicionada)
default_questions = [
    {"code": "q_like_programming", "text": "Você gosta de programar? (1-5)"},
    {"code": "q_like_data", "text": "Você gosta de trabalhar com dados? (1-5)"},
    {"code": "q_like_design", "text": "Você tem interesse em design? (1-5)"},
    {"code": "q_interest_ai", "text": "Interesse em IA? (1-5)"},
]

if __name__ == "__main__":
    for q in default_questions:
        print(f"{q['code']}: {q['text']}")
