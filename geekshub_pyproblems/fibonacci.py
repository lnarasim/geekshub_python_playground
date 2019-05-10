"""This module has fibonacci functions with custom caching using dictionary"""


def fib(number, cache=None):
    """Returns the Nth number in fibonacci series for a given N"""

    if cache is None:
        cache = dict()
    if number < 0:
        raise ValueError("Invalid value")
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number in cache:
        result = cache[number]
    else:
        result = fib(number - 1, cache) + fib(number - 2, cache)
        cache[number] = result

    return result
