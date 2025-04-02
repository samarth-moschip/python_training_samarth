from collections import Counter

str=input("enter first string:")
str1=input("enter second string:")

ctr1 = Counter(str)
ctr2 = Counter(str1)


print(ctr1) 
print(ctr2) 

if ctr1==ctr2:
    print("anagram string")
else:
    print("given string is not anagram")    