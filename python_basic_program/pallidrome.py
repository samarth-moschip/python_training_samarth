#program to cheack given string is pallidrome or not
def is_pallidrome(str_para):
    str_rev=str_para[::-1]
    if(str_para==str_rev):
        print("given string is pallidrome")
    else:
        print("given string is not pallidrome")
t=5
for i in range(1,6):
    str=input("enter string:")
    is_pallidrome(str)