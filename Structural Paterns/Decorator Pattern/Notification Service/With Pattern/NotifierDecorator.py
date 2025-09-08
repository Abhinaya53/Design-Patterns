from Notifier import Notifier

class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, message: str) -> None:
        self._notifier.send(message)