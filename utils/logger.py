import datetime
from loguru import logger


class CustomLogger:

    # date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __init__(self, log_file_name):
        self.logger = logger
        self.logger.add(f"logs/{log_file_name}.log", rotation="1 day", retention="7 days",
                        format="{time} {level} {message}")

    def get_logger(self):
        return self.logger
