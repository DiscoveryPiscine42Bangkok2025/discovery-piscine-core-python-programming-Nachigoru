def add_one(x):
    x += 1
    print("Inside function", x)

n = 5
print("Before", n)

add_one(n)

print("After:", n)