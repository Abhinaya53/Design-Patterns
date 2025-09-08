from ServiceProvider import ServiceProvider

class TwilioServiceProvider(ServiceProvider):
    def send_message(self, message: str) -> None:
        print("Service Provider: Twilio")
        print(f"Message: {message}\n")