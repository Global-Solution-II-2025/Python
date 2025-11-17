from app.database import engine
from sqlalchemy import text

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM dual"))
            print("✅ Conexão bem-sucedida com o banco de dados Oracle!")
            for row in result:
                print(f"Resultado do teste: {row}")
    except Exception as e:
        print("❌ Erro ao conectar ao banco de dados:")
        print(e)

if __name__ == "__main__":
    test_connection()
