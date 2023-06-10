import math


class Vector2d:
    typecode = "d"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self):
        return math.atan2(self.y, self.x)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __call__(self):
        return sum([self.x, self.y])

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __format__(self, format_spec=""):
        if format_spec.endswith("p"):
            coords = (abs(self), self.angle())
            format_spec = format_spec[:-1]
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        comp = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*comp)
