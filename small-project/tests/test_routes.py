import pytest
from app import create_app
from app.db import mongo


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["MONGO_URI"] = "mongodb://mongo:27017/testdb"

    with app.test_client() as client:
        with app.app_context():
            mongo.db.users.delete_many({})  # wyczyść kolekcję przed każdym testem
        yield client


def test_init_db(client):
    # Test if the database connection is established
    response = client.get('/users')
    assert response.status_code == 200


def test_get_empty_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.get_json() == []


def test_add_user(client):
    response = client.post('/users', json={'name': 'Ala'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'User added'

    get_response = client.get('/users')
    users = get_response.get_json()
    assert any(user['name'] == 'Ala' for user in users)
