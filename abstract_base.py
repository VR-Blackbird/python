from abc import ABCMeta, ABC, abstractmethod
import io
import collections.abc


a = [1, 2, 3, 4, 5]
d = {"ajs": 10, "bahs": 19}


class SomeAbstractClass(ABC):
    @abstractmethod
    def sides(self):
        pass


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self):
        print("Read method of abstract base class")

    def write(self, data):
        print(data)


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


IStream.register(io.IOBase)

f = open("helper_files/abstract.txt")
print(isinstance(f, IStream))

print(isinstance(a, collections.abc.Sequence))
print(isinstance(a, collections.abc.Iterable))
print(isinstance(a, collections.abc.Mapping))
print(isinstance(d, collections.abc.Mapping))
print(isinstance(d, collections.abc.Sized))
