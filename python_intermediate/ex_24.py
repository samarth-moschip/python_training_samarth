list1 = []
size = int(input("Enter the size of the list: "))

for _ in range(size):
    temp = int(input("Enter a number: "))
    list1.append(temp)

pairs = []
integer = int(input("Enter the integer: "))

# Iterating over list elements
for i in range(size):
    for j in range(size):
        if list1[j] != 0 and list1[i] // list1[j] == integer:
            pairs.append((list1[i],list1[j]))

print("Resulting pair:",pairs)
