import os


class Config:
    # General Config
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://dev_user:dev_password@localhost/dev_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGER_CONFIG_FILE = os.path.join(os.getcwd(), 'logger_config.json')
    LOG_FILE = 'app_log.log'
