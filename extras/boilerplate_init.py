import math
import pdb


class Structure:
    _fields = []

    def __init__(self, *args) -> None:
        if len(args) > len(self._fields):
            raise ValueError(f"Expected 3 arguments but {len(args)} were given")

        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            print(self.__dict__[name])


class Structure2(Structure):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args)
        if kwargs:
            for name in self._fields[len(args) :]:
                try:
                    setattr(self, name, kwargs.pop(name))
                except KeyError:
                    pdb.set_trace()
                    raise KeyError(f" Key - {','.join(kwargs.keys())} - is unexpected")
                else:
                    print(self.__dict__[name])
            if kwargs:
                raise ValueError(f"Unexpected keyword argument {','.join(kwargs)}")


class Stock(Structure2):
    _fields = ["name", "age", "price"]


class Point(Structure2):
    _fields = ["x", "y"]


class Circle(Structure2):
    _fields = ["radius"]

    def area(self):
        return math.pi * self.radius**2


s = Point(x=2, y=1)
f = Stock("as", age=31, price=80000)
# f2 = Stock("asj", 12)     ValueError: Expected 3 arguments but 2 were given
c1 = Circle(radius=1)
print(c1.area())
