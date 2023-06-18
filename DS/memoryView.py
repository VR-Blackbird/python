from array import array


octets = array("B", range(10))
signed = array("h", [-2, -1, 0, 1, 2])

new_mem = memoryview(octets)
new_signed = memoryview(signed)
print(new_signed, id(new_signed))
print(new_mem, id(new_mem))

m1 = new_mem.cast("B", [2, 5])
m1[1, 1] = 100

print(new_mem.tolist())

sign1 = new_signed.cast("B")
print(sign1.tolist())
sign1[5] = 4
print(new_signed.tolist())
