# Swap Two Numbers Without Using Third Variable

a = 5
b = 10

# print(f"Before Swapping: a =  {a}, b = {b}")
print("Before Swapping: a =",a,"and b = ",b)
# Swapping without third variable
a = a + b;  # a becomes 15 (5 + 10)
b = a - b;  # b becomes 5 (15 - 10)
a = a - b;  # a becomes 10 (15 - 5)
print(f"After Swapping: a = {a}, b = {b}")