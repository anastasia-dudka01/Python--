from models import Car, Repair, RepairStatus, SparePart
from decorators import log_call, measure_time, repeat
from context import OperationLogger
from services import RepairService, inspect_object


@log_call
def create_demo_repairs():
    service = RepairService()

    car1 = Car("А123БВ", "Toyota Camry", "Иванов")
    car2 = Car("Е456КМ", "Kia Rio", "Петров")
    car3 = Car("М789НО", "Ford Focus", "Сидоров")

    r1 = Repair(car1, "Замена масла", 1.5)
    r1.parts.append(SparePart("Масляный фильтр", 800))
    r1.parts.append(SparePart("Моторное масло", 2500))

    r2 = Repair(car2, "Замена тормозных колодок", 2.0)
    r2.parts.append(SparePart("Тормозные колодки", 3500))

    r3 = Repair(car3, "Диагностика двигателя", 1.0)
    r3.parts.append(SparePart("Свечи зажигания", 1200))
    r3.parts.append(SparePart("Масляный фильтр", 800))

    service.add_repair(r1)
    service.add_repair(r2)
    service.add_repair(r3)

    return service


@measure_time
def show_stats(service):
    print("Общая стоимость всех ремонтов: " +
          str(round(service.total_cost(), 2)) + " руб.")
    print("Самая частая запчасть: " + service.popular_parts())


@repeat(2)
def show_header():
    print("-------------------------")


def main():
    print("Автосервис")
    show_header()

    with OperationLogger("создание демо-ремонтов"):
        service = create_demo_repairs()

    print()
    print("Все ремонты:")
    service.show_all()

    print()
    show_stats(service)

    print()
    print("Меняем статус ремонта для А123БВ:")
    with OperationLogger("изменение статуса"):
        service.change_status("А123БВ", RepairStatus.REPAIRING)

    print()
    print("Интроспекция первого ремонта:")
    inspect_object(service.repairs[0])

    print()
    print("Проверка исключения:")
    try:
        service.change_status("ХХХ000", RepairStatus.READY)
    except Exception as e:
        print("Поймали ошибку: " + str(e))


if __name__ == "__main__":
    main()