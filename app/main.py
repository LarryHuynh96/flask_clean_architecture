from flask import Flask
from app.routes.language_routes import language_blueprint
from app.log_handlers.log_handler import CustomLogger


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    with app.app_context():
        logger_instance = CustomLogger()
        logger = logger_instance.get_logger()
        # Register the blueprints
        app.register_blueprint(language_blueprint(config_object))
        logger.info("Flask App was created")

    return app
