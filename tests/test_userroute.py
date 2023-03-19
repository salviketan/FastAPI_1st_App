from fastapi.testclient import TestClient
import json, os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_create_user():
    data = {"email": "testuser@client.com", "password": ""}
    response = client.post("/users/", json= data)
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@client.com"
    assert response.json()["is_active"] == True