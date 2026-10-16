import json
import csv
from models import BankAccount


class JsonStorage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, accounts):
        data = []
        for a in accounts:
            data.append(a.to_dict())

        file = open(self.filename, "w", encoding="utf-8")
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

    def load(self):
        try:
            file = open(self.filename, "r", encoding="utf-8")
            data = json.load(file)
            file.close()
        except FileNotFoundError:
            return []

        accounts = []
        for item in data:
            accounts.append(BankAccount.from_dict(item))
        return accounts

    def export_csv(self, filename):
        accounts = self.load()
        file = open(filename, "w", encoding="utf-8", newline="")
        writer = csv.writer(file)
        writer.writerow(["number", "owner", "balance", "account_type"])
        for a in accounts:
            writer.writerow([a.number, a.owner, a.balance, a.account_type])
        file.close()
        print("Данные экспортированы в " + filename)