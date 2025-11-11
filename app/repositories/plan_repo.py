from app.database import get_connection
import json

def insert_plan(user_id, career_code, plan_json):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO study_plan (user_id, career_code, plan_json, created_at)
            VALUES (:1, :2, :3, SYSTIMESTAMP)
        """, (user_id, career_code, json.dumps(plan_json)))
        conn.commit()
