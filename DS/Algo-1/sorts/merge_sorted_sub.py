# Merge two sorted sub arrays

"""
i -> left subarray
j -> right subarray
i starts from start of the array
j will be the mid + 1 th element and gets incremented when a[j] is moved to an auxillary array
Same case for i

if i goes past mid, it means frst subarray is exhausted. Now assign all elements of subarray j to aux array

if j goes past len(arr), means second subarray is exhausted. Now assign all elements of subarray i to aux array




"""


def sort(arr: list) -> list:
    aux_arr = []
    mid = len(arr) // 2
    i = 0
    j = mid
    lp = 0
    while True:
        lp += 1
        if len(aux_arr) == len(arr):
            return aux_arr
        if i >= mid:
            aux_arr.extend(arr[j:])
        elif j > len(arr):
            aux_arr.extend(arr[i:mid])
        elif arr[i] <= arr[j]:
            aux_arr.append(arr[i])
            i += 1
        else:
            aux_arr.append(arr[j])
            j += 1


print(sort(["D", "E", "E", "G", "M", "R", "A", "B", "C", "E", "R", "T"]))
