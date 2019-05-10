"""Has some code to demonstrate GC functions"""
import gc


def is_object_in_gc(object_id):
    """Given the ID of the object, this function returns whether the object is
available in Python's memory if the object is tracked"""
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return True
    return False
