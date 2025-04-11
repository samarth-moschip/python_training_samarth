#program to remove repeated element in given lists

num = int(input("Enter number of elements in the list: "))
list1 = []
list2=[]
for i in range(num):
    element = int(input(f"Enter number {i + 1}: "))
    list1.append(element)


for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])

print(list2)

