#program to implement binary search on given list

def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] > key:
            high = mid - 1
        elif lst[mid] < key:
            low = mid + 1
        else:
            return mid  
    
    return -1  

list1 = []

num = int(input("Enter number of elements you want to add to the list: "))
for i in range(num):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)

list1.sort()  # Sorting the list before performing binary search

key = int(input("Enter the key to search in the given list: "))
result = binary_search(list1, key)

if result != -1:
    print(f"Key found at index {result}")
else:
    print("Key not found in the list")
