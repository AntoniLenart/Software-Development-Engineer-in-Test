import pytest
from source.shapes import Circle, Rectangle


@pytest.fixture
def rectangle():
    """Fixture to create a Rectangle object."""
    return Rectangle(4, 5)


@pytest.fixture
def rectangle_equal():
    """Fixture to create a Rectangle object for equality test."""
    return Rectangle(4, 5)


@pytest.fixture
def square():
    """Fixture to create a Square object."""
    return Rectangle(4, 4)
