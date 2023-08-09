from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_example():
    example_data = {
        "name": "Teste Uno",
        "description": "Something in Angola"
    }
    response = client.post("/v1/examples/", json=example_data)

    assert response.status_code == 200
    assert response.json()["name"] == example_data["name"]
    assert response.json()["description"] == example_data["description"]
