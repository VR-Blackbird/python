import time



class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Year : {self.year}, Month : {self.month}, Day {self.day}"

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


d = Date(2012, 10, 21)
d1 = Date.today()
print(d.year)
print(d1)
