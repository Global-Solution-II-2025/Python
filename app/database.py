from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Carrega variáveis de ambiente
ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN")

# Verifica se as variáveis existem
missing = [k for k, v in {
    "ORACLE_USER": ORACLE_USER,
    "ORACLE_PASSWORD": ORACLE_PASSWORD,
    "ORACLE_DSN": ORACLE_DSN,
}.items() if not v]

if missing:
    print(f"❌ ERRO: Variáveis de ambiente faltando: {', '.join(missing)}")
    sys.exit(1)

# Oracle DSN recomendado: "host:port/servicename"
DATABASE_URL = f"oracle+cx_oracle://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_DSN}"

# Cria engine
engine = create_engine(
    DATABASE_URL,
    encoding="utf-8",
    echo=False,     # coloque True para debug SQL
    pool_pre_ping=True,  # evita conexões quebradas
    pool_recycle=1800    # evita timeout no Oracle
)

# Session maker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base declarativa para models
Base = declarative_base()
