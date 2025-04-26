from source.shapes import Rectangle
import pytest


def test_rectangle_area(rectangle):
    """Test the area of the rectangle."""
    assert rectangle.area() == 20


def test_rectangle_perimeter(rectangle):
    """Test the perimeter of the rectangle."""
    assert rectangle.perimeter() == 18


def test_rectangle_equality(rectangle, rectangle_equal):
    """Test the equality of two rectangles."""
    assert rectangle == rectangle_equal


def test_not_same_area(rectangle, rectangle_equal):
    """Test the inequality of two rectangles with different areas."""
    assert rectangle != Rectangle(4, 6)
