def apply_asynci(func, args, *, caback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    caback(result)


def print_result(result):
    print("Got:", result)


def add(x, y):
    return x + y


apply_asynci(add, (1,2), caback=print_result)