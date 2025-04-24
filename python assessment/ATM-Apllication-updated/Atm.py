from time import sleep
import random

class Atm:
    def __init__(self):
        self.dict1 = {
            "SBI-1234": ["1234", "4500"],
            "BOB-234": ["7890", "4000"],
            "UNO-123": ["8976", "7000"]
        }

    def pin_validation_fun(self, cu_id, pin_arg):
        for i in self.dict1:
            if cu_id == i:
                temp = self.dict1[i]
                if temp[0] == pin_arg:
                    print("authentication successful")
                    return True
        return False

    def check_balance(self, cu_id):
        for i in self.dict1:
            if cu_id == i:
                temp = self.dict1[i]
                return temp[1]
        return "0"

    def withdraw_money(self, cu_id, money):
        for i in self.dict1:
            if cu_id == i:
                current_balance = int(self.dict1[i][1])
                if money <= current_balance:
                    updated_balance = current_balance - money
                    self.dict1[i][1] = str(updated_balance)
                    return True
                else:
                    return False
        return False


atm = Atm()
attempt = 0

while True:
    print("----------welcome to ATM application-----------")
    print("---------- Insert Your card-------------------")
    print("-------------Loading--------------------------")
    sleep(1)

    # Menu Display to user
    import random

    a = [1]
    otp=random.choice(a)
    otp_user=int(input("enter your otp number send to your mobile:"))
    if otp == otp_user:
        print("kindly enter customer ID")
        customer_id = input()
        print("Kindly enter Your Pin:")
        pin_user = input()
    else:
        print("invalid otp")
        break
    if atm.pin_validation_fun(customer_id, pin_user):
        while True:
            print("1: check_balance \n2: withdraw money \n3: exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                balance = atm.check_balance(customer_id)
                print(f"Your current balance is: {balance}")

            elif choice == "2":
                print("Enter amount of money to withdraw:")
                money_input = int(input())
                if atm.withdraw_money(customer_id, money_input):
                    print(f"Withdrawal successful. New balance: {atm.check_balance(customer_id)}")
                else:
                    print("Insufficient balance or account not found")

            elif choice == "3":
                print("Thank you for using our ATM. Goodbye!")
                exit()

            else:
                print("Invalid choice. Please try again.")

    else:
        attempt += 1
        print(f"Authentication failed. Attempts left: {3 - attempt}")
        if attempt >= 3:
            print("Too many failed attempts. Card blocked.")
            break
