import pytest
from app import app as flask_app, todos


@pytest.fixture(autouse=True)
def clear_todos():
    """Clear in-memory store before and after every test."""
    todos.clear()
    yield
    todos.clear()


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client
