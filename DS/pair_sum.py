def pair_sum(lst, target):
    seen = set()

    for num in lst:
        comp = target - num

        if comp in seen:
            print(comp, num)

        seen.add(num)





pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)