def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

result = divide(10, 0)
print("Result:", result)
