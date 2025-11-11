from app.database import get_connection
import json

def insert_profile(user_id, computed_json, recommended_career):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO user_profile (user_id, computed_json, recommended_career, created_at)
            VALUES (:1, :2, :3, SYSTIMESTAMP)
        """, (user_id, json.dumps(computed_json), recommended_career))
        conn.commit()

def get_latest_profile(user_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT computed_json, recommended_career FROM user_profile
            WHERE user_id = :1
            ORDER BY created_at DESC
        """, (user_id,))
        row = cur.fetchone()
        if not row:
            return None
        return {"computed_json": row[0], "recommended_career": row[1]}
