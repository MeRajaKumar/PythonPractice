''' 👇 Assignment
WAP to input a number and check whether it is Even or Odd.
WAP to input a number print its Square if it is odd, otherwise print its square root.
WAP to input a Year and check whether it is a Leap year.
WAP to input a number check whether it is Positive or Negative or ZERO.
WAP to input Percentage Marks of a students, and find the grade as per following criterion:
     Marks			Grade
     >=90			     A
     75-90			B
     60-75			C
     Below 60			D  '''


# 1️⃣ WAP to input a number and check whether it is Even or Odd.
# num = int(input("Enter a number to check whether it is Even or Odd : "))
# if num % 2==0:
#      print("Number is Even!")
# else:
#      print("Number is Odd!")


# 2️⃣ WAP to input a number print its Square if it is odd, otherwise print its square root.
# import math
# num = int(input("Enter a number to print its Square & Square room : "))
# if num % 2!=0:
#      square_num = num ** 2
#      print("Square of", num,"is", square_num)
# else:
#      square_root = math.sqrt(num)
#      print("Square root of",num, " is",square_root)


# 3️⃣ WAP to input a Year and check whether it is a Leap year.
# year = int(input("Enter a Year to check whether it is a Leap year : "))
# # Check if the year is a leap year
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


# 4️⃣ WAP to input a number check whether it is Positive or Negative or ZERO.
# number = float(input("Enter a number to check whether it is a positive or negative or zero : "))
# # Check if the number is positive, negative, or zero
# if number > 0:
#     print(f"{number} is a positive number.")
# elif number < 0:
#     print(f"{number} is a negative number.")
# else:
#     print("The number is zero.")

             
# 5️⃣ WAP to input Percentage Marks of a students, and find the grade as per following criterion:
     # Marks			Grade
     # >=90			A
     # 75-90			B
     # 60-75			C
     # Below 60		D  
# marks = float(input("Enter your Marks: "))
# if marks >= 90:
#      print("Your grade is A.")
# elif 75 <= marks < 90:
#      print("Your grade is B.")
# elif 60 <= marks < 75:
#      print("Your grade is C.")
# else:
#      print("Your grade is D.")
     
     
# ➡️ second method
# marks = float(input("Enter the percentage marks: "))
# # Determine the grade based on the marks
# if marks >= 90:
#     grade = 'A'
# elif 75 <= marks < 90:
#     grade = 'B'
# elif 60 <= marks < 75:
#     grade = 'C'
# else:
#     grade = 'D'
# print(f"The grade for {marks}% is {grade}.")
