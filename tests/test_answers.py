from fastapi.testclient import TestClient
from app.main import create_app

client = TestClient(create_app())

def test_save_answer_missing():
    # test that endpoint rejects malformed payload
    response = client.post("/responses", json={})
    assert response.status_code == 422  # pydantic validation error
