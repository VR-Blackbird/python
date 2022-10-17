from unicodedata import numeric


def numbers() -> tuple:
    return 1, 2, 3


print(numbers())

a, b, c = numbers()

print(a, b, c)
