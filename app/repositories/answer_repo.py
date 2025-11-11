from app.database import get_connection

def insert_answer(user_id, question_code, answer_text, answer_value=None):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO user_answers (user_id, question_code, answer_text, answer_value, answered_at)
            VALUES (:1, :2, :3, :4, SYSTIMESTAMP)
        """, (user_id, question_code, answer_text, answer_value))
        conn.commit()

def get_answers_by_user(user_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT question_code, answer_value FROM user_answers WHERE user_id = :1", (user_id,))
        rows = cur.fetchall()
        return [(r[0], r[1]) for r in rows]
