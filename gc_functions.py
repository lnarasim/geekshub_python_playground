import gc


def is_object_in_gc(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return True
    return False