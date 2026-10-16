from models import CurrentAccount, SavingsAccount
from operations import filter_accs, get_balances, sort_accs, total_balance
from generators import accounts_by_type, AccountIterator

accounts = []
accounts.append(CurrentAccount("001", "Иванов", 15000, "текущий", 5000))
accounts.append(SavingsAccount("002", "Петров", 32000, "сберегательный", 7))
accounts.append(CurrentAccount("003", "Сидорова", -1500, "текущий", 3000))
accounts.append(SavingsAccount("004", "Кузнецов", 80000, "сберегательный", 9))
accounts.append(CurrentAccount("005", "Смирнов", 2500, "текущий", 2000))
accounts.append(SavingsAccount("006", "Иванов", -300, "сберегательный", 5))

print("Анализ банковских счетов")
print()

print("Все счета:")
for a in accounts:
    print(a.show())

print()
print("Счета с положительным балансом:")
positive = list(filter_accs(accounts, lambda a: a.balance > 0))
for a in positive:
    print(a.show())

print()
print("Балансы:")
balances = get_balances(accounts)
print(balances)

print()
print("Сортировка по балансу:")
s = sort_accs(accounts, lambda a: a.balance)
for a in s:
    print(a.number, a.owner, a.balance)

print()
print("Общий баланс:", total_balance(accounts))

print()
if any(a.balance < 0 for a in accounts):
    print("Есть отрицательные счета")
else:
    print("Отрицательных счетов нет")

print()
print("Все с номерами:", all(a.number != "" for a in accounts))

print()
print("Счета с балансом больше 20000:")
rich = [a for a in accounts if a.balance > 20000]
for a in rich:
    print(a.number, a.balance)

print()
print("Сберегательные счета:")
for a in accounts_by_type(accounts, "сберегательный"):
    print(a.show())

print()
print("Первые два счёта через итератор:")
it = AccountIterator(accounts)
try:
    print(next(it).number)
    print(next(it).number)
except StopIteration:
    print("конец")

print()
print("Все номера:")
print([a.number for a in accounts])