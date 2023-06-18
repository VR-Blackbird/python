from typing import Type


class Person:
    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("string expected")

        self._name = name

class SubPerson(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, name):
        print("Setting name")
        super(SubPerson, SubPerson).name.__set__(self, name)

class FigPerson(Person):
    @Person.name.getter
    def name(self):
        print("Hello getter")
        return super().name


class SetPerson(Person):
    @Person.name.setter
    def name(self, name):
        print("SETTING...........")
        super(SetPerson, SetPerson).name.__set__(self, name)

p = Person("logan")
print(p.name)

p.name = "Paul"

print(p.name)
s = SubPerson("Subname")
print(s.name)
s.name = "Loki"
print(s.name)

f = FigPerson("Swask")
print(f.name)


s = SetPerson("lakaks")
print(s.name)