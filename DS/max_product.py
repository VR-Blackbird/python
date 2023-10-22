def max_product(nums):
    max1 = 0
    max2 = 0

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
            
        elif num > max2:
            max2 = num
    print(max1 * max2)


max_product([1, 10, 2, 4, 3, 9, 5])
