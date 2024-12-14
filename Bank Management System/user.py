from person import Person
from bank import Bank
from datetime import datetime
class User(Person):
    def __init__(self, name, email, address,account_type):
        super().__init__(name, email, address)
        self.account_type=account_type
        self.balance=0
        self.txt=202400
        self.account_no=None
        self.transaction=[]
        self.loan=0
     
    def deposite(self,bank,amount):
        if amount>0:
            self.balance+=amount
            bank.bank_balance+=amount
            self.transaction.append([datetime.now(),amount,"Deposite"])
            print(f'\n\t\t\t{amount} taka successfully added.\n')
        else:
            print("\n\t\t\tAmount does not negative!!!\n")

    def withdraw(self,bank,amount):
        if amount > self.balance:
            print("\n\t\t\tWithdrawal amount exceeded!!\n")
        elif amount > bank.bank_balance:
            print("\n\t\t\tThe ABC bank is bankrupt!!!\n")
        else:
            self.balance-=amount
            bank.bank_balance-=amount
            self.transaction.append([datetime.now(),amount,"Withdraw"])
            print(f"\n\t\t\tThe withdrawl money: {amount} taka.\n")

    def check_balance(self):
        print(f"\n\t\t\tCurrent Balance:{self.balance}\n")
    
    def show_transaction(self):
        print("\n\t\t\t Date   \tTime    Amount    Type")
        for history in self.transaction:
            print(f"\t\t\t{history[0]} {history[1]} {history[2]}")

    def apply_loan(self,bank):
        bank.send_loan(self)
     
    def transfer(self,bank,user,ac_no,amount):
        other=bank.find_account(ac_no)
        if other!=None and user.balance > amount:
            user.balance-=amount
            other.balance+=amount
            print(f"\n\t\t {amount} taka transferred to Account No.:{other.account_no}\n")
            self.transaction.append([datetime.now(),amount,"Transfer"])
        elif other==None:
            print("\n\t\t Account does not exist.\n")
        else:
            print("\n\t\t User balance is not sufficient!\n")

    
    

    


    
    
