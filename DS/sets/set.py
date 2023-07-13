l = ["spam", "spam", "eggs", "spam", "bacon", "eggs"]
empty_set = set()  # Empty set
s = set(l)
l1 = list(set(l))

d = dict.fromkeys(l).keys()
print(list(d))


haystack = ["purr", "kiffness", "stuart", "lokie"]
needles = ["kiffness", "little", "stuart"]

print(set(needles) & set(haystack))
