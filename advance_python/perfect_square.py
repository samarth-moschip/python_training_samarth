#Write a Python code to check if a number is a perfect square

num=int(input("enter number:"))

for i in range(1,num+1):
    if i*i == num:
        break


if i*i==num:
    print("given number is perfect sqaure:")
else:
    print("given number is not perfect sqaure:")


