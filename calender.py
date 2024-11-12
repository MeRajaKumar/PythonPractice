import calendar

def print_calendar(year, month):
    if month < 1 or month > 12:
        return "Invalid month. Please enter a month between 1 and 12."
    cal = calendar.month(year, month)
    return cal

year = 2023
month = 1  # Change this to a valid month
output = print_calendar(year, month)
print(output)
