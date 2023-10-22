def findPairs(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        comp = target - num

        if comp in seen:
            print((seen[comp], i))
        seen[num] = i


lst = [1, 2, 3, 3, 4, 3, 5, 6]

findPairs(lst, 6)
