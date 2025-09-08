from ServiceProvider import ServiceProvider

class AmazonSNSServiceProvider(ServiceProvider):
    def send_message(self, message: str) -> None:
        print("Service Provider: Amazon SNS")
        print(f"Message: {message}\n")