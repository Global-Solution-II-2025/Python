from app.database import get_connection

def create_user(name, email, timezone="America/Sao_Paulo"):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (name, email, timezone, created_at)
            VALUES (:1, :2, :3, SYSTIMESTAMP)
            RETURNING user_id INTO :4
        """, (name, email, timezone, None))
        # Oracle's RETURNING with python-oracledb needs special handling; fallback: select
        conn.commit()
        # try to find the user_id
        cur.execute("SELECT user_id FROM users WHERE email = :1", (email,))
        row = cur.fetchone()
        return row[0] if row else None

def get_user_by_id(user_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT user_id, name, email, timezone FROM users WHERE user_id = :1", (user_id,))
        row = cur.fetchone()
        if not row:
            return None
        return {"user_id": row[0], "name": row[1], "email": row[2], "timezone": row[3]}
