from exceptions import AccountNotFoundError
from exceptions import InsufficientFundsError
from exceptions import InvalidAmountError


class BankService:
    def __init__(self, storage):
        self.storage = storage

    def add_account(self, account):
        accounts = self.storage.load()
        for a in accounts:
            if a.number == account.number:
                print("Счёт с таким номером уже существует.")
                return
        accounts.append(account)
        self.storage.save(accounts)
        print("Счёт добавлен.")

    def show_all(self):
        accounts = self.storage.load()
        if len(accounts) == 0:
            print("Счетов пока нет.")
            return
        print()
        print("Все счета:")
        for a in accounts:
            print("  " + a.show_info())

    def find_account(self, number):
        accounts = self.storage.load()
        for a in accounts:
            if a.number == number:
                return a
        raise AccountNotFoundError("Счёт №" + number + " не найден")

    def deposit(self, number, amount):
        if amount <= 0:
            raise InvalidAmountError("Сумма должна быть больше нуля")
        accounts = self.storage.load()
        found = None
        for a in accounts:
            if a.number == number:
                found = a
                break
        if found is None:
            raise AccountNotFoundError("Счёт №" + number + " не найден")
        found.balance = found.balance + amount
        self.storage.save(accounts)
        print("Пополнение выполнено. Новый баланс: " +
              str(round(found.balance, 2)) + " руб.")

    def withdraw(self, number, amount):
        if amount <= 0:
            raise InvalidAmountError("Сумма должна быть больше нуля")
        accounts = self.storage.load()
        found = None
        for a in accounts:
            if a.number == number:
                found = a
                break
        if found is None:
            raise AccountNotFoundError("Счёт №" + number + " не найден")
        if amount > found.balance:
            raise InsufficientFundsError("Недостаточно средств на счёте")
        found.balance = found.balance - amount
        self.storage.save(accounts)
        print("Снятие выполнено. Новый баланс: " +
              str(round(found.balance, 2)) + " руб.")

    def show_balance(self, number):
        account = self.find_account(number)
        print("Баланс счёта №" + account.number + ": " +
              str(round(account.balance, 2)) + " руб.")
        return account.balance