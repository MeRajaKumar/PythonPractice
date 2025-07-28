# question: Write a Python program to find the factorial of a number using a loop.
# Get input from the user
# Get input from user
num = int(input("Enter the number: "))

# Check for valid input
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"{num}! = 1")
else:
    factorial = 1
    steps = ""
    
    for i in range(1, num + 1):
        factorial *= i
        steps += str(i)
        if i < num:
            steps += "*"
    
    # Print steps and result
    print(f"{steps} = {factorial}")


# method 2 : Minimal Factorial with Step
# num = int(input("Enter the number: "))
# factorial = 1
# steps = []

# for i in range(1, num + 1):
#     factorial *= i
#     steps.append(str(i))

# print("*".join(steps), "=", factorial)