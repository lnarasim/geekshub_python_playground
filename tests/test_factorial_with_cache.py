import pytest
from factorial_with_cache import factorial_with_cache


def test_factorial_with_cache():
    result = factorial_with_cache(8)
    assert result == 40320

    result = factorial_with_cache(10)
    assert result == 3628800

    result = factorial_with_cache(11)
    assert result == 3628800 * 11

    result = factorial_with_cache(12)
    assert result == factorial_with_cache(10) * 11 * 12

    result = factorial_with_cache(15)
    assert result == factorial_with_cache(10) * 11 * 12 * 13 * 14 * 15

    result = factorial_with_cache(20)
    assert result == factorial_with_cache(15) * 16 * 17 * 18 * 19 * 20

    result = factorial_with_cache(-1)
    assert result == 1

    result = factorial_with_cache(0)
    assert result == 1

    result = factorial_with_cache(-200)
    assert result == 1

    with pytest.raises(ValueError):
        factorial_with_cache("str")

    with pytest.raises(TypeError):
        factorial_with_cache([])

    with pytest.raises(TypeError):
        factorial_with_cache({})

    with pytest.raises(ValueError):
        factorial_with_cache(35.0)

    with pytest.raises(ValueError):
        factorial_with_cache(20.0)
