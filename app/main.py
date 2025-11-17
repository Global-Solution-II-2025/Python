# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(
    title="Chatbot Vocacional API",
    version="1.0.0",
    description="API do teste vocacional com FastAPI"
)

# Origem do seu frontend local + Render (produção)
origins = [
    "http://localhost:5173",
    "https://noraia-sm77.onrender.com",   # importante para CORS no Render!
    "*",  # libera tudo caso precise depurar
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prefixo /api deixa tudo assim:
# GET  /api/start-chat
# POST /api/submit-answer
app.include_router(router, prefix="/api")


# rota raiz opcional (só pra testar no navegador)
@app.get("/")
def root():
    return {"status": "API Online", "endpoints": ["/api/start-chat", "/api/submit-answer"]}
