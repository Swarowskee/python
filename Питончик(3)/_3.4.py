#coding=utf-8
class Wallet:
    payment_system = "MasterCard"  

    def __init__(self, name: str, currency: str, balance: float):
        self.name = name
        self.currency = currency
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"баланс {self.name} успешно пополнен на {amount} {self.currency}")

    def pay(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"оплата в размере {amount} {self.currency} прошла успешно")
        else:
            print("недостаточно средств на балансе для совершения операции")

    def get_balance_info(self):
        print(f"на балансе кошелька {self.name} {self.balance} {self.currency}")

    def delete_account(self):
        del self.name
        del self.currency
        del self.balance
        print("счет удален")

my_wallet = Wallet("MyWallet", "USD", 100.0)
my_wallet.get_balance_info()
my_wallet.deposit(502.0)
my_wallet.get_balance_info()
my_wallet.pay(322)
my_wallet.get_balance_info()
my_wallet.pay(480)  
my_wallet.delete_account()
