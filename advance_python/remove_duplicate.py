# Write a Python code to find unique element in list

num = int(input("enter no of element in list:"))
list1=[]
temp=0
for i in range(0,num):
    no=int(input(f"enter element no {i+1}:"))
    list1.append(no)

for i in range(0,num):
    temp=temp^list1[i]  

print(temp)    
