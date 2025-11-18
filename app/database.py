from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import sys

# Carrega variáveis do .env
load_dotenv()

# Variáveis obrigatórias
ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN")  # Ex: oracle.fiap.com.br:1521/ORCL

# Verifica variáveis faltando
missing = [
    k for k, v in {
        "ORACLE_USER": ORACLE_USER,
        "ORACLE_PASSWORD": ORACLE_PASSWORD,
        "ORACLE_DSN": ORACLE_DSN,
    }.items() if not v
]

if missing:
    print(f"❌ ERRO: Variáveis de ambiente faltando: {', '.join(missing)}")
    sys.exit(1)

# DSN usando driver oracledb (modo THIN)
DATABASE_URL = (
    f"oracle+oracledb://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_DSN}?mode=thin"
)

# Cria engine
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=1800
)

# Session maker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base de modelos
Base = declarative_base()
