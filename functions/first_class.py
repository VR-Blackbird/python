def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)
# fact = factorial(3)
fact = factorial
print(list(map(factorial, range(1, 10))))
print(list(map(fact, range(1, 10))))
