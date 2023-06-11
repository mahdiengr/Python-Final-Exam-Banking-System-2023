from Bank import Bank
from Account import Account
from User import User
from Admin import Admin

def main():

    bank = Bank()
    user1 = User()
    user2 = User()
    account = Account()
    user1.create_accout("Mahdi",3456,"dhaka")
    user1.create_accout("Sakib", 6688,"Ctg")


    admin1 = Admin()

    print(user2.check_available_balance())
    user1.deposit(bank,500)
    user1.transfer(user2,600)
    print(user1.check_available_balance())
    user1.withdrawa(bank,200)

    admin1.create_accout("Josim", 4567, "Rajsahi")
    print(user1.check_available_balance())

    print(user2.check_available_balance())
    print(user1.account)
    print(admin1.account)


    print(admin1.check_total_available_balance(bank))
    print(bank.loan_feature_enabled)

    # print(admin1.enable_loan_feature(bank))
    # print(bank.loan_feature_enabled)

    # print(admin1.disable_loan_feature(bank))


    print(admin1.check_total_bank_loan_balance(bank))
    print(user1.get_transaction_history())
    user1.take_loan(bank)
    print(admin1.check_total_bank_loan_balance(bank))
    print(user1.get_transaction_history())


if __name__ == '__main__':
    main()




