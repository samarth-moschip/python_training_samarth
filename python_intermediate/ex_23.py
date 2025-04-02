num = int(input("Enter number of elements in the list: "))
list1 = []

for i in range(num):
    element = int(input(f"Enter number {i + 1}: "))
    list1.append(element)

for i in range(len(list1)):
    if list1[i] < 0:
        break

print(f"The value of i is: {i+1}")

if (i+1)==len(list1):
    print("First case pass")
else:
    print("First case failed")


count=0
for j in range(num):
    temp=list1[j]
    rev=0
    while list1[j]>0 and count<=0:
        rem=list1[j]%10
        rev=rev*10+rem
        list1[j]=list1[j]//10
    if temp==rev:
        count=count+1    


if(count>0 and (i+1)==len(list1)):
    print("all case pass:")
else:
    print("case failed")    