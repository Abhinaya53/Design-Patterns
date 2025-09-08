from AppConfig import AppConfig

config = AppConfig.get_instance()
print(f"API Key: {config.get_api_key()}")
print(f"Database URL: {config.get_db_url()}")