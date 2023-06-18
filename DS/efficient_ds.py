from decorator.simple_decor import clock
import array


lf = [float(x) for x in range(10**7)]

af = array.array("f", list(range(10**7)))


@clock.clock
def fetch_values(sequence):
    return sequence[90000]


# print(af)
fetch_values(lf)
fetch_values(af)
