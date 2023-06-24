import os
from array import array
import numpy
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

floats = numpy.loadtxt("10_million.txt")
print(floats[-3])

# floats *= 0.5
# print(floats[-3])

t0 = time.perf_counter()
floats /= 0.5
time_taken = time.perf_counter() - t0

print(time_taken)
print(floats[-3])

numpy.save("floats_10M", floats)
floats2 = numpy.load("floats_10M.npy", "r+")
floats2 *= 9
print(floats2[-3])
