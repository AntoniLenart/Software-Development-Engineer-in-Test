import pytest
import source.shapes as shapes
from math import pi


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up the test method: {method}")
        self.circle = shapes.Circle(5)

    def teardown_method(self, method):
        print(f"Tearing down the test method: {method}")
        del self.circle

    def test_circle_area(self):
        assert self.circle.area() == pi * 5 ** 2

    def test_circle_perimeter(self):
        assert self.circle.perimeter() == 2 * pi * 5

    def test_not_same_area(self, rectangle):
        assert self.circle.area() != rectangle.area()
