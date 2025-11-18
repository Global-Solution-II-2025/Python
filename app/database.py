from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import oracledb
import os
import sys


load_dotenv()

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN")  # host:port/servicename

missing = [
    k for k, v in {
        "ORACLE_USER": ORACLE_USER,
        "ORACLE_PASSWORD": ORACLE_PASSWORD,
        "ORACLE_DSN": ORACLE_DSN,
    }.items() if not v
]

if missing:
    print(f"❌ ERRO: Variáveis faltando: {', '.join(missing)}")
    sys.exit(1)

DATABASE_URL = f"oracle+cx_oracle://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_DSN}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=1800,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
