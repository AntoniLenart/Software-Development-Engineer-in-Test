import pytest
from source.shapes import Square


@pytest.mark.parametrize("side_length, expected_area", [(2, 4), (3, 9), (4, 16), (5, 25)])
def test_multiple_square_areas(side_length, expected_area):
    square = Square(side_length)
    assert square.area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(2, 8), (3, 12), (4, 16), (5, 20)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    square = Square(side_length)
    assert square.perimeter() == expected_perimeter
