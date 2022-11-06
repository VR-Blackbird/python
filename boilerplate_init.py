class Structure:
    _fields = []

    def __init__(self, *args) -> None:
        if len(args) != len(self._fields):
            raise ValueError(f"Expected 3 arguments but {len(args)} were given")

        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            print(self.__dict__[name])


class Stock(Structure):
    _fields = ["name", "age", "price"]


class Point(Structure):
    _fields = ["x", "y"]


s = Point(2, 1)
f = Stock("as", 31, 80000)
# f2 = Stock("asj", 12)     ValueError: Expected 3 arguments but 2 were given
