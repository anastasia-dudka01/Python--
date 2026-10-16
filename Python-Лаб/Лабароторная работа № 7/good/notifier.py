class PrintNotifier:
    def send(self, to, text):
        print("[Сообщение] " + to + ": " + text)


class FileNotifier:
    def send(self, to, text):
        print("[В файл] " + to + ": " + text)