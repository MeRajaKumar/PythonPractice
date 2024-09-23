#Wih the help of class
class employee:
    emp_name = input("Enter emp name: ")
    emp_id = int(input("Enter emp ID: "))
    emp_branch = input("Enter emp branch: ")

obj = employee()
search_value = int(input("Enter emp ID to get information: "))
def info():
     if employee.emp_id == search_value:
        print("The information of emp:")
        print(f"Name: {obj.emp_name}")
        print(f"ID: {obj.emp_id}")
        print(f"Branch: {obj.emp_branch}")
     else:
        print("Id not found!")
info()



#Wih the help of dictonary
# user_dict = {
#     "User_ID": 229,
#     "User-Name": "Raja Kumar",
#     "Age": 21
# }
# search_ID = input("Enter User ID to get details: ")
# if int(search_ID) == user_dict["User_ID"]:
#     print(f"User_ID: {user_dict['User_ID']}")
#     print(f"User_Name: {user_dict['User-Name']}")
#     print(f"Age: {user_dict['Age']}")
# else:
#     print("User ID not found.")



class Student:
    # Constructor to initialize student details
    def __init__(self, rollno, name, student_class):
        self.rollno = rollno
        self.name = name
        self.student_class = student_class

    # Method to display student details
    def display_details(self):
        print(f"Roll Number: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Class: {self.student_class}")

# Taking user input for student details
rollno = input("Enter Roll Number: ")
name = input("Enter Name: ")
student_class = input("Enter Class: ")

# Creating an instance of the Student class
student = Student(rollno, name, student_class)

# Displaying the details
print("\nStudent Details:")
student.display_details()
