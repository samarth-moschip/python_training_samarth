import traceback

num = 10
try:
    file1 = open("file_not_found.txt", "r")  
    rev = num // 0  
except ZeroDivisionError:
    print("Exception caught: Cannot divide by zero")
    traceback.print_exc()
except FileNotFoundError:
    print("Hello from file not found")
    traceback.print_exc()
