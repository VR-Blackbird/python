import array


shirt_colors = ["Black", "White"]
shirt_size = ["S", "M", "L"]

available_shirts = [(color, size) for color in shirt_colors for size in shirt_size]


# Generator Expressions

naming = "8&*$#a1!"

ord_gens = tuple(ord(i) for i in naming)

arr = array.array("I", (ord(i) for i in naming))


# cartesian product


for shirt in (f"{col}-{size}" for col in shirt_colors for size in shirt_size):
    print(shirt)
