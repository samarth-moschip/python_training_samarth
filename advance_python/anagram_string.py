from collections import Counter
str=input("enter first string:")
str1=input("enter second string:")
dict={}
dict1={}
if len(str1) !=len(str):
    print("Not anagram:")
else:
    for i in str:
        dict[i]=dict.get(i,0)+1
    for i in str1:
        dict1[i]=dict1.get(i,0)+1

    if dict==dict1:
        print("anagram")
    else:
        print("not anagram")

#by using counter
"""sd=Counter(str)
sd1=Counter(str1)
if sd==sd1:
    print("anagram")
else:
    print("not anagram")"""