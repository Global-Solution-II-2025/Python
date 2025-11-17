# data.py
from typing import List, Dict

# Perguntas do teste vocacional
questions = [
    {
        "id": 1,
        "question": "Você prefere trabalhar com pessoas ou sozinho?",
        "options": [
            {"text": "Com pessoas", "weights": {"humanas": 2, "tecnologia": 0, "artes": 1}},
            {"text": "Sozinho", "weights": {"humanas": 0, "tecnologia": 2, "artes": 1}}
        ]
    },
    {
        "id": 2,
        "question": "Você gosta de resolver problemas lógicos?",
        "options": [
            {"text": "Sim", "weights": {"humanas": 0, "tecnologia": 2, "artes": 0}},
            {"text": "Não", "weights": {"humanas": 1, "tecnologia": 0, "artes": 2}}
        ]
    },
    # Adicione mais perguntas aqui (ex.: 5-10 no total)
]

# Carreiras possíveis com base nas categorias
careers = {
    "tecnologia": "Engenheiro de Software ou Cientista de Dados",
    "humanas": "Psicólogo ou Professor",
    "artes": "Designer Gráfico ou Artista"
}