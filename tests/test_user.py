from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    user_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/auth/signup", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login_and_get_token():
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
