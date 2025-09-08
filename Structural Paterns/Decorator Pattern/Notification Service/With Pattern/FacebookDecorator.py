from NotifierDecorator import NotifierDecorator
from Notifier import Notifier

class FacebookDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier):
        super().__init__(notifier)

    def send(self, message: str) -> None:
        self._notifier.send(message)
        print(f"Sending via Facebook...\nMessage: {message}\n")