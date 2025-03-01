class BankAccount:

    __account_number = None
    __account_holder = None
    __account_balance = 0
    def __init__(self,account_number,account_holder):
        self.account_number =account_number
        self.account_holder = account_holder

    def account_info(self,account_holder):
        
        print(f"Hello {account_holder} welcome to HDFC")

    def deposit(self,value):
        BankAccount.__account_balance +=value
        print(f"You have deposited {value} ")

    def withdrawl(self,value):
        BankAccount.__account_balance -= value
        print(f"Your withdrawl {value} ")

    def get_account_details(self):

        print("Your account details")

        print(f"name:{self.account_holder}")
        print(f"account number:{self.account_number}")
        print(f"balance:{BankAccount.__account_balance}")
        
obj = BankAccount(12345,'Dev')
obj.__account_holder,obj.__account_number = "Dev",12345
obj.account_info('Dev')
obj.deposit(65000)
obj.withdrawl(2000)
obj.deposit(78000)


obj.get_account_details()



