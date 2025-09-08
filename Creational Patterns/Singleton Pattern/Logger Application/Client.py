from Logger import Logger

logger = Logger.get_instance()
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")