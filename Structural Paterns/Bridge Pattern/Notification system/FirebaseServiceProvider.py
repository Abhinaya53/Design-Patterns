from ServiceProvider import ServiceProvider

class FirebaseServiceProvider(ServiceProvider):
    def send_message(self, message: str) -> None:
        print("Service Provider: Firebase")
        print(f"Message: {message}\n")