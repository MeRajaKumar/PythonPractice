# #lecture no - 30
# size=input("What size pizza you want to buy(S/M/L)")
# bill=0
# if size =='s' or size=='S':
#      bill+=100
#      print("Small pizza price is 100 Rs.")
# elif size=="m" or size=="M":
#      bill+=200
#      print("Medium pizza price is 200 Rs.")
# else:
#      bill+=300
#      print("Large pizza price is 300 Rs.")

# add_pepp=input("Do you want prepp(y/n)? :")
# if add_pepp =="y" or add_pepp =="Y":
#      if size =="s" or size =="S":
#           bill+=30
#      else:
#           bill+=50

# extra_cheese = input("Do you want extra cheese(y/n)? ")
# if extra_cheese=='y' or extra_cheese=='Y':
#      bill+=20
# print(f"Your total bill is {bill}")


# #lecture no - 29
# height=int(input("What is your height : "))
# bill=0
# if height >=3:
#      print("You can ride")
#      age=int(input("What is your age? :"))
#      if age < 12:
#           bill=150
#           print("Ticket price is 150 Rs")
#      elif age <=18:
#           bill=250
#           print("Ticket price is 150 Rs")
#      else:
#           bill=500
#           print("Ticket price is 150 Rs")
#      want_photo=input("Do you want to take photo (y/n)? :")
#      if want_photo =="y" or want_photo=="Y":
#           bill=bill+50
#           print(f"Your total bill is {bill}")
# else:
#      print("Can't ride!!")
# print("Bye")


#lecture no - 28
# year1 = int(input("Enter your year to check?? : "))
# if year1 %4==0:
#      if year1 % 100 ==0:
#           if year1 % 400 ==0:
#                print("Leap year")
#           else:
#                print("Not a leap year")
#      else:
#           print("Leap Year")
# else:
#      print("Not leap year")
     

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
