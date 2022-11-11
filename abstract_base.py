from abc import ABCMeta, ABC, abstractmethod


class SomeAbstractClass(ABC):
    @abstractmethod
    def sides(self):
        pass


class Triangle(SomeAbstractClass):
    def sides(self):
        print("I have 3 sides")


class Rectangle(SomeAbstractClass):
    def sides(self):
        print("I have 4 sides")


class Pentagon(SomeAbstractClass):
    def sides(self):
        print("I have 5 sides")


t = Triangle()
t.sides()
