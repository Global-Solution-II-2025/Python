from app.core.constants import WEIGHTS

def compute_user_profile(answers):
    """
    answers: list of tuples (question_code, answer_value)
    returns dict with normalized scores and recommended career key
    """
    scores = {}
    for code, value in answers:
        try:
            val = float(value)
        except Exception:
            val = 1.0
        mapping = WEIGHTS.get(code, {})
        for skill, weight in mapping.items():
            scores[skill] = scores.get(skill, 0.0) + weight * val

    total = sum(scores.values()) or 1.0
    normalized = {k: v/total for k, v in scores.items()}
    # pick top skill as recommendation key (this is simplistic)
    top = sorted(normalized.items(), key=lambda x: x[1], reverse=True)
    recommended = top[0][0] if top else None

    return {
        "scores": normalized,
        "recommended_career": recommended
    }
