from Bank_sample import Bank, Account, User, Admin

def main():
    bank = Bank()

    admin = Admin(bank)
    admin.create_account("John Doe")
    admin.create_account("Jane Smith")

    user1 = User("John Doe")
    user2 = User("Jane Smith")
    
    user1.deposit(200)
    user1.withdraw(100)
    user1.transfer(user2, 300)

    print(user1.get_transaction_history())

    user1.take_loan(bank)

   
   
    

    print(user1.check_balance())
    print(user2.check_balance())
    

    print(admin.check_total_balance())
    print(admin.check_total_loan_amount())



    
if __name__ == '__main__':
    main()