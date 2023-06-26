dial_codes = [
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United States"),
]

code_dict = {
    code: country.upper() for code, country in sorted(dial_codes, key=lambda k: k[1])
}

# Unpacking


def dump(**kwargs):
    return kwargs


print(dump(**{"x": 1}, y=2, **{"z": 3}))

# Merge mappings
d1 = {"x": 10, "y": 1, "z": 12}
d2 = {"x": 11, "y": 15}
d3 = {"z": 90}

d4 = d1 | d2 | d3
print(d4)
