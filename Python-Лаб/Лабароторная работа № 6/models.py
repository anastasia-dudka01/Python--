from dataclasses import dataclass, field
from enum import Enum


class RepairStatus(Enum):
    ACCEPTED = "принят"
    DIAGNOSING = "диагностируется"
    REPAIRING = "ремонтируется"
    READY = "готов"
    ISSUED = "выдан"


@dataclass
class SparePart:
    name: str
    price: float


@dataclass
class Car:
    plate: str
    brand: str
    owner: str


@dataclass
class Repair:
    car: Car
    description: str
    hours: float
    status: RepairStatus = RepairStatus.ACCEPTED
    parts: list = field(default_factory=list)

    def cost(self) -> float:
        total = self.hours * 1000
        for p in self.parts:
            total = total + p.price
        return total

    def get_report_data(self) -> str:
        return ("Ремонт " + self.car.plate +
                " | " + self.car.brand +
                " | " + self.description +
                " | статус: " + self.status.value +
                " | стоимость: " + str(round(self.cost(), 2)) + " руб.")