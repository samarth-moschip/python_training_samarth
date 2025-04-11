#to demonstrate hashing in python

list1=[1,2,1,1,2,3,1,2,3,4,5,5,6,6,7,8]

dict1={ }

for i in list1:
    dict1[i]=dict1.get(i,0)+1
count=0
for i in dict1:
    if dict1[i]==2:
       count+=1 
print(count)       
