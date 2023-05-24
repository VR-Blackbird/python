# Class Averager to store history of a variable


class Averager:
    def __init__(self) -> None:
        self.series = []

    def __call__(self, value) -> int:
        self.series.append(value)
        return sum(self.series) / len(self.series)


avg = Averager()
print(avg(12))
print(avg(11))
print(avg(15))


def averager_func():
    count = 0
    total = 0

    def averager(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count

    return averager


print("------------------------------\n")
avg_func = averager_func()
print(avg_func(10))
print(avg_func(19))
print(avg_func(12))
