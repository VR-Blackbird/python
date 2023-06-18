from dis import dis
from functools import partial
import math


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)
s1(21, 3, 4)

s2 = partial(spam, c=12)
s2(1, 2, d=3)

s3 = partial(spam, d=10)
s3(21, 3, 4)


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dist = math.hypot(x2 - x1, y2 - y1)
    print(dist)
    return dist


pt = (4, 3)
origin = (0, 0)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# points.sort(key=lambda a: distance(a, origin))

print(points)
