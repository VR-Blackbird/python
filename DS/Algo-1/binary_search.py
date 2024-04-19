import time

a = [1, 17, 12, 8, 18, 0, 19, 13, 11, 16, 15, 34, 22, 90, 55, 20, 21, 23, 25, 28, 27]

def normal_search(arr, search):
    start_time = time.perf_counter()
    ele = search in arr
    stop_time = time.perf_counter()

    print(stop_time - start_time)
    return ele

def binary_search_algo(arr, search):

    # stop_time = time.perf_counter()
    start = 0
    stop = len(arr)
    count = 0
    start_time = time.perf_counter()
    while (start <= stop):
        print(count)
        
        mid = (start + stop) // 2
        if mid == start or mid == stop:
            stop_time = time.perf_counter()
            print(stop_time - start_time)
            return False
        if arr[mid] == search:
            stop_time = time.perf_counter()
            print(stop_time - start_time)
            return True
        if search < arr[mid]:
            stop = mid
        elif search > arr[mid]:
            start = mid
        count += 1
        # print(start, mid, stop)
    stop_time = time.perf_counter()
    print(stop_time - start_time)
    return False

a.sort()


print(normal_search(a, 200))
print(binary_search_algo(a, 200))