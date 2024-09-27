import matplotlib.pyplot as plt

# Example data in two dictionaries
dict1 = {'A': 5, 'B': 7, 'C': 3}
dict2 = {'A': 4, 'B': 2, 'C': 8}

# Create lists of keys (categories) and values (data)
keys = list(dict1.keys())
values1 = list(dict1.values())
values2 = list(dict2.values())

# Set the position of bars on x-axis
x = range(len(keys))

# Create a bar chart
plt.bar(x, values1, width=0.4, label='Dict 1', align='center')
plt.bar(x, values2, width=0.4, label='Dict 2', align='edge')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart for Two Dictionaries')

# Add ticks and legend
plt.xticks(x, keys)
plt.legend()

# Show the plot
plt.show()
