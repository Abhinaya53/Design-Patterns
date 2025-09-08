from Notification import Notification
from abc import ABC, abstractmethod

class NotificationCollectionTemplate(ABC):
    def __init__(self):
        self._notifications = []

    def add_notification(self, notification: Notification):
        self._notifications.append(notification)

    def get_notifications(self):
        return self._notifications
    
    @abstractmethod
    def __iter__(self):
        pass