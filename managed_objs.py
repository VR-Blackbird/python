class Person:
    def __init__(self, first_name):  # Uses setter by default
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first):
        if not isinstance(first, str):
            raise TypeError("Expected a string")
        self._first_name = first

    @first_name.deleter
    # def first_name(self):
    #     raise AttributeError("Can't delete")

    def first_name(self):
        try:
            del self._first_name
        except:
            print("can't delete")
        else:
            print("deleted")


f = Person("Abay")
print(f.first_name)
# f.first_name = 12
f.first_name = "Kleesan"
print(f.first_name)
del f.first_name
