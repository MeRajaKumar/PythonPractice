import matplotlib.pyplot as plt

# Sample dictionary
data = {
    'Apples': 30,
    'Bananas': 20,
    'Cherries': 25,
    'Dates': 15,
    'Elderberries': 10
}

# Extracting keys and values from the dictionary
categories = list(data.keys())
values = list(data.values())

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'yellow', 'purple'])
plt.title('Fruit Distribution Pie Chart')
plt.show()
