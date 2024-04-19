import time


ints = range(-500, 500)


#Brute forces

def find_three_sum(arr):
    start_time = time.perf_counter()
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    count += 1
                    print(arr[i], arr[j], arr[k])
    end_time = time.perf_counter()
    print(end_time - start_time)
    return count


print(find_three_sum(ints))