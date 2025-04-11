#Write a Python code to count the number of uppercase letters in a string

str1=input("enter string:")

count=0
for i in str1:
    if i.isupper():
        count=count+1

print(count)
