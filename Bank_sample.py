class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name):
        account = Account(name)
        self.accounts.append(account)

    # def update_total_balance(self):
    #     self.total_balance = sum(account.balance for account in self.accounts)


    def check_total_balance(self):
        return self.total_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False
    


class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        b1=Bank()
        b1.total_balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
       

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return self.balance

    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {other_account.name}")
            other_account.transaction_history.append(f"Received: {amount} from {self.name}")
        else:
            print("Insufficient funds!")

    def take_loan(self, bank):
        if bank.loan_feature_enabled:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            bank.total_loan_amount += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
        else:
            print("Bank does not offer loans at the moment!")

    def get_transaction_history(self):
        return self.transaction_history


class User:
    def __init__(self, name):
        self.name = name
        self.account = Account(name)

    def deposit(self, amount):
        self.account.deposit(amount)

    def withdraw(self, amount):
        self.account.withdraw(amount)

    def check_balance(self):
        return self.account.check_balance()

    def transfer(self, other_user, amount):
        self.account.transfer(other_user.account, amount)

    def take_loan(self, bank):
        self.account.take_loan(bank)

    def get_transaction_history(self):
        return self.account.get_transaction_history()


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name):
        self.bank.create_account(name)

    def check_total_balance(self):
        return self.bank.check_total_balance()

    def check_total_loan_amount(self):
        return self.bank.check_total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()



