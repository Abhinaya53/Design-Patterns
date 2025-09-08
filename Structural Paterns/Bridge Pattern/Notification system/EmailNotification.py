from ServiceProvider import ServiceProvider
from Notification import Notification

class EmailNotification(Notification):
    def __init__(self, service_provider: ServiceProvider):
        super().__init__(service_provider)
    
    def notify(self, message: str) -> None:
        print("Notification Type: Email")
        self._service_provider.send_message(message)