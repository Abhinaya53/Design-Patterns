from ServiceProvider import ServiceProvider
from Notification import Notification

class SMSNotification(Notification):
    def __init__(self, service_provider: ServiceProvider):
        super().__init__(service_provider)
    
    def notify(self, message: str) -> None:
        print("Notification Type: SMS")
        self._service_provider.send_message(message)