from Notification import Notification
from EmailNotification import EmailNotification
from PushNotification import PushNotification
from SMSNotification import SMSNotification
from NotificationCollectionTemplate import NotificationCollectionTemplate

class NotificationManager:
    def __init__(self):
        self.__email_notifications = EmailNotification()
        self.__push_notifications = PushNotification()
        self.__SMS_notifications = SMSNotification()
    
    def add_email_notification(self, message: str):
        message = f"E-Mail: {message}"
        self.__email_notifications.add_notification(Notification(message))
    
    def add_sms_notification(self, message: str):
        message = f"SMS: {message}"
        self.__SMS_notifications.add_notification(Notification(message))
    
    def add_push_notification(self, message: str):
        message = f"Push: {message}"
        self.__push_notifications.add_notification(Notification(message))
    
    def print_all_notifications(self):
        self.print_notifications(self.__email_notifications)
        self.print_notifications(self.__SMS_notifications)
        self.print_notifications(self.__push_notifications)

    def print_notifications(self, collection: NotificationCollectionTemplate):
        print()
        for notification in collection:
            print(notification)
        print()