
from Account import Account
from Bank import Bank

class Admin(Account):
    

    def enable_loan_feature(self,bank):
        bank.loan_feature_enabled = True
        
    def disable_loan_feature(self,bank):
        bank.loan_feature_enabled = False
    
    def check_total_available_balance(self,bank):
        return bank.total_bank_balance
    
    
    
    def check_total_bank_loan_balance(self,bank):
        return bank.total_loan_balance