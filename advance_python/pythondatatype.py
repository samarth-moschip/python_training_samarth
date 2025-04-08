
str="append 1 2 3"
list1=str.split()
list2=[3,5,1]
if list1[0]=="append":
    for i in range(1,len(list1)):
        list2.append(list1[i])
elif list1[0]=="sort":
    list2.sort()

print(list2)
