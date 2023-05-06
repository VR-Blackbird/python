registry = []


def register(func):
    print("Regiter called ->", func)
    registry.append(func)

@register
def f1():
    print("f1 called")

@register
def f2():
    print("f2 called")

def f3():
    print("f3 called")


def main():
    print("Main function called")
    print(registry)
    f3()


if __name__ == "__main__":
    main()
