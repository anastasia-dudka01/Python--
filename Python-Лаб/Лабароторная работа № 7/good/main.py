from models import Car, Repair, SparePart
from repo import MemoryRepo
from notifier import PrintNotifier
from service import RepairService


def menu(service):
    while True:
        print()
        print("1 - добавить машину")
        print("2 - создать ремонт")
        print("3 - добавить запчасть")
        print("4 - показать ремонты")
        print("5 - завершить ремонт")
        print("0 - выход")
        ch = input("Выбор: ")

        if ch == "1":
            p = input("Номер: ")
            b = input("Марка: ")
            o = input("Владелец: ")
            service.register_car(Car(p, b, o))
            print("Машина добавлена")

        elif ch == "2":
            p = input("Номер: ")
            car = service.repo.find_car(p)
            if car is None:
                print("Машина не найдена")
                continue
            d = input("Описание: ")
            h = float(input("Часы: "))
            service.create_repair(Repair(car, d, h))
            print("Ремонт создан")

        elif ch == "3":
            p = input("Номер: ")
            n = input("Запчасть: ")
            pr = float(input("Цена: "))
            service.add_part(p, SparePart(n, pr))

        elif ch == "4":
            for r in service.repo.all_repairs():
                print(r.car.plate, r.description, r.status.value,
                      r.cost(), "руб.")

        elif ch == "5":
            p = input("Номер: ")
            service.finish(p)

        elif ch == "0":
            print("Пока")
            break


def main():
    repo = MemoryRepo()
    notifier = PrintNotifier()
    service = RepairService(repo, notifier)

    car = Car("А123", "Toyota", "Иванов")
    service.register_car(car)
    service.create_repair(Repair(car, "Диагностика", 2))
    service.add_part("А123", SparePart("Свечи", 1200))

    print("Стоимость:", service.calc_total("А123"))

    menu(service)


if __name__ == "__main__":
    main()