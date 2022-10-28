# class A:
#     def some_func(self):
#         print("Some func from class A")


# class B(A):
#     def some_func(self):
#         print("Some func from class B")

#     def inherited(self):
#         super().some_func()


# a = A()
# b = B()


# a.some_func()
# b.some_func()
# b.inherited()


# class Base:
#     def __init__(self):
#         print('Base.__init__')


# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('A.__init__')


# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('B.__init__')


# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('C.__init__')


# c = C()
class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__(self)
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__(self)
        print('B.__init__')


class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


c = C()


class Note:
    def __init__(self) -> None:
        self.anotate = 10
        self.kviv = 199

    def print_vals(self):
        print(self.anotate)
        print(self.kviv)


class Paper(Note):
    def __init__(self) -> None:
        super().__init__()
        self.mutate = 1990
        self.year = 1997

    def get_vals(self):
        super().print_vals()


p = Paper()
p.get_vals()