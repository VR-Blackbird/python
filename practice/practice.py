# Candy distrubution

total = 17  # Input
num_children = 3  # Input

# Initialize a list of zeros for each child
children = [0] * num_children

# Distribute candies to children
current_child = 0
candies = 1

while total > 0:
    # Distribute candies to the current child
    if candies <= total:
        children[current_child] += candies
        total -= candies
        candies += 1
    else:
        children[current_child] += total
        total = 0

    # Move to the next child in a circular manner
    current_child = (current_child + 1) % num_children

# Print the distribution of candies to children
print(children)


class A:
    x = [1,2,3]

class B(A):
    pass

b = B()
A.x[1] = 19
print(b.x)



