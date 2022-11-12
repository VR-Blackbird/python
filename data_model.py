import pdb


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise ("Type Error.....")
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise TypeError("Negative values are not accepted")
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise ValueError("Expecting max size")

        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError(f"Value must not exceed {self.size}")

        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class SizedString(MaxSized):
    pass


class Usage:
    name = SizedString("name", size=19)
    price = UnsignedFloat()

    def __init__(self, name, price):
        self.name = name
        self.price = price


usage = Usage("Cringe", 12.45)
usage2 = Usage("Starve", -12.45)
print(usage.name)
