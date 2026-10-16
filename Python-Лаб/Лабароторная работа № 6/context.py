class OperationLogger:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(">>> Начало операции: " + self.name)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("<<< Операция завершена успешно")
        else:
            print("<<< Ошибка в операции: " + str(exc_value))
        return False