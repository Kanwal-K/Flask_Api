from app import app
import json

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD!" in response.data

def test_add():
    client = app.test_client()
    response = client.get("/add?a=7&b=6")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["result"] == 13

def test_add_invalid():
    client = app.test_client()
    response = client.get("/add?a=invalid&b=6")
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data
