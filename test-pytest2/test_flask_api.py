import pytest
from flask_api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_initialization(client):
    assert app is not None
    assert app.config["TESTING"] is True


def test_add_user(client):
    response = client.post('/users', json={"id": 1, "name": "Alice"})
    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Alice"}


def test_get_user(client):
    client.post('/users', json={"id": 1, "name": "Alice"})
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json == {"id": 1, "name": "Alice"}


def test_get_user_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}


def test_add_duplicate_user(client):
    client.post('/users', json={"id": 1, "name": "Alice"})
    response = client.post('/users', json={"id": 1, "name": "Bob"})
    assert response.status_code == 400
    assert response.json == {"error": "User already exists"}
