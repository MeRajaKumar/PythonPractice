# 1️⃣ Write a Python program to print "Hello, World!".
# print("Hello, World")

# 2️⃣ Write a Python program to add two numbers.
# num1 = 25
# num2 = 45
# tot = num1 + num2
# # print(tot)
# print("Addition of two number is",num1+num2)

# 3️⃣ Write a Python program to calculate the area of a rectangle given its length and width.
# len = float(input("Enter length :"))
# wid = float(input("Enter width :"))
# print("Area of Triangle is :",len*wid)

# 4️⃣ Write a Python program to swap two variables.
# a = 10
# b = 15
# # Print original values
# print("Before swapping:")
# print("a =", a)
# print("b =", b)
# a = a + b  # a now becomes 15 (5 + 10)
# b = a - b  # b now becomes 5 (15 - 10)
# a = a - b  # a now becomes 10 (15 - 5)
# # Print swapped values
# print("After swapping:")
# print("a =", a)
# print("b =", b)
# # Swap the values using a temporary variable
# # temp = a
# # a = b
# # b = temp
# # Swap the values using tuple unpacking
# # a, b = b, a
# # Swap the values without using a temporary variable

# 5️⃣ Write a Python program to find the maximum of three numbers.
# num1=int(input("Enter 1st number :"))
# num2=int(input("Enter 2nd number :"))
# num3=int(input("Enter 3rd number :"))
# print("1st number is :",num1)
# print("2nd number is :",num2)
# print("3rd number is :",num3)
# if num1 > num2 and num1 > num3:
#      print("The maximum number is : ",num1)
# elif num2 > num1 and num2 > num3:
#      print("The maximum number is : ",num2)
# else:
#      print("The maximum number is: ",num3)
# 2nd method : Find the maximum number using conditional statements
# if num1 >= num2 and num1 >= num3:
#     max_num = a
# elif num2 >= num1 and num2 >= num3:
#     max_num = b
# else:
#     max_num = c
# print("The maximum number is:", max_num)
# # 3rd method : Find the maximum number using the max() function
# max_num = max(num1, num2, num3)
# print("The maximum number is:", max_num)

# 6️⃣ Write a Python program to check if a number is even or odd.
# num = int(input("Enter number to check :"))
# if num%2==0:
#      print(num,"is even number!")
# else:
#      print(num,"is odd number!")

# 7️⃣ Write a Python program to find the factorial of a number using a loop.
# num = int(input("Enter number to factorial :"))
# factorial = 1
# # Use a for loop to calculate the factorial
# for i in range(1, num + 1):
#     factorial *= i  # Multiply factorial by the current number
# # Print the factorial
# print("The factorial of", num, "is:", factorial)

# 8️⃣ Write a Python program to find the sum of all numbers in a list.
# list = [12,45,56,5,6]
# tot= sum(list)
# print("list is :",list)
# print("Total of :",tot)

# # 9️⃣ Write a Python program to find the length of a string.
# str="Aayush Gupta"
# len=len(str)
# print("String is :",str)
# print("length of string is :",len)

# 1️⃣0️⃣ Write a Python program to reverse a string.
# str="Aayush Gupta"
# # Initialize an empty string for the reversed string
# reversed_string = ""
# # Use a for loop to reverse the string
# for char in str:
#     reversed_string = char + reversed_string
# # Print the reversed string
# print("Reversed string is:", reversed_string)
# # Reverse the string using slicing
# # reversed_string = str[::-1]
# # # Print the reversed string
# # print("Reversed string is:", reversed_string)

# 1️⃣1️⃣ Write a Python program to check if a year is a leap year.
# year = int(input("Enter a Year to check whether it is a Leap year : "))
# Check if the year is a leap year
# if (year % 4 == 0):
#     if (year % 100 == 0):
#         if (year % 400 == 0):
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# 1️⃣2️⃣ Write a Python program to check if a number is positive, negative, or zero.
# num = int(input("Enter your number to check : "))
# if num > 0:
#      print(num," is positive value!")
# elif num < 0:
#      print(num," is negative value!")
# else:
#      print(num," is equal to zero!")
    
    
# 1️⃣3️⃣ Write a Python program to find the largest among three numbers.
# num1 = int(input("Enter your number to check : "))
# num2 = int(input("Enter your number to check : "))
# num3 = int(input("Enter your number to check : "))
# if num1 > num2 and num1 > num3:
#      print(num1,"Is greatest number!")
# elif num2 > num1 and num2 > num3:
#      print(num2,"Is greatest number!")
# else:
#      print(num3,"Is greatest number!")

# 1️⃣4️⃣ Write a Python program to determine if a person is eligible to vote based on their age.
# age = int(input("Enter your age to check?? :"))
# if age < 18:
#      print("You are not eligible for voting!!")
# else:
#      print("You are eligible for voting!!") 

# 1️⃣5️⃣ Write a Python program to check if a character is a vowel or consonant.
# char = str(input("Enter your char to check :"))
# if char == "a" or char == "e" or char=="i" or char=="o" or char=="u":
#      print(char,"is vowel!!")
# else:
#      print(char,"is constant!!")

# 1️⃣6️⃣ Write a Python program to check if a string is a palindrome.
char = str(input("Enter string to check palindrome :"))

