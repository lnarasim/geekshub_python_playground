import pytest

from geekshub_pyproblems.swap_dict_key_values import swap_dict_keys_values


def test_swap_dict_key_values():
    d = {'1': 'a', '2': 'b'}
    swap = {'a': '1', 'b': '2'}
    assert swap_dict_keys_values(d) == swap

    d = {'1': 'a', '2': 'b', '3': 'a' }
    swap = {'a': ['1', '3'], 'b': '2'}
    assert swap_dict_keys_values(d) == swap

    d = {}
    swap = {}
    assert swap_dict_keys_values(d) == swap


def test_swap_dict_key_values_invalid():
    with pytest.raises(TypeError):
        swap_dict_keys_values(None)

    with pytest.raises(TypeError):
        swap_dict_keys_values([])

    with pytest.raises(TypeError):
        swap_dict_keys_values(123)