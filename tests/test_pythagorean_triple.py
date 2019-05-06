import pytest
from geekshub_pyproblems.pythagorean_triple import is_pythagorean_triple


def test_pythagorean_triple_valid_values():
    assert is_pythagorean_triple(3, 4, 5)
    assert is_pythagorean_triple(6, 8, 10)
    assert is_pythagorean_triple(30, 40, 50)
    assert is_pythagorean_triple(5, 4, 3)


def test_pythagorean_triple_invalid_values():
    assert not is_pythagorean_triple(3, 4, 6)
    assert not is_pythagorean_triple(9, 16, 25)
    assert not is_pythagorean_triple(9, 16, 26)
    assert not is_pythagorean_triple(30, 40, 51)
    assert not is_pythagorean_triple(90, 160, 251)
    assert not is_pythagorean_triple(90, 160, 250)
    assert not is_pythagorean_triple(160, 250, 90)


def test_pythagorean_triple_bad_values():
    with pytest.raises(ValueError):
        is_pythagorean_triple('3', 4, 6)

    with pytest.raises(ValueError):
        is_pythagorean_triple(9.0, 16, 26)

    with pytest.raises(ValueError):
        is_pythagorean_triple(30, '4', 51)

    with pytest.raises(ValueError):
        is_pythagorean_triple(90, 160, '251')

    with pytest.raises(ValueError):
        is_pythagorean_triple(90, 160, None)

    with pytest.raises(ValueError):
        is_pythagorean_triple(None, None, None)
