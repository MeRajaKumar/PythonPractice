# WAP to get uder id, user name, and user age, form user and based on 
# the entered id print the details for particular use hint- use dictionary (search_id.isdigit() and )
# stud1 = {}
# count = int(input("Enter the number of entries you want to add: "))
# for i in range(count):
# 	key = input("Enter key: ")
# 	value = input("Enter value: ")
# 	stud1[key] = value
# print("Dictionary after adding user input: ", count)
# print(stud1)


user_dict = {
    "User_ID": 229,
    "User-Name": "Raja Kumar",
    "Age": 21
}
search_ID = input("Enter User ID to get details: ")
if int(search_ID) == user_dict["User_ID"]:
    print(f"User_ID: {user_dict['User_ID']}")
    print(f"User_Name: {user_dict['User-Name']}")
    print(f"Age: {user_dict['Age']}")
else:
    print("User ID not found.")