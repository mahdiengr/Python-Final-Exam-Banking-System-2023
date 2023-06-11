from Bank import Bank

class Account(Bank):
    def __init__(self) -> None:
        self.account = []
        self.loan_features = False
        self.balance = 0
        self.transaction_history = []
        
    def create_accout(self, name, phone_number, address):
        self.name = name
        self.phone_nmbr = phone_number
        self.address = address
        self.account.append((self.name,self.phone_nmbr,self.address))

    
    def deposit(self,bank,amount):
        if amount > 0:
            self.balance += amount
            bank.total_bank_balance +=amount
            self.transaction_history.append(f"Deposited: {amount}")
    
            
        else:
            print("Invalid deposit amount")
         

    
    def withdrawa(self,bank,amount):
        if amount > 0:
            if self.balance > amount:
                self.balance -= amount 
                bank.total_bank_balance -=amount
                self.transaction_history.append(f"Withdrawn: {amount}")
            else:
                print(f'Sorry Not enough Balance {self.balance}')
        else:
            print("Wrong Amount Withdrawa") 