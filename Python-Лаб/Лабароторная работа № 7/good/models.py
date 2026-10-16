from enum import Enum


class RepairStatus(Enum):
    ACCEPTED = "принят"
    DIAGNOSING = "диагностируется"
    REPAIRING = "ремонтируется"
    READY = "готов"
    ISSUED = "выдан"


class Car:
    def __init__(self, plate, brand, owner):
        self.plate = plate
        self.brand = brand
        self.owner = owner


class SparePart:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Repair:
    def __init__(self, car, description, hours):
        self.car = car
        self.description = description
        self.hours = hours
        self.status = RepairStatus.ACCEPTED
        self.parts = []

    def cost(self):
        total = self.hours * 1000
        for p in self.parts:
            total = total + p.price
        return total


# разные типы работ (для OCP)
class RepairType:
    def price(self, hours):
        return hours * 1000


class DiagnosticRepair(RepairType):
    def price(self, hours):
        return hours * 800


class BodyRepair(RepairType):
    def price(self, hours):
        return hours * 1500