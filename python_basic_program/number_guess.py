#Number guessing game in Python 3
import re
import random
print("Number guessing game in Python 3")
str1=input("enter range for ex:1-100:")   
list1=re.findall('\d+',str1)
num1=int(list1[0])
num2=int(list1[1])

choices1=[]
for i in range(num1,num2):
    choices1.append(i)
chances=0
num2=random.choice(choices1)   

while True:    
    num=int(input("guesss the number:"))
    if num2 ==num:
        print("congratulation !you won the game")
        break
    elif num>num2:
        print("ohhhh ! you guessed bigger number:")
    elif num<num1:
        print("ohh !you guessed smaller number:")    
    elif chances==3:
        print("game over!! no more chances")
        print("better luck next time !")
        break    
    else:
        chances=chances+1
        print("try again!!")    