# Selection Sort

"""
Iterate using two pointers and exchange least element with the first pointer
"""


def sort(arr: list) -> list:
    for i in range(len(arr)):
        min_e = (arr[i], i)
        for j in range(i + 1, len(arr)):
            if arr[j] < min_e[0]:
                min_e = (arr[j], j)

        value, idx = min_e
        arr[i], arr[idx] = arr[idx], arr[i]

    return arr


# print(sort([3, 18, 6, 8]))
