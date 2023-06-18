# class Person:
#     def __init__(self, name) -> None:
#         self.name = name

#     def hobbies(self, **kwargs):
#         print(kwargs)


# p1 = Person("kevin")

# p1.hobbies(morning="run", eve="sleep", early="study")


def person(name):
    def hobbies(**kwargs):
        print(f"Name is {name} : \n\t {kwargs}")

    return hobbies


p1 = person("Aegon")
p1(morning="run", eve="sleep", early="study")
