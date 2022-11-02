class OneDigitNumericValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        obj.__dict__[self.name] = value


class Foo:
    number = OneDigitNumericValue()


ob_one = Foo()
ob_two = Foo()
ob_one.number = 3
print(ob_one.number)
print(ob_two.number)
