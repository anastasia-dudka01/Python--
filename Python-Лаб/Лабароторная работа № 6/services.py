import inspect
from models import Repair, RepairStatus, SparePart


class RepairService:

    def __init__(self):
        self.repairs = []

    def add_repair(self, repair):
        self.repairs.append(repair)

    def show_all(self):
        if len(self.repairs) == 0:
            print("Ремонтов пока нет.")
            return
        for r in self.repairs:
            print(r.get_report_data())

    def change_status(self, plate, new_status):
        for r in self.repairs:
            if r.car.plate == plate:
                r.status = new_status
                print("Статус изменён на: " + new_status.value)
                return
        print("Ремонт для машины " + plate + " не найден.")

    def total_cost(self):
        total = 0
        for r in self.repairs:
            total = total + r.cost()
        return total

    def popular_parts(self):
        counts = {}
        for r in self.repairs:
            for p in r.parts:
                if p.name in counts:
                    counts[p.name] = counts[p.name] + 1
                else:
                    counts[p.name] = 1

        best_name = ""
        best_count = 0
        for name in counts:
            if counts[name] > best_count:
                best_count = counts[name]
                best_name = name

        if best_count == 0:
            return "нет данных"
        return best_name + " (" + str(best_count) + " раз)"


def inspect_object(obj):
    print("=== ИНФОРМАЦИЯ ОБ ОБЪЕКТЕ ===")
    print("Тип: " + str(type(obj)))
    print("Класс: " + obj.__class__.__name__)
    print("Атрибуты: " + str([a for a in dir(obj) if not a.startswith("__")]))
    if hasattr(obj, "status"):
        print("Статус: " + obj.status.value)
    if hasattr(obj, "cost"):
        print("Стоимость: " + str(round(obj.cost(), 2)) + " руб.")
    print("Сигнатура метода get_report_data: " +
          str(inspect.signature(obj.get_report_data)))