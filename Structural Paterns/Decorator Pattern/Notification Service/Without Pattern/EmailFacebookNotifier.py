from EmailNotifier import EmailNotifier
from FaceboofNotifier import FacebookNotifier

class EmailFacebookNotifier(EmailNotifier):
    def send(self, message):
        super().send(message)
        print(f"Sending via Facebook...\nMessage: {message}\n")