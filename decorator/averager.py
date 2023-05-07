class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, number):
        self.series.append(number)
        total = sum(self.series)
        return total/len(self.series)


avg = Averager()
print(avg(20))
print(avg(21))
print(avg(22))
# using closures
