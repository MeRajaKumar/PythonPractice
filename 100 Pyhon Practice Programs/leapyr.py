year = int(input("Enter your year: "))
print("You have entered", year, "!!")

if year > 0:
    if year % 400 == 0:
        print("A leap year!")
    elif year % 100 == 0:
        print("Not a leap year!")
    elif year % 4 == 0:
        print("A leap year!")
    else:
        print("Not a leap year!")
else:
    print("Enter a valid year!")
