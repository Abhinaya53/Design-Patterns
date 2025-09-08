from ServiceProvider import ServiceProvider
from TwilioServiceProvider import TwilioServiceProvider
from AmazonSNSServiceProvider import AmazonSNSServiceProvider
from FirebaseServiceProvider import FirebaseServiceProvider
from Notification import Notification
from EmailNotification import EmailNotification
from SMSNotification import SMSNotification
from PushNotification import PushNotification

class Client:
    def send_all_notifications(self, notification: Notification) -> None:
        message = "You order 123 is on the way."
        
        notification.set_service_provider(TwilioServiceProvider())
        notification.notify(message)

        notification.set_service_provider(AmazonSNSServiceProvider())
        notification.notify(message)

        notification.set_service_provider(FirebaseServiceProvider())
        notification.notify(message)
    
    def main(self) -> None:
        self.send_all_notifications(EmailNotification(TwilioServiceProvider()))
        self.send_all_notifications(SMSNotification(TwilioServiceProvider()))
        self.send_all_notifications(PushNotification(TwilioServiceProvider()))

if __name__ == "__main__":
    client = Client()
    client.main()