from Notification import Notification
from NotificationCollectionTemplate import NotificationCollectionTemplate

class SMSNotification(NotificationCollectionTemplate):

    def __iter__(self):
        return self._SMSNotificationIterator(self.get_notifications())

    class _SMSNotificationIterator:
        def __init__(self, notifications):
            self.__position = 0
            self._notifications = notifications

        def __iter__(self):
            return self

        def __next__(self):
            if self.__position < len(self._notifications):
                notification = self._notifications[self.__position]
                self.__position += 1
                return notification
            else:
                raise StopIteration