from person import Person
from user import User
class Admin(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    
    def create_account(self,bank,user):
        bank.add_account(user)
    
    def delete_account(self,bank,user):
        bank.remove_account(user)

    def view_accounts(self,bank):
        bank.view_all_accounts()

    def No_Of_Loan(self,bank):
        return bank.num_of_loan

    def loan_system(self,bank):
            bank.loan_system=False
    

    


