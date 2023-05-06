# Function that takes a function as an argument and returns a Function
def reverse(fruit):
    return fruit[::-1]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key= len))
print(sorted(fruits))
print(sorted(fruits, key= reverse))
print(sorted(fruits, key= lambda x : x[::-1]))
