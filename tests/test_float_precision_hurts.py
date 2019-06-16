from geekshub_pyproblems.float_precision_hurts import float_precision_issue


def test_float_precision_hurts():
    value = 100.01
    number = 1000_000_000
    assert 100010000000 != float_precision_issue(value, number)
