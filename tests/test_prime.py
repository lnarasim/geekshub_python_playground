import pytest
from geekshub_pyproblems.prime import is_prime, next_prime


def test_is_prime_negative_numbers():
    assert not is_prime(-1)
    assert not is_prime(-100)
    assert not is_prime(-1000)


def test_is_prime_non_prime_positive_numbers():
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(10*12)
    assert not is_prime(11*13)
    assert not is_prime(111*119)


def test_is_prime_prime_numbers():
    assert is_prime(2)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(131)


def test_is_prime_invalid_inputs():
    assert not is_prime('100')
    assert not is_prime(1.23)
    assert not is_prime('10000')
    assert not is_prime('test')
    assert not is_prime(None)
    assert not is_prime([])
    assert not is_prime({})
    assert not is_prime(set())


def test_get_next_prime():
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(-1) == 2
    assert next_prime(0) == 2
    assert next_prime(-100) == 2
    assert next_prime(100) == 101
    assert next_prime(1000) == 1009


def test_get_invalid_input():
    with pytest.raises(ValueError):
        next_prime('123')

    with pytest.raises(ValueError):
        next_prime('121233')

    with pytest.raises(ValueError):
        next_prime(1.21)

    with pytest.raises(ValueError):
        next_prime("-inf")
