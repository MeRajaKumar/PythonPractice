# #que- write a python program to generate a simple bar graph using matplotlib the graph should be property labeled.
# import matplotlib.pyplot as plt

# data_bar = {'apple': 30, 'Banana': 45, 'Cherries': 15, 'Dates': 18}
# color_dict = {'apple': 'red', 'Banana': 'blue', 'Cherries': 'green', 'Dates': 'orange'}

# labels_bar = list(data_bar.keys())
# value_bar = list(data_bar.values())
# bars = plt.bar(labels_bar, value_bar)

# for label, bar in zip(labels_bar, bars):
#     bar.set_color(color_dict[label]) 

# for bar, value in zip(bars, value_bar):
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 2,   
#              str(value), ha='center', va='bottom', color='white', fontweight='bold')  
     
# plt.xlabel('Fruits')
# plt.ylabel('Quantity (pcs)')
# plt.title('Fruits Distribution')
# plt.show()


# data = {'C':20, 'C++':15, 'Java':30, 'Python':35}
# courses = list(data.keys())
# values = list(data.values())
# colors=['red', 'blue', 'green', 'yellow']
# def add_label(courses, values):
#      for i in range(len(courses)):
#           plt.text(i,values[i],values[i])
#           plt.bar(courses, values, color=colors)
# add_label(courses, values)
# plt.title("Students enrolled in different courses")
# plt.xlabel("Courses")
# plt.ylabel("Values")
# plt.show()

import matplotlib.pyplot as plt

data_bar = {'apple': 30, 'Banana': 45, 'Cherries': 15, 'Dates': 18}
color_dict = {'apple': 'red', 'Banana': 'blue', 'Cherries': 'green', 'Dates': 'orange'}

labels_bar = list(data_bar.keys())
value_bar = list(data_bar.values())

bars = plt.bar(labels_bar, value_bar, color=[color_dict[label] for label in labels_bar])
for bar, value in zip(bars, value_bar):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 2,   
             str(value), ha='center', va='bottom', color='white', fontweight='bold')  
             
plt.xlabel('Fruits')
plt.ylabel('Quantity (pcs)')
plt.title('Fruits Distribution')

plt.show()
