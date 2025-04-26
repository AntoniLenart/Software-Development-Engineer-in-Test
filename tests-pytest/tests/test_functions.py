import pytest
import source.my_functions as my_functions
import time


def test_add():
    result = my_functions.add(1, 5)
    assert result == 6


def test_add_strings():
    result = my_functions.add("Hello ", "World")
    assert result == "Hello World"


def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_slow():
    time.sleep(5)  # Simulate a slow test
    result = my_functions.divide(10, 2)
    assert result == 5


@pytest.mark.skip(reason="Currently broken")
def test_skip():
    result = my_functions.add(1, 2)
    assert result == 3


@pytest.mark.xfail(reason="Expected to fail, cannot divide by 0")
def test_divide_zero_xfail():
    result = my_functions.divide(10, 0)
    assert result == 5
