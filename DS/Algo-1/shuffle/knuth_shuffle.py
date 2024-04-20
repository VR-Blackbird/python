# Knuth Shuffle

"""
1 --> Iterate through the list (i)
2 ---> get a uniform random number index (r) between 0 and i
3 ---> swap arr[r]<-->arr[i]

"""
import random

inp_list = list(range(1, 10))


def shuffle(arr: list) -> list:
    for i in range(1, len(arr)):
        r = random.randint(0, i)
        arr[r], arr[i] = arr[i], arr[r]

    return arr


print(shuffle(inp_list))
