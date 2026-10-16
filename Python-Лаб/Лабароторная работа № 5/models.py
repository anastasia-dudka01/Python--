class BankAccount:
    def __init__(self, number, owner, balance, account_type):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.account_type = account_type

    def show(self):
        return "№" + self.number + " " + self.owner + " " + str(self.balance) + " руб"


class CurrentAccount(BankAccount):
    def __init__(self, number, owner, balance, account_type, overdraft):
        super().__init__(number, owner, balance, account_type)
        self.overdraft = overdraft

    def show(self):
        return "Текущий " + super().show()


class SavingsAccount(BankAccount):
    def __init__(self, number, owner, balance, account_type, percent):
        super().__init__(number, owner, balance, account_type)
        self.percent = percent

    def show(self):
        return "Сберегательный " + super().show()