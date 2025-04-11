#program to display given number is perfect square or not
#optimal approch using Binary search

def is_perfect_square(num):
    if num < 1:
        return False
    
    low = 1
    high = num
    
    while low <= high:
        mid = (low + high) // 2
        squared = mid * mid
        
        if squared == num:
            return mid 
        elif squared < num:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1 

num = int(input("Enter number: "))
result = is_perfect_square(num)

if result != -1:
    print(f"{num} is a perfect square of {result}")
else:
    print(f"{num} is not a perfect square.")
