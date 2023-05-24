registry = set()


def register(active=True):
    def wrapper(func):
        def decorate():
            if active:
                registry.add(func)
                result = func()
            else:
                registry.discard(func)
                result = f"Can't execute for {func.__name__}"
            return result

        return decorate

    return wrapper


@register()
def f1():
    return "Function 1"


@register(active=False)
def f2():
    return "Function 2"


print(f1())
print(f2())
print(registry)
