from NotificationManager import NotificationManager

notifications = ["Hello", "I am Abhinaya", "How are you doing?"]
manager = NotificationManager()

for notification in notifications:
    manager.add_email_notification(notification)
    manager.add_push_notification(notification)
    manager.add_sms_notification(notification)

manager.print_all_notifications()