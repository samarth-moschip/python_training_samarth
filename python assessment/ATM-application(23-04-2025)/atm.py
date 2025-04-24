from time import sleep

class Atm:
    def __init__(self):
        self.dict1={"SBI-1234":["1234","4500"],"BOB-234":["7890","4000"],"UNO-123":["8976","7000"]
        }
        
    def pin_validation_fun(customer_id,pin):

        for i in self.dict1:
            if(customer_id==i):
                temp=dict1[i]
                if temp[0]==pin:
                    print("authetication succesfull")
                    return True
        return False

    def check_balance(customer_id):

        for i in self.dict1:
            if(customer_id==i):
                temp=dict[i]
                return temp[1]
            

    def withdrawl_money(cusomer_id,money):
            
            for i in self.dict1:
                if(customer_id==i):
                temp=dict[i]
                updated_money=int(temp[1])-money
                temp[1]=updated_money

    

main=Atm()
attempt=0
while True:
    print("----------welcome to ATM application-----------")
    print("----------Insert Your card-------------")
    print("----loading------")
    sleep(1)
    
    #Menu Display to user
    print("kindly enter cutomer ID")
    customer_id= input()
    print("Kindly enter Your Pin:")
    pin=input()

    if Atm.pin_validation_fun(customer_id,pin):
        print("1:cheack_balance \n 2:withdraw money \n3:deposit money \nexit")
        choice=int(input())

        if choice ==1:
            atm.check_balance(customer_id)
        else if choice==2:
            print("enter amout of money")
            money_input=int(input())
            if money_input<=int(Atm.check_balance()):
                withdrwal_money(money_input,customer_id)   
            else:
                print("insufficent balanace")         
    else:
        print("enter try again")
        attempt=attempt+1
        atm.print_menu()
        if attempt>3:
            break
