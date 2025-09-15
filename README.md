# Todo App (FastAPI + SQLite)

A simple **Todo API** built with FastAPI and SQLite, designed to practice modern development workflow (GitHub Flow, CI/CD, and deployment).

---

## 🚀 Features
- CRUD API for tasks
- SQLite + SQLAlchemy for persistence
- Pydantic for request/response validation
- pytest for automated tests
- GitHub Actions for CI (linting + tests)
- Deployed on Render with Auto Deploy (CD)

---

## 📦 Requirements
- Python 3.12+
- Virtual environment (`venv`)

---

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/<your-username>/Todo-App.git
cd Todo-App
```

## Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Run the Server
```bash
uvicorn src.main:app --reload
```

### Server runs at:
- Local: http://127.0.0.1:8000
- Docs (Swagger UI): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## Run Tests
```bash
pytest
```

### Tests cover:
- Create / Read / Update / Delete task
- Error handling for invalid IDs

---

## Development Flow
We follow GitHub Flow:
1. Create feature branch
```bash
git checkout -b feature/<name>
```
2. Commit changes
```bash
git commit -m "feat: <what you did>"
```
3. Push and create Pull Request
```bash
git push origin feature/<name>
```
4. Wait for CI (lint + tests) to pass
5. Review & merge into main

---

## CI/CD
- CI: GitHub Actions runs on every PR (lint + pytest).
- CD: Render auto-deploys on every push to main.

Start command on Render:
```bash
uvicorn src.main:app --host 0.0.0.0 --port 10000
```

## Deployment
Live API:
-> https://todo-app-gv75.onrender.com/docs
