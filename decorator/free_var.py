def make_averager():
    series = []
    new_valus = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(dir(avg.__code__))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)


def make_averager_optimised():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager
