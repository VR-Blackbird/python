import math


class Representation:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Object with -> {self.x}, {self.y}"

    def __repr__(self) -> str:
        return f"Representation({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)
