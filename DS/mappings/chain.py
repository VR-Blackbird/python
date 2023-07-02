from collections import ChainMap

d1 = dict(a=11, b=12, c=13)
d2 = dict(a=10, b=90, d=14)

chain = ChainMap(d1, d2)
print(chain['d'])
