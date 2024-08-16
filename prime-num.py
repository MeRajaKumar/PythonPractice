# for num in range(1,1001):
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(f"{num} is a prime number!")


for i in range (2,1000):
    j=i+2
    primetw=True
    if i%2 == 0 or i%3==0 or i%5==0 or i%7==0:
        primetw=False
    if j%2 == 0 or j%3==0 or j%5==0 or j%7==0:
        primetw=False
    if i==3 or i==5 or j==5:
        primetw=True
    if primetw==True:
        print(i,j)