from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ajuste seu usuário e senha aqui 👇
DATABASE_URL = "oracle+oracledb://rm563197:180407@oracle.fiap.com.br:1521/ORCL"

print("🔄 Inicializando conexão com o banco Oracle...")

try:
    engine = create_engine(DATABASE_URL)
    print("✅ Engine criada com sucesso!")
except Exception as e:
    print("❌ Erro ao criar engine:")
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print("✅ Sessão configurada e Base declarativa pronta!")


def get_db():
    print("📥 Criando sessão com o banco...")
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("❌ Erro durante o uso da sessão:")
        print(e)
        raise
    finally:
        db.close()
        print("📤 Sessão encerrada.")
