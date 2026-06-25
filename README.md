# Flask Todo App

A simple REST API built with Python Flask for managing todos (in-memory store).

## Endpoints

| Method | Endpoint        | Description      |
|--------|-----------------|------------------|
| GET    | /health         | Health check     |
| GET    | /todos          | List all todos   |
| POST   | /todos          | Create a todo    |
| GET    | /todos/<id>     | Get a todo       |
| PUT    | /todos/<id>     | Update a todo    |
| DELETE | /todos/<id>     | Delete a todo    |

## Run Locally

```bash
pip install -r requirements-dev.txt
python app.py
```

App runs on http://localhost:5000

## Lint

```bash
flake8 .
```

## Test

```bash
pytest tests/ -v --cov=app
```
