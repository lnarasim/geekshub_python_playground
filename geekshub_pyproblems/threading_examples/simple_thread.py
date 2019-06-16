import threading
from time import sleep


def simple_thread():
    print("something")


def simple_thread_with_an_arg(a_param):
    print(f"param passed {a_param}")


def simple_thread_with_many_args(a, b, c):
    print(f"params passed {a}, {b}, {c}")


def sleeping_thread(duration):
    print(f'sleeping for {duration}secs')
    print(threading.current_thread().isDaemon())
    sleep(duration)
    print('waking up and exiting')


def enumerate_threads():
    print("printing threads")
    for thread in threading.enumerate():
        print(thread.getName())


def simple_thread_with_positional_args(a, *args):
    print(a)
    print(args)

def simple_thread_with_keyword_args(*, key1, key2, **kwargs):
    print(key1)
    print(key2)
    print(kwargs)


print("main")
thread = threading.Thread(target=simple_thread)
thread.start()

thread = threading.Thread(target=simple_thread_with_an_arg, args=(1,))
thread.start()

thread = threading.Thread(target=simple_thread_with_many_args, args=(1, 2, 3))
thread.start()

thread = threading.Thread(target=sleeping_thread, args=(1,))
thread.start()

thread.join()

thread = threading.Thread(target=sleeping_thread, args=(1,), daemon=True)
thread.start()

thread = threading.Thread(target=enumerate_threads, daemon=True)
thread.start()

thread.join()

thread = threading.Thread(target=simple_thread_with_positional_args, args=(1, 2, 3))
thread.start()

thread.join()
thread = threading.Thread(target=simple_thread_with_keyword_args, kwargs={'key1': 1, 'key2': 2, 'key3': 5})
thread.start()

print('end of main')



