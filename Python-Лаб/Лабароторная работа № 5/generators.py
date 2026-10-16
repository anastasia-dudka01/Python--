def accounts_by_type(accounts, acc_type):
    for a in accounts:
        if a.account_type == acc_type:
            yield a


class AccountIterator:
    def __init__(self, accounts):
        self.accounts = accounts
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.accounts):
            raise StopIteration
        x = self.accounts[self.index]
        self.index = self.index + 1
        return x