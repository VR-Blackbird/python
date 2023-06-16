l = list(range(10))
l[2:5] = [10, 20]
del l[5:7]
l[3::2] = [11, 13]

xo_game = [["_"] * 3 for i in range(3)]
xo_game[1][2] = "X"
xo_game[0][1] = "O"
print("Game starts -->\n")
for i in xo_game:
    print(*i)
print("\n")

# Augumented assignments

l = [1, 2, 3]
t = (1, 2, [30, 40])
t[2] += [50, 60]
