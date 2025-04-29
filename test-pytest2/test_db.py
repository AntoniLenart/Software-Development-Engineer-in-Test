import pytest
from db import Database


@pytest.fixture
def db():
    db = Database()
    yield Database()
    db.data.clear()


def test_initialization(db):
    assert isinstance(db, Database)


def test_add_user(db):
    db.add_user("Alice", "alice@lol.pl")
    assert db.get_user("Alice") == "alice@lol.pl"


def test_add_duplicate_user(db):
    db.add_user("Alice", "alice@lol.pl")
    with pytest.raises(ValueError, match="Username already exists"):
        db.add_user("Alice", "Alice@lol.pl")


def test_delete_user(db):
    db.add_user("bob", "bob@lol.pl")
    db.delete_user("bob")
    assert db.get_user("bob") is None


def test_delete_nonexistent_user(db):
    with pytest.raises(ValueError, match="User not found"):
        db.delete_user("nonexistent")

