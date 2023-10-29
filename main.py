import time
from datetime import datetime
from contextlib import contextmanager


@contextmanager
def context_manager():
    start_time = datetime.now()
    yield
    print(datetime.now()  - start_time)


class ContextManager:
    def __init__(self):
        self.start_time = datetime.now()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(datetime.now()-self.start_time)


with ContextManager() as manager:
    time.sleep(2)
    sum1 = 0
    for i in range(1000):
        sum1 += 1


with context_manager() as manager:
    time.sleep(1)
    sum1 = 0
    for i in range(1000):
        sum1 += 1