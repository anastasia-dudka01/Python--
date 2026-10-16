class BankAccount:
    def __init__(self, number, owner, balance, account_type):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.account_type = account_type

    def to_dict(self):
        return {
            "number": self.number,
            "owner": self.owner,
            "balance": self.balance,
            "account_type": self.account_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["number"],
            data["owner"],
            data["balance"],
            data["account_type"]
        )

    def show_info(self):
        return ("Счёт №" + self.number +
                " | Владелец: " + self.owner +
                " | Баланс: " + str(round(self.balance, 2)) + " руб." +
                " | Тип: " + self.account_type)