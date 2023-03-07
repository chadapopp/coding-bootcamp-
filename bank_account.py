class BankAccount:
    accounts = []
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)


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

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

account_holder1 = BankAccount(0.01, 3000)
account_holder2 = BankAccount(0.6, 3000)




account_holder1.deposit(1000).deposit(1000).deposit(1000).withdraw(1000).withdraw(500).yield_interest().display_account_info()
account_holder2.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

BankAccount.print_all_accounts()




