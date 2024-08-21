# Aim: WAP to perform list operation-creating, accessing, slicing, modifying, adding, removing, sorting, reversing, finding length and looping through lists. 
list1=[12,45,4,8,13,56,87] #creating
print(list1[0]) #accessing
print(list1[2:4]) #slicing
list1.insert(3,56) #modifying
print(list1)
list1.append(27) #adding
print(list1)
list1.remove(13) #removing
print(list1)
list2 = [2,89,4,46,19,76]
list2.sort() #sorting
print(list2)
list2 = [2,13,4,46,13,76]
list2.reverse() #reversing
print(list2)
list2 = [2,13,4,46,13,76]
print(len(list2)) #finding length
list2 = [2,13,4,46,13,76]
for x in list2:
     print(x) 


# 2️⃣ Write a program to print twin prime less than thousand. (How to calculate twin prime in range of thousand). If two consecutive odd number are both prime then they are knows as twin primes. 
# For print prime number only!!
# for num in range(1,1001):
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(f"{num} is a prime number!")


# for i in range (2,1000):
#     j=i+2
#     primetw=True
#     if i%2 == 0 or i%3==0 or i%5==0 or i%7==0:
#         primetw=False
#     if j%2 == 0 or j%3==0 or j%5==0 or j%7==0:
#         primetw=False
#     if i==3 or i==5 or j==5:
#         primetw=True
#     if primetw==True:
#         print(i,j)