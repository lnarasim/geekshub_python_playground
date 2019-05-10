import pytest
from geekshub_pyproblems.fibonacci import fib


def test_fib_valid_values():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(10) == 55

def test_fib_bigger_values():
    assert fib(30) == 832040
    assert fib(60) == 1548008755920
    assert fib(100) == 354224848179261915075


def test_fib_invalid_values():
    with pytest.raises(TypeError):
        fib("test")

    with pytest.raises(ValueError):
        fib(-1)

    with pytest.raises(TypeError):
        fib(None)

    with pytest.raises(ValueError):
        fib(-10)