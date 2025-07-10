class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Yangi balans:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Yangi balans:", self.balance)
        else:
            print("Xatolik: yetarli mablag' yo'q")
    def show_balance(self):
        print("Balans:", self.balance)

acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Vali", 500)
acc3 = BankAccount("Sami", 800)

acc1.deposit(200)
acc2.withdraw(100)
acc3.deposit(300)

acc1.show_balance()
acc2.show_balance()
acc3.show_balance()