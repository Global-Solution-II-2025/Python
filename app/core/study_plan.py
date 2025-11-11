import json
from datetime import datetime, timedelta

def generate_study_plan(user_id: int, career_code: str, availability: dict):
    """
    availability: dict e.g. {"monday": ["19:00-21:00"], "saturday": ["10:00-13:00"]}
    This function returns a simple plan JSON.
    """
    # Simple template with milestones
    now = datetime.utcnow()
    milestones = [
        {"title": "Fundamentos", "duration_weeks": 4},
        {"title": "Cursos técnicos", "duration_weeks": 8},
        {"title": "Projetos práticos", "duration_weeks": 8},
        {"title": "Preparação para entrevistas", "duration_weeks": 4},
    ]
    plan = {
        "user_id": user_id,
        "career": career_code,
        "created_at": now.isoformat(),
        "availability": availability,
        "milestones": milestones
    }
    return plan
