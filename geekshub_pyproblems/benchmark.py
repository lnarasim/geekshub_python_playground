"""A simple decorator to measure the time taken by a function"""
from time import perf_counter
from functools import wraps


def timer(function):
    """Timer - time your callable"""
    @wraps(function)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        end = perf_counter()
        print(f"{function.__name__} took {end - start} seconds")
        return result

    return inner
