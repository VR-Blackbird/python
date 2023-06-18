class Student:
    def __init__(self) -> None:
        self.foo = 10
        self._bar = 19
        self.__baz = 20

    def public_method(self):
        self._private_method()

    def _private_method(self):
        pass


b = Student()

print(b.__baz)