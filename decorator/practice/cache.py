from clock_decor import clock
from functools import cache


@cache  # Python-3.9 and above
@clock(fmt="FIBONACCI  \n[{result}] -> {arg_str} : Time taken = {elapsed_time:0.8f}s")
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
