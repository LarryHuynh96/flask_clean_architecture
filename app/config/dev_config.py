from app.config.config import Config

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://dev_user:dev_password@localhost/dev_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

