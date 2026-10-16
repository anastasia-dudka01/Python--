from typing import Protocol


class Repo(Protocol):
    def add_car(self, car):
        ...

    def add_repair(self, repair):
        ...

    def all_repairs(self):
        ...

    def find_car(self, plate):
        ...


class Notifier(Protocol):
    def send(self, to, text):
        ...