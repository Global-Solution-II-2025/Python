from fastapi.testclient import TestClient
from app.main import create_app

client = TestClient(create_app())

def test_profile_no_answers():
    # try compute profile for non-existing user (no answers)
    response = client.post("/profile/compute/999999")
    assert response.status_code in (404, 500)
