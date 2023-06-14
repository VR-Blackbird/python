a = (12, 13, 11, (12, 16))  # Immutable and hashable
b = (12, 13, 11, [12, 16])  # Mutable and Non hashable


b[3][1] = 90


# Find if a sequence is immutable


def check_immutability(seq):
    try:
        hash(seq)
    except TypeError:
        return False
    return True


print(check_immutability(a))
print(check_immutability(b))
