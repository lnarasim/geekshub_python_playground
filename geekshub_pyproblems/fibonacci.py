"""This module has fibonacci functions with custom caching using dictionary"""
FIB_CACHE = dict()


def fib(number):
    """Returns the Nth number in fibonacci series for a given N"""
    if number < 0:
        raise ValueError("Invalid value")
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number in FIB_CACHE:
        result = FIB_CACHE[number]
    else:
        result = fib(number - 1) + fib(number - 2)
        FIB_CACHE[number] = result

    return result
