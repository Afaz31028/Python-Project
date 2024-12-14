from admin import Admin
from user import User
from bank import Bank

bank=Bank("Boro looker bank",'Dhaka')
print("-------Welcome to ABC Bank Ltd-------")
def main_interface():
    while True:
        print("******Main Interface******")
        print("1.  Admin")
        print("2.  User")
        print("3.  Exit")
        op=(input("Press an option:"))
        if op=='1':
            Admin_interface()
        elif op=='2':
            user_Interface()
        elif op=='3':
            break
        else:
            print("\n\tInvalid Input, Try again!\n")
            main_interface()
def user_Interface():
    print("\t1.  Registar")
    print("\t2.  Login")
    print("\t3.  Main Interface")
    n=(input("\tEnter one option:"))
    if n=='1':
        name=input("\t\tEnter Your Name:")
        email=input("\t\tEnter Your Email:")
        address=input("\t\tEnter Your Address:")
        A_type=input("\t\tAccount Type:")
        user=User(name,email,address,A_type)
        bank.add_account(user)
        user_Interface()
    elif n=='2':
        ac_no=int(input("\t\tEnter Account No.:"))
        user=bank.find_account(ac_no)
        if(user!=None):
            while True:
                print("\t\t*****USER INTERFACE******")
                print("\t\t1. Deposite")
                print("\t\t2. Withdraw")
                print("\t\t3. Check Balance")
                print("\t\t4. Transfer money")
                print("\t\t5. View Transaction History")
                print("\t\t6. Check Available Loan")
                print("\t\t7. Apply for loan")
                print("\t\t8. Exit")
                op=(input("\t\tChoose an option:"))
                if op=='1':
                    amount=int(input("\t\t\tEnter amount:"))
                    user.deposite(bank,amount)
                elif op=='2':
                    amount=int(input("\t\t\tEnter amount:"))
                    user.withdraw(bank,amount)
                elif op=='3':
                    user.check_balance()
                elif op=='4':
                    other=int(input("\t\t\tTo Account No.:"))
                    amount=int(input("\t\t\tEnter amount:"))
                    user.transfer(bank,user,other,amount)
                elif op=='5':
                    user.show_transaction()
                elif op=='6':
                    print(f"\t\t\tAvailable loan no:{2-user.loan}")
                elif op=='7':
                    user.apply_loan(bank)
                elif op=='8':
                    break
                else:
                    print("\t\t\tInvalid Input, Try again!")

        else:
            print("\t\tInvalid Account Number or Not Resistered")
            user_Interface()
    elif n=='3':
        main_interface()
    else:
        print("\tInvalid Input,Try again!")
        user_Interface()

def Admin_interface():
    name=input("\tEnter Your Name:")
    email=input("\tEnter Your Email:")
    address=input("\tEnter Your Address:")
    admin=Admin(name,email,address)
    while True:
        print("\t\t*****Admin INTERFACE******")
        print("\t\t1. Create an Account")
        print("\t\t2. Delete an Account")
        print("\t\t3. View All Accounts")
        print("\t\t4. Check Available Bank Balance")
        print("\t\t5. Total Loan Amount")
        print("\t\t6. Lock Loan System")
        print("\t\t7. Exit")
        op=(input("\t\tChoose an option:"))
        if op=='1':
            name=input("\t\t\tEnter Your Name:")
            email=input("\t\t\tEnter Your Email:")
            address=input("\t\t\tEnter Your Address:")
            A_type=input("\t\t\tAccount Type:")
            user=User(name,email,address,A_type)
            admin.create_account(bank,user)
        elif op=='2':
            ac_no=int(input("\t\t\tEnter Account No:"))
            account=bank.find_account(ac_no)
            admin.delete_account(bank,account)
        elif op=='3':
            admin.view_accounts(bank)
        elif op=='4':
            print(f"\t\t\tThe Current balance in Bank:{bank.bank_balance} taka")
        elif op=='5':
            num=admin.No_Of_Loan(bank)
            amount=num * 20000
            print(f"\t\t\tThe loan amount:{amount} taka")
        elif op=='6':
            admin.loan_system(bank)
            print("\t\t\tThe loan system is stopped by Admin")
        elif op=='7':
            break
        else:
            print("\t\t\tInvalid Input, Try again!")
main_interface()

                  









