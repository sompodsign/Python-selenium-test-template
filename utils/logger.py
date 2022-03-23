import datetime
from loguru import logger


class CustomLogger:

    def __init__(self, log_file_name):
        self.logger = logger
        self.logger.add(f"logs/{log_file_name}.log", format="{time} {level} {message}", mode="w")

    def get_logger(self):
        return self.logger
