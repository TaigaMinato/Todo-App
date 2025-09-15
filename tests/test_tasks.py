from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks?title=Buy milk")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Buy milk"
    assert data["done"] is False


def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_read_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Buy milk"


def test_update_task():
    response = client.put("/tasks/1?done=true")
    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True


def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task deleted"
