from functools import lru_cache
from time import perf_counter


@lru_cache(maxsize=32, typed=True)
def factorial_with_cache(n):
    if not isinstance(n, int):
        raise ValueError("Invalid input")
    if n <= 1:
        return 1
    return n * factorial_with_cache(n-1)
