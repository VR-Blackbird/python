from unicodedata import name

new_set = {chr(i) for i in range(1, 256) if "SIGN" in name(chr(i), "")}
print(new_set)

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
c = {2, 8, 7, 9}
d = {12, 13, 14}

print(a.union(b, c, d))
print(a)
print({*a, *b, *c, *d})
