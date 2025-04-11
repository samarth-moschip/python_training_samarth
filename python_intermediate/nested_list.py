#program to create nested list

list1 = []

num = int(input("Enter the number of lists you want to insert into a single list: "))

for i in range(num):
    num_element = int(input(f"Enter the number of elements you want to add in list {i + 1}: "))
    sublist = []
    for j in range(num_element):
        element = int(input(f"Enter element {j + 1} for list {i + 1}: "))
        sublist.append(element)
    list1.append(sublist)

print("The resulting list of lists is:", list1)
