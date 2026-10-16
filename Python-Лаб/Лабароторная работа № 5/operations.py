def filter_accs(accounts, check):
    return filter(check, accounts)


def get_balances(accounts):
    result = []
    for a in accounts:
        result.append(a.balance)
    return result


def sort_accs(accounts, key_func):
    return sorted(accounts, key=key_func)


def total_balance(accounts):
    s = 0
    for a in accounts:
        s = s + a.balance
    return s