from decorator.simple_decor import clock
import array


lf = list(range(100))

af = array.array("f", list(range(100)))


@clock.clock
def fetch_values(sequence):
    return sequence[90]


# print(af)
fetch_values(lf)
fetch_values(af)
