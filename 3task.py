def log_fun(func):
    def inner():
        print("Start")
        func()
        print("end")

    return inner


@log_fun
def i_like():
    print("I like ...")
    

i_like()
