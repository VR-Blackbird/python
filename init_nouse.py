import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


serialised = {'year':2012, 'month':8, 'day':29}
d = Date.__new__(Date)
for key, value in serialised.items():
    setattr(d, key, value)


print(d.year)
d1 = Date.today()
print(d1.year)
