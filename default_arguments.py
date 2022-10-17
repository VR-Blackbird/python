def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)


# Check if a user passed any 2nd argument
def check_arguments(a, b=None):
    if b is None:
        print("No value passed")  # It will pass even if a user supplied None


# Better solution

_no_value = object()


def check_args(a, b=_no_value):
    if b is _no_value:
        print("No value passed")


# _no_value = 10
check_arguments(1, None)
check_args(1)
