import math


class lazyproperty:
    def __init__(self) -> None:
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    @lazyproperty
    def area(self):
        print("computing area")
        return math.pi * self.radius**2

    @lazyproperty
    def perimeter(self):
        print("Computing perimeter")
        return 2 * math.pi * self.radius


c = Circle(4.0)
