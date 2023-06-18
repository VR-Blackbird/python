names = ["David Beazley", "Brian Jones", "Raymond Hettinger", "Ned Batchelder"]

print(sorted(names, key=lambda name: name.split()[-1].lower()))


add = lambda x, y: x + y


print(add(1, 14))
