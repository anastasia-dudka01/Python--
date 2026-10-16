from models import BankAccount
from services import BankService
from storage import JsonStorage
from exceptions import AccountNotFoundError
from exceptions import InsufficientFundsError
from exceptions import InvalidAmountError


def main():
    storage = JsonStorage("accounts.json")
    service = BankService(storage)

    print("==============================")
    print("     БАНКОВСКИЕ СЧЕТА")
    print("==============================")

    while True:
        print()
        print("Меню:")
        print("1 - добавить счёт")
        print("2 - показать все счета")
        print("3 - найти счёт")
        print("4 - пополнить")
        print("5 - снять")
        print("6 - показать баланс")
        print("7 - экспорт в CSV")
        print("0 - выход")

        choice = input("Выбор: ")

        if choice == "1":
            number = input("Номер счёта: ")
            owner = input("Владелец: ")
            try:
                balance = float(input("Начальный баланс: "))
            except ValueError:
                print("Ошибка: нужно ввести число.")
                continue
            account_type = input("Тип счёта (текущий/сберегательный): ")
            acc = BankAccount(number, owner, balance, account_type)
            service.add_account(acc)

        elif choice == "2":
            service.show_all()

        elif choice == "3":
            number = input("Номер счёта: ")
            try:
                acc = service.find_account(number)
                print("Найден: " + acc.show_info())
            except AccountNotFoundError as e:
                print("Ошибка: " + str(e))

        elif choice == "4":
            number = input("Номер счёта: ")
            try:
                amount = float(input("Сумма пополнения: "))
            except ValueError:
                print("Ошибка: нужно ввести число.")
                continue
            try:
                service.deposit(number, amount)
            except AccountNotFoundError as e:
                print("Ошибка: " + str(e))
            except InvalidAmountError as e:
                print("Ошибка: " + str(e))

        elif choice == "5":
            number = input("Номер счёта: ")
            try:
                amount = float(input("Сумма снятия: "))
            except ValueError:
                print("Ошибка: нужно ввести число.")
                continue
            try:
                service.withdraw(number, amount)
            except AccountNotFoundError as e:
                print("Ошибка: " + str(e))
            except InvalidAmountError as e:
                print("Ошибка: " + str(e))
            except InsufficientFundsError as e:
                print("Ошибка: " + str(e))

        elif choice == "6":
            number = input("Номер счёта: ")
            try:
                service.show_balance(number)
            except AccountNotFoundError as e:
                print("Ошибка: " + str(e))

        elif choice == "7":
            storage.export_csv("accounts.csv")

        elif choice == "0":
            print("Пока!")
            break

        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()