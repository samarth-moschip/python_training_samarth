#Calculate the factorial of a given number.

fact=1
num=int(input("enter number want to calculate factorial:"))

for i in range(1,num+1):
    fact=fact*i

print(fact)