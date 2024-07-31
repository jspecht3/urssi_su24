from math_operations import add, subtract, multiply, divide, mean
import pytest
import numpy as np

def test_add():
    assert add(1, 5) == 6
    assert add(1, -152) == -151
    assert add(125, 12581) == add(12581, 125)


@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (1.5, 2.5, 4)]
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(2, -5) == 7
    assert subtract(2, 0) == 2


@pytest.mark.parametrize(
    "a, b, expected", [(0, 1, -1), (125, 0, 125), (3, 3, 0), (-3, 3, -6)]
)
def test_subtract_parametrized(a, b, expected):
    assert subtract(a, b) == expected

def test_multiply():
    assert multiply(2, 25) == 50
    assert multiply(2, 0) == 0
    assert multiply(152, 12612) == multiply(12612, 152)


def test_divide():
    assert divide(144, 12) == 12
    assert divide(0, 2) == 0


@pytest.mark.parametrize("numbers, expected", [
    ([10, 20, 30], 20),
    ([1.5, 2.5, 3.5], 2.5)
    ])
def test_mean(numbers, expected):
    assert mean(numbers) == expected
