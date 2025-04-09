# Base class
class Employee:
    def __init__(self):
        print("Hello from Employee class constructor")

    def fun1(self):
        print("Hello, I am from Employee function")


# Derived class
class samarth(Employee):
    def __init__(self):
        super().__init__() 
        print("Hello from Samarth constructor")

    def fun1(self):
        print("Hello from fun1 function")



emp = samarth() 
emp.fun1()      

