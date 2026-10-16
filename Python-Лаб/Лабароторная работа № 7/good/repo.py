class MemoryRepo:
    def __init__(self):
        self.cars = []
        self.repairs = []

    def add_car(self, car):
        self.cars.append(car)

    def add_repair(self, repair):
        self.repairs.append(repair)

    def all_repairs(self):
        return self.repairs

    def find_car(self, plate):
        for c in self.cars:
            if c.plate == plate:
                return c
        return None