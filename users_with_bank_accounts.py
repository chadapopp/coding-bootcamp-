class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        if self.balance == 0:
            self.balance = self.balance + amount
        else:
            self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        if self.balance > 0:
            print(f"Balance: {self.balance}")

        elif self.balance > 0:
            print((f"Account balance is -{self.balance}"))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self





class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  
        # BankAccount(int_rate=0.02, balance=0)

    def open_new_account(self, int_rate = 0.02, balance = 0, account_name = "checking"):
        new_account = BankAccount(int_rate, balance)
        self.accounts[account_name] = new_account
        return self


    def make_deposit(self,amount, account_name = "checking"):
        self.accounts[account_name].deposit(amount) 
        return self

    def make_withdraw(self,amount,account_name):
        self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self,account_name):
        print(self.name)
        self.accounts[account_name].display_account_info()
        return self


chad = User("Chad Popp", "chadapopp@outlook.com")
chad.open_new_account(0.5, 0)
chad.make_deposit(100).display_user_balance("checking")
chad.open_new_account(0, 1000, "savings").display_user_balance("savings")

John = User("John Doe", "jdoe@email.com")
John.open_new_account(.02, 2000, "savings").display_user_balance("savings")

# account_holder1 = User("Chad", "chadapopp@outlook.com")
# account_holder2 = User("John", "jdoe@email.com")


# account_holder1.make_deposit(200).make_deposit(500).display_user_balance()
# account_holder2.make_deposit(500).make_deposit(500).make_withdraw(250).display_user_balance()