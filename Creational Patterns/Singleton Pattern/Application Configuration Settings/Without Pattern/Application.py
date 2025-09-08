from AppConfig import AppConfig

config = AppConfig()
print(f"API Key: {config.get_api_key()}")
print(f"Database URL: {config.get_db_url()}") 