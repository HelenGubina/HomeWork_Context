import time


def timeit(func):
    def inner():
        start_time = time.time()
        func()
        print(time.time()-start_time)

    return inner


@timeit
def my_fun():
    time.sleep(1)


my_fun()
