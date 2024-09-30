#que- write a python program to generate pie-chart using matplotlib the graph should be properly labeled.
#que- write a python program to plot the function y = x2 using the matplotlib libraries.
import matplotlib.pyplot as plt

# Data for the pie chart
data_pie = {'MCA': 30, 'BTECH': 45, 'BSC': 15, 'BCA': 10}
labels_pie = list(data_pie.keys())
values_pie = list(data_pie.values())

plt.figure(figsize=(6,6))  
plt.pie(values_pie, labels=labels_pie, autopct='%1.1f%%', startangle=90, colors=['red', 'yellow', 'green', 'orange'])

plt.title('Courses in CU')
plt.legend(labels_pie, title="Courses", loc="upper left")

plt.axis('equal')
plt.show()
