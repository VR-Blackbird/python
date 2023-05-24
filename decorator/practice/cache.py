from clock_decor import clock
from functools import cache


@cache  # Python-3.9 and above
@clock
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
