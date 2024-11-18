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


# Que - WAP to calculate the sum and average of 10 numbers.
# numbers = []
# for i in range(10):
#     number = float(input(f"Enter number {i+1}: "))
#      # number = i
#     numbers.append(number)
# total_sum = sum(numbers)
# average = total_sum / len(numbers)
# print(f"\nSum of the numbers: {total_sum}")
# print(f"Average of the numbers: {average}")




# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#      total_sum = sum(numbers[i])
# average = total_sum / len(numbers)
# print(f"\nSum of the numbers: {total_sum}")
# print(f"Average of the numbers: {average}")


# Que - WAP to calculate the simple intrest of 1000
# pri = 1000
# rate_ints = 4
# time_period = 2

# final_amount = (pri*rate_ints*time_period)/100
# print(final_amount)