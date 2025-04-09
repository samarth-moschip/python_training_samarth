#print calender using python:

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
    
    # Print the calendar
    while current_day <= num_days:
        print(f"{current_day:2}  ", end="")
        
        # Move to next day
        current_day += 1
        day_of_week += 1
        
        if day_of_week == 7:
            print()
            day_of_week = 0
    
    print("\n")

day=int(input("enter number of days in month:"))
if day>31 or  day<28:
	print("invalid no of days you have enter")
	quit()
else:	
	start_day=input("enter first day of month:")
	print_calendar(start_day, day)

