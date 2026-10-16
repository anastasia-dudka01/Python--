from enum import Enum


class RepairStatus(Enum):
    ACCEPTED = "принят"
    DIAGNOSING = "диагностируется"
    REPAIRING = "ремонтируется"
    READY = "готов"
    ISSUED = "выдан"


class RepairManager:
    def __init__(self):
        self.cars = []
        self.repairs = []

    def add_car(self, plate, brand, owner):
        self.cars.append({"plate": plate, "brand": brand, "owner": owner})
        print("Машина добавлена")

    def add_repair(self, plate, description, hours):
        self.repairs.append({
            "plate": plate,
            "description": description,
            "hours": hours,
            "status": RepairStatus.ACCEPTED,
            "parts": []
        })
        print("Ремонт добавлен")

    def add_part(self, plate, name, price):
        for r in self.repairs:
            if r["plate"] == plate:
                r["parts"].append({"name": name, "price": price})

    def calc_cost(self, plate):
        for r in self.repairs:
            if r["plate"] == plate:
                total = r["hours"] * 1000
                for p in r["parts"]:
                    total = total + p["price"]
                return total
        return 0

    def change_status(self, plate, status):
        for r in self.repairs:
            if r["plate"] == plate:
                r["status"] = status
                print("Статус: " + status.value)
                print("EMAIL: клиенту " + plate + " статус изменён")
                print("SMS: клиенту " + plate + " статус изменён")

    def show_all(self):
        for r in self.repairs:
            print(r)

    def save_file(self):
        print("Сохранено в файл")

    def menu(self):
        while True:
            print("1 - добавить машину")
            print("2 - добавить ремонт")
            print("0 - выход")
            ch = input("Выбор: ")
            if ch == "1":
                p = input("Номер: ")
                b = input("Марка: ")
                o = input("Владелец: ")
                self.add_car(p, b, o)
            elif ch == "2":
                p = input("Номер: ")
                d = input("Описание: ")
                h = float(input("Часы: "))
                self.add_repair(p, d, h)
            elif ch == "0":
                break


if __name__ == "__main__":
    manager = RepairManager()
    manager.menu()