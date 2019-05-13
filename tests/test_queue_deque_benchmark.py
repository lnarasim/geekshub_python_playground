from geekshub_pyproblems.queue_deque_perf_test import queue_benchmark, deque_benchmark


def test_benchmark():
    assert queue_benchmark(100) > deque_benchmark(100)