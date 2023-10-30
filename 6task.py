def memorise(func):
    memo_tab = {}

    def inner(a, b):
        nonlocal memo_tab
        try:
            return memo_tab[(a, b)]
        except KeyError:
            memo_tab[(a, b)] = func(a, b)
            return memo_tab[(a, b)]

    return inner


@memorise
def my_fun(a, b):
    return a*b


print(my_fun(2, 3))
print(my_fun(2, 3))
print(my_fun(3, 3))
