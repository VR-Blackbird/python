class BoundedNumber:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if self.min_val > value or value > self.max_val:
            msg = "{} takes values between {} and {}".format(
                self.name,
                self.min_val,
                self.max_val,
            )
            raise ValueError(msg)
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name]


class Person:
    age = BoundedNumber(1, 120)
    weight = BoundedNumber(1, 250)
    height = BoundedNumber(1, 230)

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def give_age_number(self):
        return self.age


p1 = Person("John", age=30, weight=100, height=120)
print(p1.age)
print(p1.give_age_number())
