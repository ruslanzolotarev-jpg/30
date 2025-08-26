from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_recipes():
    response = client.get("/recipes")
    assert response.status_code == 200
