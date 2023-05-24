import time

DEFAULT_FORMAT = "[{elapsed_time:0.8f}s] ({arg_str})"


class clockClass:
    def __init__(self, fmt=DEFAULT_FORMAT) -> None:
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*args):
            t0 = time.perf_counter()
            result = func(*args)
            elapsed_time = time.perf_counter() - t0
            arg_str = ", ".join(repr(arg) for arg in args)
            print(self.fmt.format(**locals()))
            return result

        return clocked


@clockClass(fmt="[{result}] -> {arg_str} : Time taken = {elapsed_time:0.8f}s")
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(19))
