import time

DEFAULT_FORMAT = "[{elapsed_time:0.8f}s] ({arg_str})"


def clock(fmt=DEFAULT_FORMAT):
    def decorate(func):
        def clocked(*args):
            t0 = time.perf_counter()
            result = func(*args)
            elapsed_time = time.perf_counter() - t0
            arg_str = ", ".join(repr(arg) for arg in args)
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorate


@clock(fmt="[{result}] -> {arg_str} : Time taken = {elapsed_time:0.8f}s")
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)
