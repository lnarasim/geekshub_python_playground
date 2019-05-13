from geekshub_pyproblems.benchmark import timer
from time import sleep


def test_benchmark():
    @timer
    def func_sleep(duration):
        sleep(2)
        return f'Slept for {duration} seconds'

    assert func_sleep(2) == 'Slept for 2 seconds'
    assert func_sleep(4) == 'Slept for 4 seconds'
