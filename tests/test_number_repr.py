import pytest
from geekshub_pyproblems.number_repr import convert_from_base10


def test_convert_from_base10_valid_values():
    number = 10
    base = 2
    result = convert_from_base10(number, base)
    assert int(result, base = base) == number

    number = 5
    base = 5
    result = convert_from_base10(number, base)
    assert int(result, base=base) == number

    number = 256
    base = 16
    result = convert_from_base10(number, base)
    assert int(result, base=base) == number

    number = 256
    base = 36
    result = convert_from_base10(number, base)
    assert int(result, base=base) == number

    number = 256
    base = 16
    result = convert_from_base10(number, base)
    assert int(result, base=base) == number

    number = 123456789
    base = 16
    result = convert_from_base10(number, base)
    assert int(result, base=base) == number

    number = -123456789
    base = 16
    result = convert_from_base10(number, base)
    assert int(result, base=base) == number


def test_convert_from_base_10_invalid_values():
    number = "123"
    base = 16
    with pytest.raises(TypeError):
        convert_from_base10(number, base)

    number = 123
    base = "16"
    with pytest.raises(TypeError):
        convert_from_base10(number, base)

    number = "123"
    base = "16"
    with pytest.raises(TypeError):
        convert_from_base10(number, base)

    number = None
    base = 16
    with pytest.raises(TypeError):
        convert_from_base10(number, base)

    number = 123456
    base = 50
    with pytest.raises(ValueError):
        convert_from_base10(number, base)

    number = 123456
    base = 1
    with pytest.raises(ValueError):
        convert_from_base10(number, base)

    number = 123456
    base = -5
    with pytest.raises(ValueError):
        convert_from_base10(number, base)