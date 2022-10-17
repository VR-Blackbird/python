from sqlalchemy import func


x = 10
a = lambda y, x=x: x + y  # capture x without getting modified in next line
x = 20

print(a(10))


funcs = [lambda x, n=n: x + n for n in range(5)]

for f in funcs:
    print(f(0))
