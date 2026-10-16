from models import Car, Repair, SparePart, RepairStatus
from repo import MemoryRepo
from service import RepairService


class FakeNotifier:
    def __init__(self):
        self.messages = []

    def send(self, to, text):
        self.messages.append(text)


def test_add_car():
    repo = MemoryRepo()
    service = RepairService(repo, FakeNotifier())
    service.register_car(Car("A1", "Kia", "Петров"))
    assert len(repo.cars) == 1


def test_create_repair():
    repo = MemoryRepo()
    service = RepairService(repo, FakeNotifier())
    car = Car("A2", "Ford", "Сидоров")
    service.register_car(car)
    service.create_repair(Repair(car, "Работа", 1))
    assert len(repo.repairs) == 1


def test_calc_total():
    repo = MemoryRepo()
    service = RepairService(repo, FakeNotifier())
    car = Car("A3", "Kia", "Иванов")
    service.register_car(car)
    service.create_repair(Repair(car, "Работа", 2))
    service.add_part("A3", SparePart("Фильтр", 500))
    assert service.calc_total("A3") == 2500


def test_finish():
    repo = MemoryRepo()
    service = RepairService(repo, FakeNotifier())
    car = Car("A4", "Ford", "Петров")
    service.register_car(car)
    r = Repair(car, "Работа", 1)
    service.create_repair(r)
    service.finish("A4")
    assert r.status == RepairStatus.ISSUED


def test_notifier():
    repo = MemoryRepo()
    fake = FakeNotifier()
    service = RepairService(repo, fake)
    car = Car("A5", "Kia", "Иванов")
    service.register_car(car)
    service.create_repair(Repair(car, "Работа", 1))
    assert "Заказ-наряд создан" in fake.messages