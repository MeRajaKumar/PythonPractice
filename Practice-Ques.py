# 👉 Python program that uses a function to find the sum and average of multiple values entered by the user. 
# The program will also use a loop to keep prompting the user for more values until they decide to stop?
def calculate_sum_and_average():
    # Ask the user how many numbers they want to enter
    count = int(input("How many numbers do you want to enter? "))
    # Initialize the sum variable
    total_sum = 0
    # Use a for loop to get all the values from the user
    for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        total_sum += num
    # Calculate the average
    if count > 0:
        average = total_sum / count
    else:
        average = 0  
    return total_sum, average
# Call the function and print the results
total, avg = calculate_sum_and_average()
print(f"Sum of the values: {total}")
print(f"Average of the values: {avg}")
