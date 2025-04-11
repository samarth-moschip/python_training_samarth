#Problem Statement:
#This script display fib series of upto given number

num=int(input("enter number upto print fib series:"))
temp1=1
temp2=1
if num==1:
    print(1)
else:    
    print(temp1)
    print(temp2)
    for i in range (3,num+1):
        print(temp1+temp2)
        temp1=i-2
        temp2=i-1
