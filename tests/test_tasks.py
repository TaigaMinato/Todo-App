from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

created_task_id = None


def test_create_task():
    global created_task_id
    response = client.post("/tasks", json={"title": "Buy milk"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == "Buy milk"
    assert data["done"] is False
    created_task_id = data["id"]


def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_read_task():
    global created_task_id
    response = client.get(f"/tasks/{created_task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task_id
    assert data["title"] == "Buy milk"


def test_update_task():
    global created_task_id
    response = client.put(f"/tasks/{created_task_id}", json={"done": True})
    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True


def test_delete_task():
    global created_task_id
    response = client.delete(f"/tasks/{created_task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Task deleted"
