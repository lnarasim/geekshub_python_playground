from geekshub_pyproblems.gc_functions import is_object_in_gc


class A:
    pass


def test_is_object_in_gc():
    a = A()
    a_id = id(a)
    assert is_object_in_gc(a_id)

    a = None
    assert not is_object_in_gc(a_id)