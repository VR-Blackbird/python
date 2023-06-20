import numpy as np

a = np.arange(12)
print(a)
print(a[0])
print(a.shape)
a.shape = (6, 2)
print(a)
print(a[2])
print(a[2, 1])
a = a.transpose()
print(a)
