"""A simple factorial that uses LRU Cache from functools"""

from functools import lru_cache


@lru_cache(maxsize=32, typed=True)
def factorial_with_cache(number):
    """Uses LRU Cache to optimize runtime by storing 'some' items in cache
and kicking out some items"""
    if not isinstance(number, int):
        raise ValueError("Invalid input")
    if number <= 1:
        return 1
    return number * factorial_with_cache(number - 1)
