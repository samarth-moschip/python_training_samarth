#program to demostrate a no of vowels in particular line

ftr=open("test.txt",'r'or 'w')

list2=ftr.readlines()[0].split()
print(list2)
for i in list2:
    for j in i:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            count+=1 

print(count)

