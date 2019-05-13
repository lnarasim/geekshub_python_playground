"""This module benchmarks two different queue implementations - custom queue
implementation and deque. For various sizes of queue, plot the insert and
retrieval response time"""

from time import perf_counter
from geekshub_pyproblems.queue import Queue


def deque_benchmark(size):
    """Benchmarks deque returning insertion and retrieval of size items"""
    from collections import deque
    start = perf_counter()
    queue = deque()
    start = perf_counter()
    for i in range(size):
        queue.append(i)

    middle = perf_counter()

    for i in range(size):
        queue.popleft()

    end = perf_counter()

    return middle - start, end - middle


def queue_benchmark(size):
    """Benchmarks queue returning insertion and retrieval of size items"""
    queue = Queue(size)
    start = perf_counter()
    for i in range(size):
        queue.add(i)

    middle = perf_counter()

    for i in range(size):
        queue.retrieve()

    end = perf_counter()

    return middle - start, end - middle
