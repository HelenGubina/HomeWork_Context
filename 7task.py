import time


def rate_limit(max_calls=2, per=1):
    def decorator(func):
        def inner():
            start_time = time.time()
            for i in range(max_calls):
                if time.time() - start_time < per:
                    func()

        return inner

    return decorator


@rate_limit(3, 5)
def my_fun():
    time.sleep(1)
    print("Decorator")


my_fun()
