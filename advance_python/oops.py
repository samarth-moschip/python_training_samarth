#program to demostrate the OOP concepts in python(inheitance,polymorphism,constuctor)

import random
class employee:
    def __init__(self,emp_id,location):
        self.emp_id=emp_id
        self.location=location
        print("super class construtor  has been called")
        

class Samarth(employee):
    def __init__(self, name, age, deparment, rnd):
        self.name = name
        self.age = age
        self.department = deparment
        self.rnd=rnd
        print("child  class construtor  has been called")
        super().__init__("INT_168","pune")






#emp=employee("INT168","pune")
#print(f"employee ID is:{emp.emp_id}")
#print(f"location is:{emp.location}")
s1= Samarth("Samarth", 23, "digital", 1)
print(f"name :{s1.name}")
print(f"deparment:{s1.department}")
print(f"age :{s1.age}")



'''while num2 <=10:  # Corrected the loop condition
    choices = [1, 0]
    num = random.choice(choices)

    if num == 1:
        sam1 = Samarth("Samarth", 23, "digital", num)
        

    else:
        print("weired")
    num2+=1 '''   
    
