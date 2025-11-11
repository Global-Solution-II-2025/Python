from app.core.study_plan import generate_study_plan

def test_generate_plan():
    plan = generate_study_plan(1, "programming", {"monday": ["19:00-21:00"]})
    assert plan["career"] == "programming"
    assert "milestones" in plan
