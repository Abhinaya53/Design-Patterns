from ServiceProvider import ServiceProvider
from Notification import Notification

class PushNotification(Notification):
    def __init__(self, service_provider: ServiceProvider):
        super().__init__(service_provider)
    
    def notify(self, message: str) -> None:
        print("Notification Type: Push")
        self._service_provider.send_message(message)