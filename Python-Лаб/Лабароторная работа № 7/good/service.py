from models import Repair, RepairStatus


class RepairService:
    def __init__(self, repo, notifier):
        self.repo = repo
        self.notifier = notifier

    def register_car(self, car):
        self.repo.add_car(car)

    def create_repair(self, repair):
        self.repo.add_repair(repair)
        self.notifier.send(repair.car.owner, "Заказ-наряд создан")

    def add_part(self, plate, part):
        for r in self.repo.all_repairs():
            if r.car.plate == plate:
                r.parts.append(part)
                return

    def calc_total(self, plate):
        for r in self.repo.all_repairs():
            if r.car.plate == plate:
                return r.cost()
        return 0

    def finish(self, plate):
        for r in self.repo.all_repairs():
            if r.car.plate == plate:
                r.status = RepairStatus.ISSUED
                self.notifier.send(r.car.owner, "Ремонт завершён")
                return