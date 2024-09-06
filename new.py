StringValue=input("enter :")
len_of_string=len(StringValue)
count=0;
print(len_of_string)
for i in range(0,len_of_string):
     if StringValue[i]=="a" or StringValue[i]=="e" or StringValue[i]=="i" or StringValue[i]=="o" or StringValue[i]=="u":
          count=+1;
else:
     print("ente yor")

print(count)