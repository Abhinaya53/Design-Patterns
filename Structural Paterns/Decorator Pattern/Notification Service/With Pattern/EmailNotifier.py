from Notifier import Notifier

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending via E-Mail...\nMessage: {message}\n")