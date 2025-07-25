# Swap two numbers without using a third variable

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
