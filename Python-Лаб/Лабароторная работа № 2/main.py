orders = []


def add_order():
    print()
    number = input("Номер заказа: ")
    client = input("Клиент: ")
    price = float(input("Стоимость (руб): "))
    status = input("Статус: ")

    order = {}
    order["number"] = number
    order["client"] = client
    order["price"] = price
    order["status"] = status

    orders.append(order)
    print("Заказ добавлен!")


def show_all():
    if len(orders) == 0:
        print("Заказов нет.")
        return

    print()
    print("Все заказы:")
    for i in range(len(orders)):
        o = orders[i]
        print(str(i + 1) + ") Номер: " + o["number"] +
              ", клиент: " + o["client"] +
              ", цена: " + str(o["price"]) +
              ", статус: " + o["status"])


def search_client():
    name = input("Введите имя клиента: ")

    found = []
    for o in orders:
        if o["client"] == name:
            found.append(o)

    if len(found) == 0:
        print("Ничего не найдено.")
    else:
        print("Найдено заказов: " + str(len(found)))
        for o in found:
            print("Номер: " + o["number"] +
                  ", цена: " + str(o["price"]) +
                  ", статус: " + o["status"])


def filter_status():
    status = input("Какой статус искать: ")

    result = []
    for o in orders:
        if o["status"] == status:
            result.append(o)

    if len(result) == 0:
        print("Заказов с таким статусом нет.")
    else:
        print("Найдено заказов: " + str(len(result)))
        for o in result:
            print("Номер: " + o["number"] +
                  ", клиент: " + o["client"] +
                  ", цена: " + str(o["price"]))


def sort_price():
    if len(orders) == 0:
        print("Заказов нет.")
        return

    sorted_list = []
    for o in orders:
        sorted_list.append(o)

    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j]["price"] > sorted_list[j + 1]["price"]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp

    print("Заказы по возрастанию цены:")
    for o in sorted_list:
        print("Номер: " + o["number"] +
              ", цена: " + str(o["price"]) +
              ", клиент: " + o["client"])


def show_stats():
    if len(orders) == 0:
        print("Статистики нет.")
        return

    total = 0
    for o in orders:
        total = total + o["price"]

    sredniy = total / len(orders)

    max_o = orders[0]
    min_o = orders[0]
    for o in orders:
        if o["price"] > max_o["price"]:
            max_o = o
        if o["price"] < min_o["price"]:
            min_o = o

    print()
    print("Статистика:")
    print("Всего заказов: " + str(len(orders)))
    print("Общая сумма: " + str(round(total, 2)) + " руб.")
    print("Средний чек: " + str(round(sredniy, 2)) + " руб.")
    print("Самый дорогой: №" + max_o["number"] +
          " (" + str(max_o["price"]) + " руб.)")
    print("Самый дешёвый: №" + min_o["number"] +
          " (" + str(min_o["price"]) + " руб.)")


def show_statuses():
    if len(orders) == 0:
        print("Данных нет.")
        return

    statuses = set()
    for o in orders:
        statuses.add(o["status"])

    print()
    print("Уникальные статусы:")
    for s in statuses:
        print("- " + s)


def main():
    print("==============================")
    print("        УЧЁТ ЗАКАЗОВ")
    print("==============================")

    while True:
        print()
        print("Меню:")
        print("1 - добавить заказ")
        print("2 - показать все")
        print("3 - найти по клиенту")
        print("4 - фильтр по статусу")
        print("5 - сортировка по цене")
        print("6 - статистика")
        print("7 - уникальные статусы")
        print("0 - выход")

        choice = input("Выбор: ")

        if choice == "1":
            add_order()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search_client()
        elif choice == "4":
            filter_status()
        elif choice == "5":
            sort_price()
        elif choice == "6":
            show_stats()
        elif choice == "7":
            show_statuses()
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()