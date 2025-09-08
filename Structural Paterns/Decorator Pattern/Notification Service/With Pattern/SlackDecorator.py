from NotifierDecorator import NotifierDecorator
from Notifier import Notifier

class SlackDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier):
        super().__init__(notifier)

    def send(self, message: str) -> None:
        self._notifier.send(message)
        print(f"Sending via Slack...\nMessage: {message}\n")