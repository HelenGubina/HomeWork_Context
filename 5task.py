def retry(num):
    def decorator(func):
        def inner():
            for i in range(num):
                try:
                    func()
                    break
                except Exception:
                    print("There is a mistake")

        return inner

    return decorator


@retry(2)
def my_fun():
    print("Decorator")


my_fun()
