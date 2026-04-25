#!/usr/bin/env python3

print("Enter the first number: ")
a = int(input())
print("Enter the second number: ")
b = int(input())

result = a * b

print(f"{a} x {b} = {result}")

if result > 0:
    print("This number is positive.")
elif result < 0:
    print("This number is negative.")
else:
    print("This number is positive and negative.")