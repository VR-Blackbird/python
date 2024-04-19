# Insertion Sort

"""
In each iteration i swap arr[i] with all the other elements to the left of i if they are larger

"""


def sort(arr: list) -> list:
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr


print(sort([19, 8, 16, 2, 1]))
