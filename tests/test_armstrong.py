import pytest
from geekshub_pyproblems import armstrong


def test_armstrong():
    assert armstrong.armstrong(0)
    assert armstrong.armstrong(1)
    assert armstrong.armstrong(153)
    assert armstrong.armstrong(370)
    assert armstrong.armstrong(371)
    assert armstrong.armstrong(407)


def test_armstrong():
    assert not armstrong.armstrong(2)
    assert not armstrong.armstrong(200)
    assert not armstrong.armstrong(400)
    assert not armstrong.armstrong(2000)


def test_armstrong_invalid_values():
    with pytest.raises(TypeError):
        armstrong.armstrong("123")

    with pytest.raises(TypeError):
        armstrong.armstrong(123.1)

    with pytest.raises(TypeError):
        armstrong.armstrong(None)

    with pytest.raises(TypeError):
        armstrong.armstrong([153])