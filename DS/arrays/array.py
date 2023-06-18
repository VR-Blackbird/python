from array import array
import sys
import os
from decorator.simple_decor import clock


os.chdir(os.path.dirname(os.path.abspath(__file__)))

floats_arr = array("f", (i for i in range(10**7)))
floats_list = [float(x) for x in range(10**7)]


print(
    f"Memory of Array of Floats : {sys.getsizeof(floats_arr)}\nMemory of Array of Lists  : {sys.getsizeof(floats_list)}"
)

with open("array.bin", "wb") as f:
    floats_arr.tofile(f)


@clock.clock
def get_element(sequence):
    return sequence.remove(11223)


get_element(floats_list)
get_element(floats_arr)  # Arrays take less time when compared to list


@clock.clock
def read_file(file):
    floats_read = array("f")
    with open(file, "rb") as f:
        floats_read.fromfile(f, 10**7)
    print(floats_read[-1])
