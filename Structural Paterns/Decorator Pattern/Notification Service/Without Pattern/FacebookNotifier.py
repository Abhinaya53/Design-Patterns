from Notifier import Notifier

class FacebookNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending via Facebook...\nMessage: {message}\n")