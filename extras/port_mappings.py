a = [1, 3, 4, 5, 6, 7,9, 11, 17]


new_str = ""

ranges = []
for i in range(0, len(a)):
    if a[i] == a[-1]:
        if ranges:
            ranges.append(a[i])
            new_str += f"{ranges[0]}-{ranges[-1]}"
        else:
            new_str += str(a[i])
        ranges = []
    elif a[i + 1] == a[i] + 1:
        ranges.append(a[i])
    else:
        ranges.append(a[i])
        new_str += f"{ranges[0]}-{ranges[-1]}," if len(ranges) > 1 else f'{ranges[0]},'
        ranges = []

print(new_str)
