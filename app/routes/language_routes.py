# app/routes/language_routes.py
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.adapters.language_adapter import LanguageAdapter
from app.controllers.language_controller import LanguageController
from app.use_cases.language_use_case import LanguageUseCase

def language_blueprint(config_object):
    language_blueprint = Blueprint('language', __name__)
    api = Api(language_blueprint)

    class LanguageResource(Resource):
        def __init__(self):
            self.config_object = config_object
            self.engine = create_engine(self.config_object.SQLALCHEMY_DATABASE_URI)
            self.language_repository = LanguageAdapter(self.engine)
            self.language_controller = LanguageController(LanguageUseCase(self.language_repository))
            super().__init__()

        def get(self):
            session = sessionmaker(bind=self.engine)()

            try:
                languages = self.language_controller.get_all_languages()
                return languages
            except Exception as e:
                print(f"Error retrieving languages: {e}")
                return []
            finally:
                session.close()

    api.add_resource(LanguageResource, '/languages')

    return language_blueprint
