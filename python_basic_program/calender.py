# Problem Statement:
# This script generates a calendar for a given month.
# The user provides the total number of days in the month (valid inputs: 28 to 31)
# and specifies the starting day of the week (e.g., Monday).
# The script then prints a formatted calendar based on the inputs.

def print_calendar(start_day, num_days):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    try:
        start_index = days_of_week.index(start_day.capitalize())
    except ValueError:
        print("Invalid day name. Please use full day names (e.g., 'Monday').")
        return
    
    print("\n" + " ".join([day[:3] for day in days_of_week]))
    print("-" * 28)
    
    current_day = 1
    day_of_week = start_index
    
    print("    " * start_index, end="")
    
    while current_day <= num_days:
        print(f"{current_day:2}  ", end="")
        current_day += 1
        day_of_week += 1
        
        if day_of_week == 7:
            print()
            day_of_week = 0
    
    print("\n")

day = int(input("Enter number of days in the month (28-31): "))
if day > 31 or day < 28:
    print("Invalid number of days entered. Please enter a value between 28 and 31.")
    quit()
else:
    start_day = input("Enter the first day of the month (e.g., 'Monday'): ")
    print_calendar(start_day, day)

