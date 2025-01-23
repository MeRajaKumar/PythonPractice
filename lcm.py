num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
x = 2
Lcm = 1
while x <= num1:
    if num1&x == 0 and num2%x == 0:
        Lcm *= x
        num1 //= x
        num2 //= x
    else:
        x += 1
print("LCM is : ",Lcm*num1*num2)