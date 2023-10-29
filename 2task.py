from contextlib import contextmanager


@contextmanager
def context_devider():
    print(100*"-")
    yield
    print(100*"-")


class ContextDevider:

    def __enter__(self):
        print(100 * "+")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(100*"+")


with ContextDevider() as manager:
    print("Context 1")


with context_devider() as manager:
    print("Context 2")
