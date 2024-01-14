from app.config.config import Config

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://prod_user:prod_password@localhost/prod_db'