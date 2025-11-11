# Career AI Backend

Estrutura básica de um backend FastAPI que armazena respostas de um chatbot e gera perfis e planos de estudo.

## Rodando local (com Docker)
1. Ajuste variáveis em `.env` (ou use `.env.example`).
2. `docker-compose up --build`
3. API disponível em: http://localhost:8000

## Rodando local sem Docker
1. `pip install -r requirements.txt`
2. Exporte variáveis de ambiente (ORACLE_*).
3. `uvicorn app.main:app --reload`

## Estrutura
Veja os diretórios `app/`, `scripts/`, `tests/`.

## Observações
- Em produção, use um Oracle Cloud / Autonomous DB ou outro RDBMS compatível.
- Troque segredos e tokens por variáveis de ambiente seguras.
