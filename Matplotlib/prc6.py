# import matplotlib.pyplot as plt

# # Sample data for two different categories
# categories = ['A', 'B', 'C', 'D']
# values1 = [4, 7, 1, 8]

# # Create a bar chart
# plt.bar(categories, values1, color='blue', label='Group 1')  # First set of values

# # Add labels and title
# plt.xlabel('Categories')          # Label for the x-axis
# plt.ylabel('Values')              # Label for the y-axis
# plt.title('Sample Bar Chart')     # Title for the chart

# # Add a legend to explain the color coding
# plt.legend()

# # Display the plot
# plt.show()

import matplotlib.pyplot as plt

# Data in dictionary format
data = {'Apples': 30, 'Bananas': 20, 'Cherries': 15, 'Dates': 10, 'Elderberries': 25}

# Extract keys and values for the bar chart
labels = list(data.keys())
values = list(data.values())

# Create the bar chart
plt.figure(figsize=(6,4))
plt.bar(labels, values, color='orange', label='Fruit Quantities')

# Add labels, title, and legend
plt.xlabel('Fruits')          # Label for x-axis
plt.ylabel('Quantity')        # Label for y-axis
plt.title('Fruit Distribution') # Title of the chart
plt.legend()                  # Adding legend

# Show the plot
plt.show()
