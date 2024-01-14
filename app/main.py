from flask import Flask
from app.routes.language_routes import language_blueprint

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    # Register the blueprints
    app.register_blueprint(language_blueprint(config_object))

    return app
