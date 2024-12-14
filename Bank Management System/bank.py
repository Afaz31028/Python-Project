from datetime import datetime
class Bank:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.bank_balance=10000000
        self.Max_loan=20000
        self.txt=2024100
        self.num_of_loan=0
        self.accounts=[]
        self.loan_system=True

    def add_account(self,user):
        if user not in self.accounts:
            acc_no=self.txt+len(self.accounts)+1
            user.account_no=acc_no
            self.accounts.append(user)
            print(f"\t\t\t{user.name},Your Account No:{user.account_no}")

    def remove_account(self,user):
        if user in self.accounts:
            self.accounts.remove(user)
            print(f"\t\t\tThe account removed whice account no:{user.account_no}")
        else:
            print("\t\t\tThe account does not exist")
    
    def derived_ac_no(self,user):
        for account in self.accounts:
            if user in self.accounts:
                print(f'\n\t\t{user.name}, Your Account Number:{user.account_no}\n')
                break

    def valid_account(self,obj):
        for user in self.accounts:
            if user == obj:
                return user
        return None
    
    def find_account(self,ac_no):
        for account in self.accounts:
            if ac_no == account.account_no:
                return account
        return None
    
    def view_all_accounts(self):
        print(f"\n\t\tAccount No.     Name       Address       Email")
        for account in self.accounts:
            print(f"\t\t {account.account_no}  {account.name}    {account.address}   {account.email}")
    
    def send_loan(self,user):
        if self.bank_balance< self.Max_loan:
            print("\n\t\t\tThe ABC bank is bankrupt!!!\n")
        elif self.loan_system and user.loan<2:
            user.balance+=self.Max_loan
            self.bank_balance-=self.Max_loan
            self.num_of_loan+=1
            user.loan+=1
            user.transaction.append([datetime.now(),self.Max_loan,"Loan"])
            print(f"\n\t\t\t20000 taka added successfully in your aaccount\n")
        elif user.loan==2:
            print("\n\t\t\tThe maximum num. of loan is 2 that you have already crossed.\n")
        else:
            print("\n\t\t\tThe loan system stopped currenlty,contact bank manager.\n")
    
    

    
