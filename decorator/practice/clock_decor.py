import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed_time = time.perf_counter() - t0
        arg_str = ", ".join(repr(arg) for arg in args)
        print(f"[{elapsed_time:0.8f}s] ({arg_str}) -> {result!r}")
        return result

    return clocked


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(5))
