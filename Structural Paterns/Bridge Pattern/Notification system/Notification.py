from abc import ABC, abstractmethod
from ServiceProvider import ServiceProvider

class Notification(ABC):
    def __init__(self, service_provider: ServiceProvider):
        self._service_provider = service_provider
    
    def set_service_provider(self, service_provider: ServiceProvider) -> None:
        self._service_provider = service_provider
    
    @abstractmethod
    def notify(self, message: str) -> None:
        pass