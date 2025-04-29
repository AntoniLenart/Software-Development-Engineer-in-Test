# https://www.youtube.com/watch?v=EgpLj86ZHFQ&ab_channel=TechWithTim

import pytest
from main import UserManager


@pytest.fixture
def user_manager():
    return UserManager()


def test_initialization(user_manager):
    assert isinstance(user_manager, UserManager)


def test_add_user(user_manager):
    user_manager.add_user("Test123", "test@lol.pl")
    assert user_manager.get_user("Test123") == "test@lol.pl"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("test", "test@lol.pl")
    with pytest.raises(ValueError, match="Username already exists"):
        user_manager.add_user("test", "test@lol.pl")
