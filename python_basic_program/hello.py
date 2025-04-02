import first 
num=(1,2,3,5,6,1,2,3,1,1)
sum=0
no=num.count(1)
num_str=str(no)
ind=num.index(6)
print(f'the index of given number is: {ind}')

print("control inside loop here")
for i in num:
    print(i)
    sum=sum+i
print("control out of loop here")
print(type(num))
print(sum)    
first.greeting("sonu")