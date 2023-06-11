from Account import Account


class User(Account):
    # def __init__(self) -> None:
    #     super().__init__(self)
    
       

    def transfer(self, other_account, amount):
        if self.balance > amount:
            self.balance -= amount
            other_account.balance +=amount
            self.transaction_history.append(f"Transferred: {amount}")
            
        else:
            print("Not enough amount on Yours Account")


    
    def take_loan(self, bank):
        if bank.loan_feature_enabled:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            bank.total_loan_balance += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
        else:
            print("Bank loan offer off at the moment!")
            

    def check_transfer_history(self):
       return self.transaction_history
        
    
    def check_available_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history