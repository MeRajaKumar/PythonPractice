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