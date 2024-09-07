#lecture no - 28
year1 = int(input("Enter your year to check?? : "))
if year1 %4==0:
     if year1 % 100 ==0:
          if year1 % 400 ==0:
               print("Leap year")
          else:
               print("Not a leap year")
     else:
          print("Leap Year")
else:
     print("Not leap year")
     

#lecture no - 23
# age=int(input("Enter Your Age : "))
# years_left = 90-age
# days_left=years_left*365
# months_left=years_left*12
# weeks_left=years_left*52

# print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left. ")

#lecture no - 18
# a=5
# b='5'
# b=5
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)

#lecture no - 12
# firstNumber=input("Enter 1st number: ")
# secondNumber=input("Enter 1st number: ")
# sum=firstNumber+secondNumber
# print(sum) #it will add 1 to 2
# firstNumber=int(input("Enter 1st number: "))
# secondNumber=int(input("Enter 1st number: "))
# sum=firstNumber+secondNumber
# print(sum)

#lecture no - 11
# var_1=123
# var_2=10.1
# print(var_1+var_2) 
# print(type(var_1))
# print(type(var_2))
# a=1
# b=2
# var=a<b
# print(var)
# print(type(var))

#lecture no - 09
# a=input("enter value of a: ")
# b=input("enter value for b: ")
# temp=a
# a=b
# b=temp
# print("now values of a: ",a)
# print("now values of a: ",b)
