number = int(input("Enter your number to check if it is odd or even: "))

if number % 2 == 0:
    print(str(number) + " is an even number!")
else:
    print(str(number) + " is an odd number!")


# alternate code
number = int(input("Enter your number to check if it is odd or even: "))

if number % 2 == 0:
    print(f"{number} is an even number!")
else:
    print(f"{number} is an odd number!")
