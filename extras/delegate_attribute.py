# class A:
#     def spam(self):
#         print("From Spam")
#
#     def foo(self):
#         print("From Foo")
#
#     def valued_sum(self, a, b):
#         print(f"Sum is {a+b}")
#
#     def __getattr__(self, name):
#         print(name, "Does not exist...Defaulting to fooo")
#         return getattr(self, "foo")
#
#
# class B:
#     def __init__(self):
#         self._a = A()
#
#     def bar(self):
#         print("From Bar")
#
#     def __getattr__(self, name):
#         return getattr(self._a, name)
#
#
# b = B()
# b.bar()
# b.spam()
# b.foo()
# b.king()
# b.queen()
# # b.valued_sm(1,2)

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)


    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith("_"):
            super().__delattr__(name, value)
        else:
            delattr(self._obj, name)


class Useful_class:
    def __init__(self, x):
        self.x = x

    def spam(self):
        print("From Spam")

    def foo(self):
        print("From Foo")

    def valued_sum(self, a, b):
        print(f"Sum is {a+b}")

u = Useful_class(2)
p = Proxy(u)
p.foo()
