import logging
import json
from app.config.config import Config
import os


class CustomLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)
            cls._instance.load_configuration()
            cls._instance.setup_handlers()

        return cls._instance

    def load_configuration(self):
        try:
            with open(Config.LOGGER_CONFIG_FILE, 'r') as file:
                config_data = json.load(file)
                self._instance.log_level = getattr(logging, config_data.get('log_level', 'INFO'))

        except FileNotFoundError:
            self._instance.log_level = logging.INFO

        except json.JSONDecodeError:
            self._instance.log_level = logging.INFO

    def setup_handlers(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create a FileHandler to log messages to a file
        file_handler = logging.FileHandler(filename=os.path.join(os.getcwd(), Config.LOG_FILE))
        file_handler.setLevel(self._instance.log_level)
        file_handler.setFormatter(formatter)
        self._instance.logger.addHandler(file_handler)

        # Create a StreamHandler to log messages to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self._instance.log_level)
        console_handler.setFormatter(formatter)
        self._instance.logger.addHandler(console_handler)

    def get_logger(self):
        return self._instance.logger
