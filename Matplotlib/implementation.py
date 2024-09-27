import matplotlib.pyplot as plt

data1={'Apple':30, 'Banana':40,'Mango':15}
data2={'May':45, 'June':40,'July':60}

label_bar1=list(data1.keys())
values_bar1=list(data1.values())

label_bar2=list(data2.keys())
values_bar2=list(data2.values())

plt.bar(label_bar1, values_bar1, color='red')
plt.bar(label_bar2, values_bar2, color='blue')
plt.title('Selling of fruites in this year')
plt.show()