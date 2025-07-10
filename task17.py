class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} hisobiga {amount} so'm qo'shildi.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.owner} hisobida yetarli mablag' yo'q.")
        else:
            self.balance -= amount
            print(f"{self.owner} hisobidan {amount} so'm olindi.")

    def get_balance(self):
        return self.balance

def task17():
    a1 = BankAccount("Ali", 1000)
    a2 = BankAccount("Vali", 2000)
    a3 = BankAccount("Sami", 1500)
    a4 = BankAccount("Olim", 1800)
    a5 = BankAccount("Aziz", 1700)

    accounts = [a1, a2, a3, a4, a5]
    total_balance = sum(acc.get_balance() for acc in accounts)
    print("Jami balans:", total_balance)