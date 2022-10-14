from collections import Iterable

a = [[1, 2, 3], 12, [3, 5]]


def flatten(data):
    for i in data:
        if isinstance(i, Iterable):
            yield from flatten(i)
        else:
            yield i


print(list(flatten(a)))
